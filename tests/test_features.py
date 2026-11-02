
"""
Unit tests for feature engineering.
"""

import pandas as pd
from src.pipeline.features import engineer_features


def test_sepal_and_petal_area_computed_correctly(tmp_path):
    df = pd.DataFrame({
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [4.0],
        "petal length (cm)": [2.0],
        "petal width (cm)": [1.0],
        "species": ["setosa"],
    })

    in_path = tmp_path / "in.csv"
    out_path = tmp_path / "out.csv"

    df.to_csv(in_path, index=False)

    result = engineer_features(str(in_path), str(out_path))

    assert result.loc[0, "sepal_area"] == 20.0
    assert result.loc[0, "petal_area"] == 2.0
    assert result.loc[0, "sepal_to_petal_length_ratio"] == 2.5


def test_petal_length_bin_is_created(tmp_path):
    df = pd.DataFrame({
        "sepal length (cm)": [5.0, 6.0, 7.0],
        "sepal width (cm)": [4.0, 3.0, 3.5],
        "petal length (cm)": [1.0, 3.0, 5.0],
        "petal width (cm)": [0.2, 1.0, 1.5],
        "species": ["setosa", "versicolor", "virginica"],
    })

    in_path = tmp_path / "in.csv"
    out_path = tmp_path / "out.csv"

    df.to_csv(in_path, index=False)

    result = engineer_features(str(in_path), str(out_path))

    assert "petal_length_bin" in result.columns
    assert result["petal_length_bin"].notnull().all()


def test_zero_petal_length_ratio_is_handled(tmp_path):
    df = pd.DataFrame({
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [4.0],
        "petal length (cm)": [0.0],
        "petal width (cm)": [0.0],
        "species": ["setosa"],
    })

    in_path = tmp_path / "in.csv"
    out_path = tmp_path / "out.csv"

    df.to_csv(in_path, index=False)

    result = engineer_features(str(in_path), str(out_path))

    ratio = result.loc[0, "sepal_to_petal_length_ratio"]

    # Verify that zero petal length is handled without division by zero.
    assert pd.isna(ratio)

