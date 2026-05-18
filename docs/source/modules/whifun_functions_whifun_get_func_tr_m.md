- **Key Features:**
  - WHIFUN_GET_FUNC_TR Extracts the TR (Repetition Time) from a functional NIfTI file. [Subj_list_1, tr, report] = WHIFUN_GET_FUNC_TR(now_func_path, Subj_list_1) attempts to read the TR from the header of a functional NIfTI file. The TR is a critical parameter for fMRI data analysis. The function uses `niftiinfo` to access the file's metadata. If the TR is successfully retrieved, it is returned and stored in the subject's structure. In case the TR value is not available, the function sets the TR to `NaN` and generates a report message, which is useful for downstream error handling. Input Arguments
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_get_func_TR()`
- **Functional Purpose:** WHIFUN_GET_FUNC_TR Extracts the TR (Repetition Time) from a functional NIfTI file. [Subj_list_1, tr, report] = WHIFUN_GET_FUNC_TR(now_func_path, Subj_list_1) attempts to read the TR from the header of a functional NIfTI file. The TR is a critical parameter for fMRI data analysis. The function uses `niftiinfo` to access the file's metadata. If the TR is successfully retrieved, it is returned and stored in the subject's structure. In case the TR value is not available, the function sets the TR to `NaN` and generates a report message, which is useful for downstream error handling. Input Arguments: now_func_path - A `dir` structure (from a call to `dir`) pointing to the functional NIfTI file. Su
- **Arguments:**
  - `now_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
