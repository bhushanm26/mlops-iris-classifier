
# Testing Strategy

## 1. Overview

This document describes the testing strategy used for the Iris Classification MLOps project.

The main objective is to ensure data quality, correct feature engineering, reliable model training, and acceptable model performance.

The project uses the pytest framework for automated testing.

## 2. Testing Objectives

- Verify preprocessing functionality.
- Test feature engineering calculations.
- Validate input data.
- Test the model training pipeline.
- Verify model prediction outputs.
- Ensure the trained model meets the minimum accuracy requirement.
- Generate test coverage and JUnit reports.

## 3. Testing Framework

The following tools are used:

| Tool | Purpose |
|---|---|
| pytest | Automated testing framework |
| pytest-cov | Code coverage measurement |
| pandas | Data manipulation and validation |
| scikit-learn | Model training and evaluation |
| JUnit XML | Test report generation |

## 4. Unit Testing

### 4.1 Preprocessing Tests

File: `tests/test_preprocess.py`

Test cases:
- Duplicate rows are removed.
- Missing nu

