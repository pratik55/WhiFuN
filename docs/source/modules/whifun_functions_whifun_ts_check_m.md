- **Key Features:**
  - WHIFUN_TS_CHECK Generates a comprehensive time series quality check figure. WHIFUN_TS_CHECK(func_path_raw, func_path_pro, txt_path, in_anat_mni_mask_path, out_func_mni_mask_path, out_image_path, Reg_, csf_covariate_path, n_pca, pca_for_temp_reg) creates a multi-panel figure to visually inspect the effect of the preprocessing pipeline on a subject's functional time series. The function provides a detailed comparison of data quality before and after key preprocessing steps. The function generates ten plots in a 2x5 grid: - **Global Mean (Raw)**: The mean signal of the raw data. - **Pairwise Vari
  - Internal calls detected: `whifun_calculate_fd`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_ts_check()`
- **Functional Purpose:** WHIFUN_TS_CHECK Generates a comprehensive time series quality check figure. WHIFUN_TS_CHECK(func_path_raw, func_path_pro, txt_path, in_anat_mni_mask_path, out_func_mni_mask_path, out_image_path, Reg_, csf_covariate_path, n_pca, pca_for_temp_reg) creates a multi-panel figure to visually inspect the effect of the preprocessing pipeline on a subject's functional time series. The function provides a detailed comparison of data quality before and after key preprocessing steps. The function generates ten plots in a 2x5 grid: - **Global Mean (Raw)**: The mean signal of the raw data. - **Pairwise Variance (Raw)**: A measure of signal change between time points. - **Rigid Body Motion**: The 6 head mo
- **Arguments:**
  - `func_path_raw` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path_pro` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `txt_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_func_mni_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Reg_` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `csf_covariate_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_pca` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `pca_for_temp_reg` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `create_mask()`
- **Functional Purpose:** WHIFUN_TS_CHECK Generates a comprehensive time series quality check figure. WHIFUN_TS_CHECK(func_path_raw, func_path_pro, txt_path, in_anat_mni_mask_path, out_func_mni_mask_path, out_image_path, Reg_, csf_covariate_path, n_pca, pca_for_temp_reg) creates a multi-panel figure to visually inspect the effect of the preprocessing pipeline on a subject's functional time series. The function provides a detailed comparison of data quality before and after key preprocessing steps. The function generates ten plots in a 2x5 grid: - **Global Mean (Raw)**: The mean signal of the raw data. - **Pairwise Vari
- **Arguments:**
  - `n` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
