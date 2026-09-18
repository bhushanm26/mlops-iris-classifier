"""
Stage 4: Data Validation.
Validates schema, nulls, categories, and numeric ranges.
"""

import argparse
import logging
import sys

import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("validate")


EXPECTED_COLUMNS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "species",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
    "petal_length_bin",
]

VALID_SPECIES = {
    "setosa",
    "versicolor",
    "virginica",
}

RANGES = {
    "sepal length (cm)": (3.0, 9.0),
    "sepal width (cm)": (1.5, 5.5),
    "petal length (cm)": (0.5, 8.0),
    "petal width (cm)": (0.05, 3.0),
}


class DataValidationError(Exception):
    """Raised when dataset validation fails."""


def validate_data(input_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)

    errors = []

    missing_columns = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        errors.append(
            f"Missing columns: {missing_columns}"
        )

    null_counts = df[EXPECTED_COLUMNS].isna().sum()

    for col, count in null_counts.items():
        if count > 0:
            errors.append(
                f"Column '{col}' contains {count} null values"
            )

    if "species" in df.columns:
        invalid_species = (
            set(df["species"].dropna()) - VALID_SPECIES
        )

        if invalid_species:
            errors.append(
                f"Invalid species values: {invalid_species}"
            )

    for col, (min_val, max_val) in RANGES.items():
        if col in df.columns:
            invalid = df[
                (df[col] < min_val) |
                (df[col] > max_val)
            ]

            if not invalid.empty:
                errors.append(
                    f"Column '{col}' has {len(invalid)} "
                    f"values outside range "
                    f"[{min_val}, {max_val}]"
                )

    if errors:
        for error in errors:
            logger.error(error)

        raise DataValidationError(
            f"Validation failed with {len(errors)} error(s)"
        )

    logger.info(
        "Validation passed: %d rows, %d columns",
        len(df),
        len(df.columns)
    )

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="data/processed/iris_features.csv"
    )

    args = parser.parse_args()

    try:
        validate_data(args.input)
    except DataValidationError as exc:
        logger.error(str(exc))
        sys.exit(1)
