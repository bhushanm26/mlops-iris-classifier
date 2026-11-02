
"""
Unit tests for data validation.
"""

import pandas as pd
import pytest

from src.pipeline.validate import validate, DataValidationError


def create_valid_dataframe():
    return pd.DataFrame({
        "sepal_length": [5.1],
        "sepal_width": [3.5],
        "petal_length": [1.4],
        "petal_width": [0.2],
        "species": ["setosa"],
        "sepal_area": [17.85],
        "petal_area": [0.28],
        "sepal_to_petal_length_ratio": [3.64],
        "petal_length_bin": ["small"],
    })


def test_valid_data_passes_validation(tmp_path):
    df = create_valid_dataframe()

    input_path = tmp_path / "valid.csv"
    df.to_csv(input_path, index=False)

    result = validate(str(input_path))

    assert isinstance(result, pd.DataFrame)
    assert not result.empty


def test_missing_required_column_fails_validation(tmp_path):
    df = create_valid_dataframe()
    df = df.drop(columns=["sepal_length"])

    input_path = tmp_path / "missing_column.csv"
    df.to_csv(input_path, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_path))


def test_invalid_species_fails_validation(tmp_path):
    df = create_valid_dataframe()
    df.loc[0, "species"] = "invalid_species"

    input_path = tmp_path / "invalid_species.csv"
    df.to_csv(input_path, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_path))


def test_out_of_range_values_fail_validation(tmp_path):
    df = create_valid_dataframe()
    df.loc[0, "sepal_length"] = 100.0

    input_path = tmp_path / "out_of_range.csv"
    df.to_csv(input_path, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_path))

