# whifun_filter_preproc

**Source:** `whifun_functions/whifun_filter_preproc.m:1`

## Signature

```matlab
function [Subj_list_1,out_func_path] = whifun_filter_preproc(quality_control_path,Subj_list_1,in_func_path,in_func_mask_path,filter_lp,filter_hp,f_pre,log_fileID,over_write)
```

## Summary

WHIFUN_FILTER_PREPROC Performs bandpass filtering on functional data.

## Syntax

```matlab
[Subj_list_1, out_func_path] = WHIFUN_FILTER_PREPROC(...) is a high-level
```

## Description

function that manages the bandpass filtering step of fMRI preprocessing. Filtering removes unwanted high-frequency physiological noise and low-frequency scanner drift, isolating the BOLD signal of interest.

The function performs the following steps:

1. **Check Existence**: It checks if a pre-filtered file already exists.
Based on the `over_write` flag, it either skips the process or creates a new file.

2. **Load Data**: It loads the functional data and the brain mask into
the workspace.

3. **Design Filter**: It uses the `butter` function to design a 2nd-order
Butterworth bandpass filter based on the specified low-pass (`filter_lp`) and high-pass (`filter_hp`) cutoffs and the TR of the scan.

4. **Apply Filter**: It applies the filter to the time series of each
voxel within the brain mask using `filtfilt` to avoid phase distortion. The mean signal is added back to the filtered data to preserve its original magnitude.

5. **Save Output**: The filtered data is saved as a new NIfTI file, and
the subject structure is updated. The process output is logged to a file.

In case of an error, the function catches the exception, updates the subject's `error` flag, and logs the detailed error information.

## Input Arguments

### `quality_control_path`
Path to the quality control directory for logs.

### `Subj_list_1`
A single subject structure to be updated.

### `in_func_path`
The path to the input functional file.

### `in_func_mask_path`
The path to the brain mask in functional space.

### `filter_lp`
The low-pass filter cutoff frequency in Hz.

### `filter_hp`
The high-pass filter cutoff frequency in Hz.

### `f_pre`
The prefix for the output filtered file.

### `log_fileID`
File ID of the log file for writing process output.

### `over_write`
A logical value (0 or 1) to force overwriting.

## Output Arguments

### `Subj_list_1`
The updated subject structure, with the `filtered` file path.

### `out_func_path`
The full path to the filtered functional file. See also WHIFUN_CREATE_FILE, BUTTER, FILTFILT, NIFTIREAD, NIFTISAVE, TRY, CATCH.

## Author

Author: Pratik Jain
