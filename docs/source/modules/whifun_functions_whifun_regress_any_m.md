- **Key Features:**
  - WHIFUN_REGRESS_ANY Performs voxel-wise nuisance regression on a 4D NIfTI. FUNC_MASK_PATH = WHIFUN_REGRESS_ANY(IN_FUNC_PATH, IN_ANAT_MASK, ... CONFOUNDS_MATRIX, OUT_FUNC_PATH) reads a functional NIfTI file, removes signals defined in the confounds matrix using linear regression, adds the mean signal back, and saves the result. INPUTS: in_func_path - String. Path to the input 4D functional NIfTI. in_anat_mask - String. Path to the anatomical mask NIfTI. confounds_matrix - Matrix (T x N). Nuisance regressors (e.g., motion parameters, CSF signal) where T matches the number of timepoints. out_func_
  - Internal calls detected: `niftisave`, `whifun_create_rest_mask`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_regress_any()`
- **Functional Purpose:** WHIFUN_REGRESS_ANY Performs voxel-wise nuisance regression on a 4D NIfTI. FUNC_MASK_PATH = WHIFUN_REGRESS_ANY(IN_FUNC_PATH, IN_ANAT_MASK, ... CONFOUNDS_MATRIX, OUT_FUNC_PATH) reads a functional NIfTI file, removes signals defined in the confounds matrix using linear regression, adds the mean signal back, and saves the result. INPUTS: in_func_path - String. Path to the input 4D functional NIfTI. in_anat_mask - String. Path to the anatomical mask NIfTI. confounds_matrix - Matrix (T x N). Nuisance regressors (e.g., motion parameters, CSF signal) where T matches the number of timepoints. out_func_path - String. Path where the regressed NIfTI will be saved. OUTPUTS: func_mask_path - String. Path
- **Arguments:**
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_anat_mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `confounds_matrix` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
