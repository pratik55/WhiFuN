- **Key Features:**
  - WHIFUN_PARTIAL_CORR Computes the partial correlation between the time series of voxels in a target mask and the average time series of a set of functional networks (FNs), controlling for all other FNs. PCOR_TS_PATH = WHIFUN_PARTIAL_CORR(WM_OR_GM, MASK_SUBJ_TS_FOLDER, AVG_TS_PATH, FR_MASK_PATH, SUBJ_LIST, K, OVER_WRITE, D_FLAG, D, STEPS, TOT_STEPS) This function calculates the individual-level partial correlation maps (Fisher-z transformed) between every voxel's time series in the target `fr_mask` and each of the K functional networks (WM-FN or GM-FN), while regressing out the influence of the 
  - Internal calls detected: `whifun_create_file`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox, ANTs command-line suite

## Function: `whifun_partial_corr()`
- **Functional Purpose:** WHIFUN_PARTIAL_CORR Computes the partial correlation between the time series of voxels in a target mask and the average time series of a set of functional networks (FNs), controlling for all other FNs. PCOR_TS_PATH = WHIFUN_PARTIAL_CORR(WM_OR_GM, MASK_SUBJ_TS_FOLDER, AVG_TS_PATH, FR_MASK_PATH, SUBJ_LIST, K, OVER_WRITE, D_FLAG, D, STEPS, TOT_STEPS) This function calculates the individual-level partial correlation maps (Fisher-z transformed) between every voxel's time series in the target `fr_mask` and each of the K functional networks (WM-FN or GM-FN), while regressing out the influence of the other K-1 networks. Input Arguments: WM_OR_GM - String indicating the network type (e.g., 'WM' or 'G
- **Arguments:**
  - `WM_or_GM` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_subj_ts_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `avg_ts_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `fr_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `K` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
