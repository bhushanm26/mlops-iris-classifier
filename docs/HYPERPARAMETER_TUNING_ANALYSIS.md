# Hyperparameter Tuning Analysis

## 1. Baseline Model

Model:
DecisionTreeClassifier

Cross-validation:
5-fold cross-validation

CV F1 Macro:
0.9663

Test Accuracy:
0.9000

Total Fits:
5

The baseline Decision Tree was used as the reference model for comparing
the tuned Random Forest models.

---

## 2. Grid Search

Model:
RandomForestClassifier

Search Method:
GridSearchCV

Total Combinations:
72

Cross-validation:
5-fold

Total Fits:
360

Best Parameters:

- n_estimators: 50
- max_depth: 3
- min_samples_split: 2
- max_features: sqrt

Best CV F1 Macro:
0.9663

Test Accuracy:
0.9667

Grid Search exhaustively evaluated all 72 combinations in the specified
hyperparameter grid.

---

## 3. Random Search

Model:
RandomForestClassifier

Search Method:
RandomizedSearchCV

Number of Iterations:
30

Cross-validation:
5-fold

Total Fits:
150

Best Parameters:

- n_estimators: 100
- max_depth: 3
- min_samples_split: 6
- max_features: sqrt

Best CV F1 Macro:
0.9663

Test Accuracy:
0.9667

Random Search evaluated 30 selected configurations instead of evaluating
all 72 possible grid combinations.

---

## 4. Comparative Analysis

| Method | Model | CV F1 Macro | Test Accuracy | Total Fits |
|---|---|---:|---:|---:|
| Baseline | Decision Tree | 0.9663 | 0.9000 | 5 |
| Grid Search | Random Forest | 0.9663 | 0.9667 | 360 |
| Random Search | Random Forest | 0.9663 | 0.9667 | 150 |

Both Grid Search and Random Search improved the test accuracy from the
baseline's 0.9000 to 0.9667.

The CV F1 Macro was 0.9663 for the baseline and both tuning approaches.

Grid Search required 360 model fits because it evaluated all 72
hyperparameter combinations using 5-fold cross-validation.

Random Search required only 150 model fits, which is substantially fewer
than Grid Search, while achieving the same CV F1 Macro and test accuracy
in this experiment.

Therefore, Random Search provided the same observed performance as Grid
Search with a lower computational cost.

---

## 5. Conclusion

The experiment demonstrates the use of MLflow, cross-validation, Grid
Search, and Random Search for systematic hyperparameter tuning.

The tuned Random Forest models achieved a test accuracy of 0.9667,
compared with 0.9000 for the baseline Decision Tree.

Random Search was more efficient in this experiment because it achieved
the same observed CV F1 Macro and test accuracy as Grid Search using only
150 fits compared with 360 fits.

The complete tuning process and individual search candidates were
tracked using MLflow for reproducibility and comparison.