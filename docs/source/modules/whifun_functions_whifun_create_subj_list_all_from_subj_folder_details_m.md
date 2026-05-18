- **Key Features:**
  - WHIFUN_CREATE_SUBJ_LIST_ALL_FROM_SUBJ_LIST_ALL_DETAILS Scans a directory and creates a subject list if the patterns for the data folder is given. Subj_list_all = WHIFUN_CREATE_SUBJ_LIST_ALL(comm_subj_name, ..., anat_data_name) scans the current directory (or a specified pattern) for subject folders and constructs a list of subject data. It assumes a specific directory structure where each subject has folders for a session, and within that, folders for functional and anatomical data. The function returns a structure array where each element corresponds to a subject and includes paths to their d
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_create_Subj_list_all_from_Subj_folder_details()`
- **Functional Purpose:** WHIFUN_CREATE_SUBJ_LIST_ALL_FROM_SUBJ_LIST_ALL_DETAILS Scans a directory and creates a subject list if the patterns for the data folder is given. Subj_list_all = WHIFUN_CREATE_SUBJ_LIST_ALL(comm_subj_name, ..., anat_data_name) scans the current directory (or a specified pattern) for subject folders and constructs a list of subject data. It assumes a specific directory structure where each subject has folders for a session, and within that, folders for functional and anatomical data. The function returns a structure array where each element corresponds to a subject and includes paths to their data files. This function is useful for setting up a batch processing script WhiFuN Input Arguments:
- **Arguments:**
  - `data_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `comm_subj_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `comm_sess_name` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_folder_name` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_data_name` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_folder_name` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_data_name` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
