- **Key Features:**
  - WHIFUN_TS_QC Generates a quality control figure for time series and motion. WHIFUN_TS_QC(GM_mask_path, WM_mask_path, CSF_mask_path, func_path, motion_txt_path, num_erosions, Par_name, over_write, f) creates a comprehensive figure for a single subject, visualizing the time series of key brain tissues alongside framewise displacement (FD). The function first creates a "deep White Matter (WM)" mask by eroding the standard WM mask, which helps to isolate a signal that is less likely to contain a gray matter component. It then extracts the time series from the Gray Matter (GM), Superficial White Ma
  - Internal calls detected: `whifun_calculate_fd`, `whifun_erode`, `whifun_ts_extract`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_ts_qc()`
- **Functional Purpose:** WHIFUN_TS_QC Generates a quality control figure for time series and motion. WHIFUN_TS_QC(GM_mask_path, WM_mask_path, CSF_mask_path, func_path, motion_txt_path, num_erosions, Par_name, over_write, f) creates a comprehensive figure for a single subject, visualizing the time series of key brain tissues alongside framewise displacement (FD). The function first creates a "deep White Matter (WM)" mask by eroding the standard WM mask, which helps to isolate a signal that is less likely to contain a gray matter component. It then extracts the time series from the Gray Matter (GM), Superficial White Matter (WM), Deep White Matter, and Cerebrospinal Fluid (CSF) using a helper function. The generated f
- **Arguments:**
  - `GM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `motion_txt_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `num_erosions` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Par_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `f` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `create_mask()`
- **Functional Purpose:** WHIFUN_TS_QC Generates a quality control figure for time series and motion. WHIFUN_TS_QC(GM_mask_path, WM_mask_path, CSF_mask_path, func_path, motion_txt_path, num_erosions, Par_name, over_write, f) creates a comprehensive figure for a single subject, visualizing the time series of key brain tissues alongside framewise displacement (FD). The function first creates a "deep White Matter (WM)" mask by eroding the standard WM mask, which helps to isolate a signal that is less likely to contain a gray matter component. It then extracts the time series from the Gray Matter (GM), Superficial White Ma
- **Arguments:**
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_name` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
