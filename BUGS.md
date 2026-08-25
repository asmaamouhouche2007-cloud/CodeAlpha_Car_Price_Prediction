# 🐛 Bug Reports & Fixes

This file documents the development issues encountered during the creation of this project, along with their solutions. It serves as a reference for future maintenance and an honest log of the debugging process.

---

## [Version 1.0.0] - [Date: 2026-08-22]

### 🚨 Critical Bugs

- **Bug 1: `ModuleNotFoundError: No module named 'src'`**
  - **Problem:** Running `python src/train.py` failed because Python couldn't find the `src` package.
  - **Root Cause:** The file was run directly from inside the `src` folder, preventing Python from finding the parent directory.
  - **Solution:** Added `sys.path.append()` to the top of `train.py`, or switched to running `python -m src.train` from the root folder.
  - **Lesson Learned:** Use `python -m package.module` for structured projects to avoid path issues.

- **Bug 2: `ValueError: If using all scalar values, you must pass an index`**
  - **Problem:** Creating a DataFrame from a single dictionary in `app.py` crashed.
  - **Root Cause:** Pandas requires an explicit index for single-row DataFrames.
  - **Solution:** Added `index=[0]` to `pd.DataFrame([new_car], index=[0])`.
  - **Lesson Learned:** Always add `index=[0]` when creating single-row DataFrames from dictionaries.

- **Bug 3: `ValueError: The feature names should match those that were passed during fit`**
  - **Problem:** Predicting on new data crashed because One-Hot Encoded columns from training were missing.
  - **Root Cause:** Pandas `get_dummies()` only creates columns for categories present in the new data, not the original training data.
  - **Solution:** Used `to_predict.reindex(columns=model.feature_names_in_, fill_value=0)` to force the new data to match the model's expected columns.
  - **Lesson Learned:** Always reindex your prediction DataFrame to match `model.feature_names_in_`.
  - **Problem:** The table prefiction_logs did not get created properly
  - **Root Cause:** using drop the table if it exist instead of creat the table if it does not exist
  in the schema table.
  - **Solution:** creating the table if it does not exist .
  - **Lesson Learned:** Always reindex your prediction DataFrame to match `model.feature_names_in_`.


