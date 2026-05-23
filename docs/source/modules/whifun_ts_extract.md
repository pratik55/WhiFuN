# whifun_ts_extract

Source: `whifun_functions/whifun_ts_extract.m:1`

```matlab
function [all_ts,n_gm,n_wm,n_deep_wm,n_csf] = whifun_ts_extract(GM_mask_path,WM_mask_path,deep_WM_mask_path,CSF_mask_path,func_path,over_write,thresh_gm,thresh_wm,thresh_deep_wm,thresh_csf)
```

## MATLAB Help

WHIFUN_TS_EXTRACT Extracts time series from multiple brain tissue masks.

  [all_ts, n_gm, n_wm, n_deep_wm, n_csf] = WHIFUN_TS_EXTRACT(...) extracts
  the time series of all voxels within four predefined brain tissue masks:
  Gray Matter (GM), Superficial White Matter (WM), Deep White Matter (WM),
  and Cerebrospinal Fluid (CSF).

  The function first uses a helper function `whifun_create_mask` to
  generate binary masks for each tissue type at a specified threshold,
  resliced to the functional space. It then reads the functional data and
  extracts the time series for all voxels within each of these masks.

  The function separates the WM time series into superficial and deep
  components, providing more detailed quality control. It returns a
  concatenated matrix of all time series and the number of voxels
  extracted from each mask.

  Input Arguments:
  GM_mask_path      - Path to the Gray Matter segmented file.
  WM_mask_path      - Path to the White Matter segmented file.
  deep_WM_mask_path - Path to the eroded deep White Matter mask.
  CSF_mask_path     - Path to the CSF segmented file.
  func_path         - Path to the functional NIfTI file.
  over_write        - Logical flag to force mask recreation.
  thresh_gm         - (Optional) Threshold for GM mask creation.
  thresh_wm         - (Optional) Threshold for WM mask creation.
  thresh_deep_wm    - (Optional) Threshold for deep WM mask creation.
  thresh_csf        - (Optional) Threshold for CSF mask creation.

  Output Arguments:
  all_ts      - A matrix of all extracted time series (voxels x time points).
  n_gm        - Number of GM voxels.
  n_wm        - Number of superficial WM voxels.
  n_deep_wm   - Number of deep WM voxels.
  n_csf       - Number of CSF voxels.

  Author: Pratik Jain
  See also NIFTIREAD, RESHAPE, WHIFUN_CREATE_MASK, WHIFUN_ERODE.
