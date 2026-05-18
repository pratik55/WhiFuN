- **Key Features:**
  - WHIFUN_FILTER_PREPROC Performs bandpass filtering on functional data. [Subj_list_1, out_func_path] = WHIFUN_FILTER_PREPROC(...) is a high-level function that manages the bandpass filtering step of fMRI preprocessing. Filtering removes unwanted high-frequency physiological noise and low-frequency scanner drift, isolating the BOLD signal of interest. The function performs the following steps: 1. **Check Existence**: It checks if a pre-filtered file already exists. Based on the `over_write` flag, it either skips the process or creates a new file. 2. **Load Data**: It loads the functional data and
  - Internal calls detected: `niftisave`, `whifun_create_file`, `write_error`
  - External dependencies detected: MATLAB NIfTI I/O, Signal Processing Toolbox

## Function: `whifun_filter_preproc()`
- **Functional Purpose:** WHIFUN_FILTER_PREPROC Performs bandpass filtering on functional data. [Subj_list_1, out_func_path] = WHIFUN_FILTER_PREPROC(...) is a high-level function that manages the bandpass filtering step of fMRI preprocessing. Filtering removes unwanted high-frequency physiological noise and low-frequency scanner drift, isolating the BOLD signal of interest. The function performs the following steps: 1. **Check Existence**: It checks if a pre-filtered file already exists. Based on the `over_write` flag, it either skips the process or creates a new file. 2. **Load Data**: It loads the functional data and the brain mask into the workspace. 3. **Design Filter**: It uses the `butter` function to design a
- **Arguments:**
  - `quality_control_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_func_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_lp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_hp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `f_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `log_fileID` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
