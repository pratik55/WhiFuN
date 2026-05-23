# whifun_segment_preproc

**Source:** `whifun_functions/whifun_segment_preproc.m:1`

## Signature

```matlab
function [Subj_list_1,out_def_path,GM_native,WM_native,CSF_native,GM_MNI,WM_MNI,CSF_MNI] = whifun_segment_preproc(quality_control_path,Subj_list_1,in_anat_path,log_fileID,over_write)
```

## Summary

WHIFUN_SEGMENT_PREPROC Orchestrates SPM-based anatomical segmentation.

## Syntax

```matlab
[Subj_list_1, out_def_path] = WHIFUN_SEGMENT_PREPROC(quality_control_path, ..., over_write)
```

## Description

is a high-level function that manages the anatomical segmentation and normalization step using SPM.

This function first checks for and resolves any ambiguity in the input anatomical file. It then checks if the core output (the deformation field file, prefixed with 'y_') already exists. Based on the `over_write` flag, it either skips the segmentation or proceeds by calling the `whifun_segment` function.

After the segmentation job, the function updates the subject structure with the paths to all the generated files, including:

- Bias-corrected anatomical image (`m...`)
- Gray, White, and CSF segments in both native (`c1...`, `c2...`, `c3...`)
and MNI space (`wc1...`, `wc2...`, `wc3...`)

- The deformation field (`y...`)
In case of an error, the function catches the exception, updates the subject's `error` flag, and logs the detailed error information to a file.

## Input Arguments

### `quality_control_path`
Path to the quality control directory for logs.

### `Subj_list_1`
A single subject structure to be updated.

### `in_anat_path`
The path to the input anatomical NIfTI file.

### `log_fileID`
File ID of the log file for writing process output.

### `over_write`
A logical value (0 or 1) to force overwriting.

## Output Arguments

### `Subj_list_1`
The updated subject structure with all new file paths.

### `out_def_path`
The full path to the forward deformation field file. See also WHIFUN_MULTIPLE_FILE_FOUND, WHIFUN_CREATE_FILE, WHIFUN_SEGMENT, TRY, CATCH.

## Author

Author: Pratik Jain
