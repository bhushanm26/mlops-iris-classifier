# Version Control Workflow — MLOps Iris Classifier

## 1. Overview

This document describes the Git-based version control workflow used for this Machine Learning project, developed as part of MLOps Lab Experiment 2.

* **Repository:** https://github.com/bhushanm26/mlops-iris-classifier
* **Primary language:** Python
* **Maintainer:** Bhushan

## 2. Branching Strategy

| Branch            | Purpose                                                           |
| ----------------- | ----------------------------------------------------------------- |
| `main`            | Stable, always-deployable code                                    |
| `develop`         | Integration branch for day-to-day development                     |
| `feature/<name>`  | Individual features, branched from and merged back into `develop` |
| `conflict-demo-*` | Demonstration branches created for conflict-resolution practice   |

**Rule:** No one commits directly to `main`.

All changes follow this flow:

`feature/* → Pull Request → develop → main`

The `main` branch contains stable code, while `develop` is used for integrating day-to-day development work.

## 3. Commit Convention

Commits follow a short, imperative style with a type prefix:

* `feat:` — Add new functionality
* `fix:` — Correct a bug
* `docs:` — Documentation changes
* `chore:` — Tooling, configuration, or maintenance changes
* `refactor:` — Code restructuring without changing behavior
* `test:` — Adding or fixing tests

Example:

`feat: add classification report to training script`

## 4. Standard Workflow (Feature Development)

```bash
git switch develop
git pull origin develop

git switch -c feature/<short-description>

# Make changes

git add <files>
git commit -m "feat: <description>"

git push -u origin feature/<short-description>

# Open a Pull Request into develop on GitHub

# After review and approval, merge through GitHub

git branch -d feature/<short-description>
git push origin --delete feature/<short-description>
```

Feature branches are used for individual changes and are merged into `develop` through Pull Requests.

## 5. Merge Conflict Resolution Process

1. Attempt the merge/rebase. Git identifies conflicting files.
2. Open the conflicted file.
3. Locate the conflict markers:
   `<<<<<<<`, `=======`, `>>>>>>>`
4. Decide which changes to keep or combine the changes manually.
5. Remove all conflict markers.
6. Save the file.
7. Mark the conflict as resolved:

```bash
git add <file>
```

8. Complete the merge:

```bash
git commit -m "merge: resolve README conflict"
```

9. Test the project:

```bash
python src/train.py
```

10. Push the changes to GitHub.

## 6. .gitignore Policy for ML Artifacts

Large or generated files are excluded from Git and should be tracked separately using tools such as DVC, cloud storage, or Git LFS.

The following are excluded:

* Raw and processed datasets
* Model files such as `.pkl`, `.joblib`, `.h5`, and `.pt`
* Virtual environments such as `.venv/` and `venv/`
* Jupyter notebook checkpoints
* IDE configuration files

This keeps the Git repository clean and avoids storing large generated files directly in Git.

## 7. Pull Request Checklist

Before opening or merging a Pull Request:

* [ ] Code runs without errors using `python src/train.py`
* [ ] No large data or model files are accidentally staged
* [ ] Commit messages follow the commit convention
* [ ] Branch is up to date with `develop`
* [ ] PR description explains what changed and why
* [ ] Changes are reviewed before merging

## 8. Verification Log

| Check                                           | Status      |
| ----------------------------------------------- | ----------- |
| Git version is ≥ 2.30                           | ✅ Completed |
| Repository contains required branches           | ✅ Completed |
| `main`, `develop`, and feature branches created | ✅ Completed |
| Pull Request created and merged                 | ✅ Completed |
| Merge conflict demonstrated and resolved        | ✅ Completed |
| `python src/train.py` runs successfully         | ✅ Completed |
| Version control workflow document created       | ✅ Completed |

## 9. Lessons Learned / Notes

During this experiment, I learned how to use Git for version control of a Machine Learning project. I practiced creating repositories, making commits, creating branches, pushing changes to GitHub, creating Pull Requests, merging branches, and resolving merge conflicts.

I also learned the importance of meaningful commit messages and using `.gitignore` to prevent datasets, trained models, virtual environments, and other generated files from being committed.

The project uses `main` for stable code, `develop` for integration, and `feature/*` branches for individual development tasks. Pull Requests are used to review and merge feature changes.

Git conflict resolution was practiced by creating two branches with different changes to the same README line and manually resolving the conflict.

## 10. Project Repository

**GitHub Repository:**
https://github.com/bhushanm26/mlops-iris-classifier

**Project:** MLOps Iris Classifier
**Language:** Python
**Maintainer:** Bhushan
