- **Key Features:**
  - LOAD_SUBJECTS Loads a list of subjects from a CSV file. [Subj_list, rm] = LOAD_SUBJECTS(folder, name) loads a CSV file named 'name' from the specified 'folder'. It returns a structure array 'Subj_list' containing the subject data and a logical array 'rm' indicating which rows were removed. The function automatically removes subjects marked with 'error', 'motion_ex', or 'manual_ex'. [Subj_list, rm] = LOAD_SUBJECTS(folder, name, first) allows for different behavior on the first run. If 'first' is true (1), the function initializes new 'error' and 'motion_ex' columns with zeros and only removes s
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB table/file I/O

## Function: `load_subjects()`
- **Functional Purpose:** LOAD_SUBJECTS Loads a list of subjects from a CSV file. [Subj_list, rm] = LOAD_SUBJECTS(folder, name) loads a CSV file named 'name' from the specified 'folder'. It returns a structure array 'Subj_list' containing the subject data and a logical array 'rm' indicating which rows were removed. The function automatically removes subjects marked with 'error', 'motion_ex', or 'manual_ex'. [Subj_list, rm] = LOAD_SUBJECTS(folder, name, first) allows for different behavior on the first run. If 'first' is true (1), the function initializes new 'error' and 'motion_ex' columns with zeros and only removes subjects marked with 'manual_ex'. This is useful for initial data processing runs. Input Arguments: f
- **Arguments:**
  - `folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `first` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
