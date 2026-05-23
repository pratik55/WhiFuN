# whifun_ts_mask_qc

**Source:** `whifun_functions/whifun_ts_mask_qc.m:1`

## Signature

```matlab
function whifun_ts_mask_qc(output_path,GM_mask_path,WM_mask_path,deep_WM_mask_path,CSF_mask_path,func_path,name,slover_slices,slover_contour_range,slover_view)
```

## Summary

WHIFUN_TS_MASK_QC Generates quality control images for tissue masks.

## Syntax

```matlab
WHIFUN_TS_MASK_QC(output_path, GM_mask_path, WM_mask_path, deep_WM_mask_path, CSF_mask_path, func_path, name, slover_slices, slover_contour_range, slover_view)
```

## Description

creates a visual report to assess the quality and alignment of multiple brain tissue masks. This is a crucial step for verifying that the masks used to extract time series data are accurate.

The function generates two types of plots:

1.  **SPM Orthoslice Plot**: A plot showing the functional image as the
underlay, with overlaid contours of the GM, WM, deep WM, and CSF masks. Each tissue type is displayed in a different color (GM-red, WM-green, deep WM-yellow, CSF-blue) for easy visual distinction.

2.  **SLover Plot**: A specialized plot using a helper function `whifun_slover`
to display the four tissue masks simultaneously, providing a clearer visualization of the spatial relationship between the different masks.

The function creates a dedicated output directory for the generated plots and saves the figures as PNG files. This allows for easy inspection and archiving of the quality control process.

## Input Arguments

### `output_path`
The path to the root output directory.

### `GM_mask_path`
The path to the Gray Matter mask file.

### `WM_mask_path`
The path to the White Matter mask file.

### `deep_WM_mask_path`
The path to the eroded deep White Matter mask file.

### `CSF_mask_path`
The path to the CSF mask file.

### `func_path`
The path to the functional NIfTI file (used as a reference).

### `name`
The subject's name.

### `slover_slices`
A vector of slice locations to display.

### `slover_contour_range`
A two-element vector for the contour range.

### `slover_view`
The view to display slices in (e.g., 'axial'). See also MKDIR, SPM_FIGURE, SPM_CHECK_REGISTRATION, SPM_ORTHVIEWS, SPM_VOL, EXPORTGRAPHICS.

## Author

Author: Pratik Jain
