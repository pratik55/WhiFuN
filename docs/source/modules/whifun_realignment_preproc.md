# whifun_realignment_preproc

**Source:** `whifun_functions/whifun_realignment_preproc.m:1`

## Signature

```matlab
function [Subj_list_1,out_func_path,out_motion_txt_path] = whifun_realignment_preproc(quality_control_path,Subj_list_1,in_func_path,Realign_pre,log_fileID, over_write)
```

## Summary

WHIFUN_REALIGNMENT_PREPROC Performs motion correction (realignment) on functional data.

## Syntax

```matlab
[Subj_list_1, out_func_path, out_motion_txt_path] = WHIFUN_REALIGNMENT_PREPROC(...)
```

## Description

is a high-level function that orchestrates the realignment step of fMRI preprocessing. Realignment corrects for head motion that occurs during a scan.

The function first checks for and resolves multiple input files. It then determines the output file path and, based on the `over_write` flag, decides whether to perform the realignment or skip it if the output file already exists. It calls a sub-function `whifun_realignment` to execute the SPM-based realignment. The function updates the subject structure with the paths to the realigned file and the motion parameters file. All process output is logged to a specified file.

In case of an error, the function catches the exception, updates the subject's error flag, and logs the detailed error information.

## Input Arguments

### `quality_control_path`
Path to the quality control directory for logs.

### `Subj_list_1`
A single subject structure to be updated.

### `in_func_path`
The path to the input functional NIfTI file.

### `Realign_pre`
The prefix to use for the output realigned file.

### `log_fileID`
File ID of the log file for writing process output.

### `over_write`
(Optional) A logical value (0 or 1) to force overwriting the output files. Defaults to 0.

## Output Arguments

### `Subj_list_1`
The updated subject structure with `realigned` and `motion_txt` fields.

### `out_func_path`
The full path to the realigned functional file.

### `out_motion_txt_path`
The full path to the motion parameter `.txt` file. See also WHIFUN_MULTIPLE_FILE_FOUND, WHIFUN_CREATE_FILE, WHIFUN_REALIGNMENT, TRY, CATCH.

## Author

Author: Pratik Jain
