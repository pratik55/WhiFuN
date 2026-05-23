# whifun_smooth_together

**Source:** `whifun_functions/whifun_smooth_together.m:1`

## Signature

```matlab
function output = whifun_smooth_together(nt,now_func_path,smooth_fwhm,Smooth_pre)
```

## Summary

WHIFUN_SMOOTH_TOGETHER Performs spatial smoothing on a 4D fMRI volume using SPM's

## Syntax

```matlab
OUTPUT = WHIFUN_SMOOTH_TOGETHER(NT, NOW_FUNC_PATH, SMOOTH_FWHM, SMOOTH_PRE)
```

## Description

'smooth' module.

This function sets up and runs an SPM job to apply a Gaussian smoothing kernel to all individual volumes (time points) of a 4D NIfTI file. It prepares the job to run non-interactively and captures the SPM output.

## Input Arguments

### `NT`
The total number of time points (volumes) in the functional image.

### `NOW_FUNC_PATH`
A structure (e.g., from `dir` or `fileparts`) or string containing the path information for the 4D functional NIfTI file. It must contain the folder and file name for the 4D image.

### `SMOOTH_FWHM`
The Full-Width at Half-Maximum (FWHM) of the Gaussian kernel in millimeters (e.g., 6). This is applied equally in the X, Y, and Z dimensions.

### `SMOOTH_PRE`
The prefix (e.g., 's') to be added to the output smoothed image file name (e.g., 'r_data.nii' becomes 'sr_data.nii').

## Output Arguments

### `OUTPUT`
A character array containing the text output captured from the SPM job execution (useful for logging/debugging).

## Requirements

MATLAB's 'spm' functions (`spm_jobman`, `spm_defaults`, etc.).

## Author

Author: Pratik Jain
