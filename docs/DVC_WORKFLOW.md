# DVC Workflow

## 1. DVC Remote

A local DVC remote was configured at:

~/dvc-remote-storage

The command used was:

dvc remote add -d myremote ~/dvc-remote-storage

## 2. Dataset Tracking Workflow

The dataset was tracked using the following workflow:

1. Generate the dataset.
2. Run `dvc add data/raw/iris_v1.csv`
3. Run `git add data/raw/iris_v1.csv.dvc`
4. Commit the DVC metadata using Git.
5. Run `dvc push` to store the dataset in the DVC remote.

## 3. Dataset Versioning

Version 1 contained 150 rows.

Version 2 was created by adding 20 synthetic rows, resulting in 170 rows.

DVC tracked both versions using different MD5 hashes.

## 4. Comparing Versions

Dataset versions were compared using:

dvc diff <commit_hash>

The comparison showed that `data/raw/iris_v1.csv` was modified.

## 5. Restoring Versions

A previous dataset version can be restored using:

git checkout <version_commit> -- data/raw/iris_v1.csv.dvc
dvc checkout data/raw/iris_v1.csv.dvc

This successfully restored Version 1 with 150 rows and Version 2 with 170 rows.

## 6. Reproducibility

Git tracks the DVC metadata files, while DVC manages the actual dataset files. This allows different dataset versions to be restored and used for reproducible machine-learning experiments.