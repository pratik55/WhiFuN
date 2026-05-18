- **Key Features:**
  - WHIFUN_CHECK_FUNC_FILE Verifies the existence of a functional data file. [now_func_path, report] = WHIFUN_CHECK_FUNC_FILE(Subj_list_1, comm_sess_name, func_folder_name, func_data_name) searches for a functional neuroimaging data file (`.nii` or `.nii.gz`) for a given subject. It constructs the expected file path and checks if the file exists. The function first tries to find the file using the path stored in the subject structure. If that fails, it tries a common alternative with an added '.nii*' extension. If the file is still not found, it generates a detailed error report, including which p
  - Internal calls detected: `complete_filepath`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_check_func_file()`
- **Functional Purpose:** WHIFUN_CHECK_FUNC_FILE Verifies the existence of a functional data file. [now_func_path, report] = WHIFUN_CHECK_FUNC_FILE(Subj_list_1, comm_sess_name, func_folder_name, func_data_name) searches for a functional neuroimaging data file (`.nii` or `.nii.gz`) for a given subject. It constructs the expected file path and checks if the file exists. The function first tries to find the file using the path stored in the subject structure. If that fails, it tries a common alternative with an added '.nii*' extension. If the file is still not found, it generates a detailed error report, including which part of the path (session folder, functional folder, or the file itself) is missing. This function is
- **Arguments:**
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `comm_sess_name` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_folder_name` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_data_name` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
