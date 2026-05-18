- **Key Features:**
  - LOAD_SUBJECTS_ALL Loads all subjects from a CSV file, with options for new runs. Subj_list_all = LOAD_SUBJECTS_ALL(folder, name) loads all subjects from a CSV file without any filtering. The function reads the CSV file named 'name' from the specified 'folder' and returns the data as a structure array. Subj_list_all = LOAD_SUBJECTS_ALL(folder, name, new_run) allows you to initialize the file for a new data run. - If `new_run` is true (1), the function adds 'error' and 'motion_ex' columns and initializes them to zeros. This is useful for starting a new analysis where you need to track errors and
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB table/file I/O

## Function: `load_subjects_all()`
- **Functional Purpose:** LOAD_SUBJECTS_ALL Loads all subjects from a CSV file, with options for new runs. Subj_list_all = LOAD_SUBJECTS_ALL(folder, name) loads all subjects from a CSV file without any filtering. The function reads the CSV file named 'name' from the specified 'folder' and returns the data as a structure array. Subj_list_all = LOAD_SUBJECTS_ALL(folder, name, new_run) allows you to initialize the file for a new data run. - If `new_run` is true (1), the function adds 'error' and 'motion_ex' columns and initializes them to zeros. This is useful for starting a new analysis where you need to track errors and exclusions. Subj_list_all = LOAD_SUBJECTS_ALL(folder, name, new_run, overwrite) provides an option
- **Arguments:**
  - `folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `new_run` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `overwrite` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
