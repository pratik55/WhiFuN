- **Key Features:**
  - WHIFUN_QC_FILTER Generates quality control figures for the filtering step. WHIFUN_QC_FILTER(out_folder, Subj_list_1, over_write, filter_freq_response_flag, filter_lp, filter_hp) creates visual quality control reports to assess the effectiveness of the bandpass filtering applied to functional data. The function performs the following steps: 1. **Check Existence**: It checks if the output plots already exist and, based on the `over_write` flag, either skips or generates new ones. The output includes up to two figures. 2. **Global Time Series Plot**: It plots the mean global time series of the fu
  - Internal calls detected: `whifun_create_file`, `whifun_plot_freqz`
  - External dependencies detected: MATLAB NIfTI I/O, Signal Processing Toolbox

## Function: `whifun_qc_filter()`
- **Functional Purpose:** WHIFUN_QC_FILTER Generates quality control figures for the filtering step. WHIFUN_QC_FILTER(out_folder, Subj_list_1, over_write, filter_freq_response_flag, filter_lp, filter_hp) creates visual quality control reports to assess the effectiveness of the bandpass filtering applied to functional data. The function performs the following steps: 1. **Check Existence**: It checks if the output plots already exist and, based on the `over_write` flag, either skips or generates new ones. The output includes up to two figures. 2. **Global Time Series Plot**: It plots the mean global time series of the functional data *before* and *after* filtering. The global mean is calculated across all voxels at eac
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_freq_response_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_lp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_hp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
