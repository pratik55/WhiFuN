- **Key Features:**
  - WHIFUN_GET_TS_FROM_MASK Extracts time series data for each subject from voxels defined by a specified NIfTI mask file. [MASK_ANALYSIS_FOLDER_PATH, MASK_SUBJ_TS_FOLDER, MASK_NAME] = WHIFUN_GET_TS_FROM_MASK(OUT_ANALYSIS_PATH, MASK_PATH, SUBJ_LIST, RESAMPLE_MASK, OVER_WRITE, ...) This function prepares an analysis folder structure, optionally resamples the input mask, and then iterates through all subjects to extract the functional time series for the voxels defined by the mask. Input Arguments: OUT_ANALYSIS_PATH - The root directory where all analysis results for the entire study will be stored.
  - Internal calls detected: `reslice_data`, `whifun_create_file`, `whifun_niftiread`, `y_Read`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O

## Function: `whifun_get_ts_from_mask()`
- **Functional Purpose:** WHIFUN_GET_TS_FROM_MASK Extracts time series data for each subject from voxels defined by a specified NIfTI mask file. [MASK_ANALYSIS_FOLDER_PATH, MASK_SUBJ_TS_FOLDER, MASK_NAME] = WHIFUN_GET_TS_FROM_MASK(OUT_ANALYSIS_PATH, MASK_PATH, SUBJ_LIST, RESAMPLE_MASK, OVER_WRITE, ...) This function prepares an analysis folder structure, optionally resamples the input mask, and then iterates through all subjects to extract the functional time series for the voxels defined by the mask. Input Arguments: OUT_ANALYSIS_PATH - The root directory where all analysis results for the entire study will be stored. MASK_PATH - Full path to the NIfTI file used as the mask (e.g., an ROI or atlas). SUBJ_LIST - Struc
- **Arguments:**
  - `out_analysis_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `resample_mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
