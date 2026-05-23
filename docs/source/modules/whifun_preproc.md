# whifun_preproc

**Source:** `whifun_functions/whifun_preproc.m:1`

## Signature

```matlab
function Subj_list_1 = whifun_preproc(output_folder, Subj_list_1, varargin)
```

## Summary

WHIFUN_PREPROC Orchestrates a comprehensive fMRI preprocessing pipeline.

## Description

is a master function that executes a sequence of fMRI preprocessing steps on a single subject. This function uses MATLAB's `inputParser` to handle a wide range of optional parameters in a clear and structured way.

The function manages the flow of data through each step, passing the output of one function as the input to the next. It includes checks to skip steps that have already been completed, based on the `over_write` flag. Crucially, it incorporates robust error handling: if any step fails, the function catches the error, logs it to a file, and stops the processing for that subject.

The preprocessing steps include:

1. Unzipping data files.
2. Discarding initial volumes.
3. Realignment (motion correction).
4. Quality control checks for framewise displacement.
5. Segmentation of anatomical data.
6. Skull stripping and anatomical mask creation.
7. Coregistration of functional to anatomical data.
8. Nuisance regression (optional).
9. Filtering (optional).
10. Smoothing (optional, with separate WM/GM option).
11. Normalization to MNI space (optional, can be skipped for DARTEL).

## Input Arguments

### `over_write` (logical)
Force overwriting of existing files. Default: 0.

### `Cut_pre` (string)
Prefix for files after discarding volumes. Default: 'c_'.

### `n_vol_dis` (numeric)
Number of initial volumes to discard. Default: 0.

### `Realign_pre` (string)
Prefix for realigned files. Default: 'r'.

### `max_fd` (numeric)
Maximum FD threshold for QC. Default: 0.5.

### `mean_fd` (numeric)
Mean FD threshold for QC. Default: 0.2.

### `greater_than_20` (numeric)
FD threshold for percentage of excluded volumes. Default: 0.2.

### `skull_pre` (string)
Prefix for skull-stripped files. Default: 'b'.

### `Reg_` (logical)
Flag to perform nuisance regression. Default: 0.

### `CSF_thres` (string)
Threshold for CSF mask creation. Default: '0.95'.

### `pca_for_temp_reg` (logical)
Flag to use PCA for CSF signal. Default: 0.

### `n_pca` (numeric)
Number of PCA components. Default: 5.

### `Reg_pre` (string)
Prefix for regressed files. Default: 'REG_'.

### `motion_reg` (logical)
Flag to include motion regressors. Default: 0.

### `filter_check` (logical)
Flag to perform filtering. Default: 0.

### `f_pre` (string)
Prefix for filtered files. Default: 'f'.

### `filter_lp` (string)
Low-pass filter cutoff frequency. Default: '0.01'.

### `filter_hp` (string)
High-pass filter cutoff frequency. Default: '0.15'.

### `Smooth_` (logical)
Flag to perform smoothing. Default: 0.

### `Smooth_pre` (string)
Prefix for smoothed files. Default: 's'.

### `WM_GM_seperate` (logical)
Flag for separate WM/GM smoothing. Default: 1.

### `smooth_fwhm` (numeric)
FWHM of the smoothing kernel. Default: 4.

### `dartel_` (logical)
Flag to skip normalization (for DARTEL). Default: 0.

### `Norm_pre` (string)
Prefix for normalized files. Default: 'w'.

### `vox` (numeric)
Voxel size for normalized output. Default: 3.

## Examples

```matlab
Subj_list_1 = WHIFUN_PREPROC(quality_control_path, Subj_list_1, varargin)
```
