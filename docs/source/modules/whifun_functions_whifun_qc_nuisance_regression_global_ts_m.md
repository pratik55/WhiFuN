- **Key Features:**
  - WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS Generates a global time series QC plot for nuisance regression. WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS(...) creates a visual quality control report to assess the effect of nuisance regression on the mean global signal of a functional scan. The function performs the following steps: 1. **Check Existence**: It checks if the output plot already exists and, based on the `over_write` flag, either skips or generates a new one. 2. **Data Loading**: It reads the functional data before and after nuisance regression. It also loads the motion parameters and the CS
  - Internal calls detected: `whifun_create_file`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_qc_nuisance_regression_global_ts()`
- **Functional Purpose:** WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS Generates a global time series QC plot for nuisance regression. WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS(...) creates a visual quality control report to assess the effect of nuisance regression on the mean global signal of a functional scan. The function performs the following steps: 1. **Check Existence**: It checks if the output plot already exists and, based on the `over_write` flag, either skips or generates a new one. 2. **Data Loading**: It reads the functional data before and after nuisance regression. It also loads the motion parameters and the CSF covariates (either PCA components or the mean time series). 3. **Plotting**: It creates a single p
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `REG_CSF` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `motion_reg` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `pca_for_temp_reg` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_pca` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
