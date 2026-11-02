
"""
Tests for model quality and accuracy.
"""

import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Minimum acceptable model accuracy
MIN_ACCURACY = 0.90


def test_model_accuracy_meets_threshold():
    # Load the processed Iris feature dataset
    data_path = Path("data/processed/iris_features.csv")

    assert data_path.exists(), "Iris feature dataset not found"

    df = pd.read_csv(data_path)

    # Target column
    target = "species"

    assert target in df.columns, "Target column 'species' is missing"

    # Separate features and target
    X = df.drop(columns=[target])
    y = df[target]

    # Convert categorical feature columns into numeric columns
    X = pd.get_dummies(X, drop_first=False)

    # Remove any remaining missing values
    X = X.fillna(0)

    # Split dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    # Train the Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(X_train, y_train)

    # Predict test data
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy:.4f}")
    print(f"Minimum Required Accuracy: {MIN_ACCURACY:.2f}")

    # Quality gate
    assert accuracy >= MIN_ACCURACY, (
        f"Model accuracy {accuracy:.4f} is below "
        f"the minimum threshold {MIN_ACCURACY:.2f}"
    )

