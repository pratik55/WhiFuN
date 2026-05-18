- **Key Features:**
  - WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. Th
  - Internal calls detected: `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, SPM12, Shell/system execution

## Function: `whifun_ts_extract()`
- **Functional Purpose:** WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. The function separates the WM time series into superficial and deep components, providing more detaile
- **Arguments:**
  - `GM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `deep_WM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_gm` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_wm` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_deep_wm` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_csf` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `whifun_create_mask()`
- **Functional Purpose:** WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. Th
- **Arguments:**
  - `mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_name` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `extract_ts()`
- **Functional Purpose:** WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. Th
- **Arguments:**
  - `func_image` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `extract_ts_wm()`
- **Functional Purpose:** WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. Th
- **Arguments:**
  - `func_image` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `wm_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `deep_wm_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `create_mask()`
- **Functional Purpose:** WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks. [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts the time series of all voxels within four predefined brain tissue masks: Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM), and Cerebrospinal Fluid (CSF). The function first uses a helper function `whifun_create_mask` to generate binary masks for each tissue type at a specified threshold, resliced to the functional space. It then reads the functional data and extracts the time series for all voxels within each of these masks. Th
- **Arguments:**
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask_name` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh_` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
