# whifun_qc_nuisance_regression_vox_ts

**Source:** `whifun_functions/whifun_qc_nuisance_regression_vox_ts.m:1`

## Signature

```matlab
function whifun_qc_nuisance_regression_vox_ts(out_folder1,Subj_list_1,slover_slices_ss,slover_contour_range_ss,slover_view,over_write)
```

## Summary

WHIFUN_QC_NUISANCE_REGRESSION_VOX_TS Generates quality control figures for nuisance regression.

## Syntax

```matlab
WHIFUN_QC_NUISANCE_REGRESSION_VOX_TS(out_folder1, Subj_list_1, ...)
```

## Description

creates visual quality control reports to assess the effectiveness of nuisance regression. The function focuses on time series plots and mask visualizations.

The function performs the following steps:

1.  **Check Existence**: It checks if the before- and after-regression
time series plots already exist and, based on the `over_write` flag, either skips or generates new ones. It also creates the necessary output directories.

2.  **Time Series Plots**: It calls a helper function `whifun_ts_qc` to
generate time series plots of key brain regions (GM, WM, CSF) and motion parameters. It generates two separate plots: one for the data *before* regression and one for the data *after* regression. This allows for a direct comparison to see the effect of the regression.

3.  **Mask Visualization**: It calls `whifun_ts_mask_qc` to generate a
figure that visualizes the GM, WM, CSF, and deep WM masks used for time series extraction. This is important for verifying that the masks used for time series extraction are accurate.

This function is essential for verifying that nuisance regression has effectively removed unwanted signals without affecting the regions of interest.

## Input Arguments

### `out_folder1`
The root directory for saving all QC output.

### `Subj_list_1`
A single subject structure with necessary fields like `realigned`, `nuisance_regressed`, and mask paths.

### `slover_slices_ss`
A vector of slice locations for the SLover plot. slover_contour_range_ss- A two-element vector for the contour range.

### `slover_view`
The view to display slices in (e.g., 'axial').

### `over_write`
A logical value (0 or 1) to force overwriting. See also WHIFUN_CREATE_FILE, WHIFUN_TS_QC, WHIFUN_TS_MASK_QC, MKDIR.

## Author

Author: Pratik Jain
