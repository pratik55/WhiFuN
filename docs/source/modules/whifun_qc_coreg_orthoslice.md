# whifun_qc_coreg_orthoslice

**Source:** `whifun_functions/whifun_qc_coreg_orthoslice.m:1`

## Signature

```matlab
function whifun_qc_coreg_orthoslice(image_1_path,image_2_path,out_image_path,caption_1,caption_2)
```

## Summary

WHIFUN_QC_COREG_ORTHOSLICE Creates a quality control image for coregistration.

## Syntax

```matlab
WHIFUN_QC_COREG_ORTHOSLICE(image_1_path, image_2_path, out_image_path, caption_1, caption_2)
```

## Description

generates a quality control image to visually inspect the alignment of two neuroimaging files (e.g., a functional image and an anatomical image) after coregistration.

The function uses SPM's `spm_check_registration_evalc` and `spm_orthviews` to create a plot showing three orthogonal slices of `image_2` with an overlay contour of `image_1`. This visual check is essential for verifying the accuracy of the coregistration step.

The function performs the following steps:

1.  **Input Handling**: It checks if custom captions are provided. If
not, it uses the filenames as default captions.

2.  **Directory Check**: It ensures that the output directory for the
QC image exists, creating it if necessary.

3.  **Visualization**: It calls SPM's plotting functions to display
`image_1` and `image_2` in the SPM Orthviews window. It then adds a contour of `image_1` to `image_2` to show the alignment.

4.  **Export**: The resulting plot is saved as a graphics file (e.g.,
`.png`) using the `exportgraphics` function.

## Input Arguments

### `image_1_path`
The full path to the first image (e.g., anatomical).

### `image_2_path`
The full path to the second image (e.g., coregistered functional).

### `out_image_path`
The full path where the output QC image will be saved.

### `caption_1`
(Optional) A custom caption for the first image.

### `caption_2`
(Optional) A custom caption for the second image. See also SPM_CHECK_REGISTRATION, SPM_ORTHVIEWS, EXPORTGRAPHICS, MKDIR, FILEPARTS.

## Author

Author: Pratik Jain
