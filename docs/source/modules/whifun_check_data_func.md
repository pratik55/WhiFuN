# whifun_check_data_func

**Source:** `whifun_functions/whifun_check_data_func.m:1`

## Signature

```matlab
function [Subj_list_1,voxel_func,n_image,tr,no_func,report] = whifun_check_data_func(Subj_list_1,comm_sess_name,func_folder_name,func_data_name,output_folder,report)
```

## Summary

WHIFUN_CHECK_DATA_FUNC Checks for functional data and extracts its properties.

## Syntax

```matlab
[Subj_list_1, voxel_func, n_image, tr, no_func, report] = WHIFUN_CHECK_DATA_FUNC(...)
```

## Description

is a high-level function that orchestrates the process of finding a subject's functional neuroimaging data file, resolving potential ambiguities, and extracting key parameters like voxel size, number of volumes, and TR.

The function first calls `whifun_check_func_file` to find the file. If multiple files are found, it sorts them by creation date and selects the oldest one. It then calls `whifun_get_func_info` and `whifun_get_func_TR` to extract the metadata.

If no functional data file is found, the function sets a flag (`no_func`) to 1, sets the subject's `error` flag to 1, and initializes all output parameters to `NaN`. This allows a calling script to gracefully handle missing data.

## Input Arguments

### `Subj_list_1`
A single subject structure.

### `comm_sess_name`
The common session folder name (e.g., 'ses-01').

### `func_folder_name`
The name of the functional data subfolder (e.g., 'func').

### `func_data_name`
The base name of the functional data file (e.g., 'task-rest_bold').

### `report`
(Optional) A string array for accumulating report messages.

## Output Arguments

### `Subj_list_1`
The updated subject structure with functional file info.

### `voxel_func`
A 1x3 array of the functional data's voxel dimensions, or NaN.

### `n_image`
The number of images (time points), or NaN.

### `tr`
The repetition time (TR), or NaN.

### `no_func`
A flag: 0 if data found, 1 if not.

### `report`
A string array with any warning or error messages. See also WHIFUN_CHECK_FUNC_FILE, WHIFUN_GET_FUNC_INFO, WHIFUN_GET_FUNC_TR.

## Author

Author: Pratik Jain
