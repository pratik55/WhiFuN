- **Key Features:**
  - WHIFUN_QC_GLOBAL_TS Generates a quality control figure for global time series. WHIFUN_QC_GLOBAL_TS(out_folder, initial_func, final_func_MNI, motion_txt, func_mask_MNI, name, Reg_, over_write, csf_covariate_path, n_pca, pca_for_temp_reg) creates a visual report to assess the quality of the mean global time series of a subject's functional data. The function plots the mean time series of the original and normalized data, as well as the head motion. The function first checks if the output plot already exists and, based on the `over_write` flag, either skips or generates a new one. It then calls a
  - Internal calls detected: `whifun_create_file`, `whifun_ts_check`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_qc_global_ts()`
- **Functional Purpose:** WHIFUN_QC_GLOBAL_TS Generates a quality control figure for global time series. WHIFUN_QC_GLOBAL_TS(out_folder, initial_func, final_func_MNI, motion_txt, func_mask_MNI, name, Reg_, over_write, csf_covariate_path, n_pca, pca_for_temp_reg) creates a visual report to assess the quality of the mean global time series of a subject's functional data. The function plots the mean time series of the original and normalized data, as well as the head motion. The function first checks if the output plot already exists and, based on the `over_write` flag, either skips or generates a new one. It then calls a helper function, `whifun_ts_check` (which is not provided in this file, but is assumed to handle th
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `initial_func` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `final_func_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `motion_txt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_mask_MNI` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Reg_` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `csf_covariate_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_pca` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `pca_for_temp_reg` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
