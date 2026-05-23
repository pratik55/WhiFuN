# whifun_check_func_file

**Source:** `whifun_functions/whifun_check_func_file.m:1`

## Signature

```matlab
function [now_func_path,report] = whifun_check_func_file(Subj_list_1,comm_sess_name,func_folder_name,func_data_name)
```

## Summary

WHIFUN_CHECK_FUNC_FILE Verifies the existence of a functional data file.

## Syntax

```matlab
[now_func_path, report] = WHIFUN_CHECK_FUNC_FILE(Subj_list_1, comm_sess_name, func_folder_name, func_data_name)
```

## Description

searches for a functional neuroimaging data file (`.nii` or `.nii.gz`) for a given subject. It constructs the expected file path and checks if the file exists.

The function first tries to find the file using the path stored in the subject structure. If that fails, it tries a common alternative with an added '.nii*' extension. If the file is still not found, it generates a detailed error report, including which part of the path (session folder, functional folder, or the file itself) is missing.

This function is critical for robust preprocessing pipelines, ensuring that the data for each subject is in the expected location before processing begins.

## Input Arguments

### `Subj_list_1`
A single subject structure, which must contain `func_folder` and `func_name` fields.

### `comm_sess_name`
The common session folder name (e.g., 'ses-01').

### `func_folder_name`
The name of the functional data subfolder (e.g., 'func').

### `func_data_name`
The base name of the functional data file (e.g., 'task-rest_bold').

## Output Arguments

### `now_func_path`
A `dir` structure if the file is found, otherwise empty.

### `report`
A string containing an error message if the file is not found, otherwise an empty string. See also DIR, FULLFILE, ISEMPTY, ISFOLDER, STRCHR.

## Author

Author: Pratik Jain
