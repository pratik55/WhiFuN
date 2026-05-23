# whifun_coreg_qc

**Source:** `whifun_functions/whifun_coreg_qc.m:1`

## Signature

```matlab
function whifun_coreg_qc(name_,now_anat_path,now_func_path,slover_slices,slover_contour_range,slover_view,ss,quality_control_path)
```

## Summary

WHIFUN_COREG_QC Generates automated QC images for Coregistration.

## Syntax

```matlab
SPM (Statistical Parametric Mapping), exportgraphics, whifun_slover.
```

## Description

This function creates two types of visual checks:

1. Orthoslice View: A standard SPM-style three-pane check with contours.
2. Slice View: A detailed multi-slice layout using the 'slover' engine.

## Input Arguments

### `name_`
String. Subject ID or session name.

### `now_anat_path`
Struct. Anatomical file info (from dir()).

### `now_func_path`
Struct. Functional file info (from dir()).

### `slover_slices`
Vector. Indices of slices to display.

### `slover_contour_range`
Vector. Range for contour levels (e.g., [0.5 0.5]).

### `slover_view`
String. 'axial', 'sagittal', or 'coronal'.

### `ss`
Boolean. Space toggle (1 = Subject, 0 = MNI).

### `quality_control_path`
String. Root folder for QC output.

## Author

Author: Pratik Jain
