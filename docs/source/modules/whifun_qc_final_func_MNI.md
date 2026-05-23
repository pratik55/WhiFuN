# whifun_qc_final_func_MNI

**Source:** `whifun_functions/whifun_qc_final_func_MNI.m:1`

## Signature

```matlab
function whifun_qc_final_func_MNI(out_folder,final_func_MNI,GM_MNI,WM_MNI,CSF_MNI,template_path,motion_txt,name,slover_slices_mni,slover_contour_range_mni,slover_view,over_write)
```

## Summary

WHIFUN_QC_FINAL_FUNC_MNI Generates final quality control figures for normalized data.

## Syntax

```matlab
WHIFUN_QC_FINAL_FUNC_MNI(out_folder, final_func_MNI, GM_MNI, ..., over_write)
```

## Description

creates a suite of visual quality control reports to assess the final preprocessed functional data after it has been normalized to MNI space.

The function performs three main checks:

1.  **Orthoslice Alignment**: It generates an SPM `check_registration`
plot comparing the first volume of the normalized functional image to a standard MNI template.

2.  **SLover Alignment**: It uses `whifun_qc_coreg_slover` to create a
more detailed overlay plot, which provides a clear visualization of the normalized functional data on the MNI template.

3.  **Voxel Time Series**: If motion parameters are available, it generates
a time series plot using `whifun_ts_qc` to show the signal from different tissue types (GM, WM, CSF) and head motion. This confirms that the time series data remains consistent and is not distorted by the normalization process.

This function is a critical final quality control step in the preprocessing pipeline. The `over_write` flag prevents redundant image generation.

## Input Arguments

### `out_folder`
The root directory for saving all QC output.

### `final_func_MNI`
The full path to the final normalized functional file. GM_MNI, WM_MNI, CSF_MNI- Paths to the segmented tissue files in MNI space.

### `template_path`
The full path to the MNI template file.

### `motion_txt`
A matrix or path to a text file of motion parameters.

### `name`
The subject's name.

### `slover_slices_mni`
A vector of slice locations for the SLover plot. slover_contour_range_mni- A two-element vector for the contour range.

### `slover_view`
The view to display slices in (e.g., 'axial').

### `over_write`
A logical value (0 or 1) to force overwriting. See also WHIFUN_CREATE_FILE, WHIFUN_QC_COREG_ORTHOSLICE, WHIFUN_QC_COREG_SLOVER, WHIFUN_TS_QC, MKDIR.

## Author

Author: Pratik Jain
