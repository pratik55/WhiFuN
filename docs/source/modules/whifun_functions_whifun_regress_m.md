- **Key Features:**
  - WHIFUN_REGRESS Performs nuisance regression on functional data. func_mask_path = WHIFUN_REGRESS(in_func_path, ..., n_pca) performs nuisance regression on a functional neuroimaging time series. This process removes signals from non-neuronal sources, such as head motion and physiological noise. The function first loads the functional data and creates a brain mask by reslicing an anatomical mask into functional space. It then constructs a design matrix (`b_init`) of nuisance regressors, which can include: - **CSF Signal**: Loaded from `in_csf_mat_path`. The signal can be either the mean CSF time 
  - Internal calls detected: `niftisave`, `whifun_create_rest_mask`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_regress()`
- **Functional Purpose:** WHIFUN_REGRESS Performs nuisance regression on functional data. func_mask_path = WHIFUN_REGRESS(in_func_path, ..., n_pca) performs nuisance regression on a functional neuroimaging time series. This process removes signals from non-neuronal sources, such as head motion and physiological noise. The function first loads the functional data and creates a brain mask by reslicing an anatomical mask into functional space. It then constructs a design matrix (`b_init`) of nuisance regressors, which can include: - **CSF Signal**: Loaded from `in_csf_mat_path`. The signal can be either the mean CSF time series or a set of PCA components. - **Motion Parameters**: Loaded from `in_motion_txt_path`. If `mo
- **Arguments:**
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_anat_mask_subj_space_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_csf_mat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_motion_txt_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_pca` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
