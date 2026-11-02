
"""
Smoke tests for the model training pipeline.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier


def create_sample_data():
    X, y = make_classification(
        n_samples=30,
        n_features=4,
        n_informative=3,
        n_redundant=0,
        n_classes=3,
        n_clusters_per_class=1,
        random_state=42,
    )

    return X, y


def test_training_pipeline_smoke():
    X, y = create_sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(X, y)

    predictions = model.predict(X)

    assert predictions.shape == (30,)
    assert len(predictions) == 30


def test_model_predict_proba_shape():
    X, y = create_sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(X, y)

    probabilities = model.predict_proba(X)

    assert probabilities.shape == (30, 3)


def test_model_probabilities_sum_to_one():
    X, y = create_sample_data()

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42,
    )

    model.fit(X, y)

    probabilities = model.predict_proba(X)

    probability_sums = np.sum(probabilities, axis=1)

    assert np.allclose(probability_sums, 1.0)

