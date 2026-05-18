- **Key Features:**
  - WHIFUN_GET_AVG_TS Extracts the average time series for each region in a given ROI atlas. AVG_TS_PATH = WHIFUN_GET_AVG_TS(OUT_FOLDER, ROI_PATH, SUBJ_LIST, FIELD, BAND_INFO, QC_PLOTS, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS) This function reads functional MRI data for a list of subjects, resamples the specified Atlas (ROI), and extracts the mean BOLD time series for every non-zero region defined in the Atlas. It also handles optional bandpass filtering and checks for regions with missing functional data. Input Arguments: OUT_FOLDER - Main output directory for saving results and QC plots. ROI_PA
  - Internal calls detected: `functional_connectivity`, `niftisave`, `whifun_create_file`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Signal Processing Toolbox, SPM12, ANTs command-line suite

## Function: `whifun_create_avg_ts()`
- **Functional Purpose:** WHIFUN_GET_AVG_TS Extracts the average time series for each region in a given ROI atlas. AVG_TS_PATH = WHIFUN_GET_AVG_TS(OUT_FOLDER, ROI_PATH, SUBJ_LIST, FIELD, BAND_INFO, QC_PLOTS, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS) This function reads functional MRI data for a list of subjects, resamples the specified Atlas (ROI), and extracts the mean BOLD time series for every non-zero region defined in the Atlas. It also handles optional bandpass filtering and checks for regions with missing functional data. Input Arguments: OUT_FOLDER - Main output directory for saving results and QC plots. ROI_PATH - Full path to the NIfTI file defining the ROI atlas. SUBJ_LIST - (can be created with whifun_cre
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ROI_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `field` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `band_info` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `QC_plots` (numeric time-series matrix, commonly T x R, V x T, or T x R x S): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
