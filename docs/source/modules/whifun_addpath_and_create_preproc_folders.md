# whifun_addpath_and_create_preproc_folders

**Source:** `whifun_functions/whifun_addpath_and_create_preproc_folders.m:1`

## Signature

```matlab
function quality_control_path = whifun_addpath_and_create_preproc_folders(preproc_code_path,output_folder)
```

## Summary

WHIFUN_ADDPATH_AND_CREATE_PREPROC_FOLDERS Sets up paths and output directories for preprocessing.

## Description

adds necessary code directories to the MATLAB path and creates a standardized set of output folders for storing preprocessing results, quality control metrics, and logs.

The function first adds the main preprocessing code path and a subfolder of utility functions to the MATLAB path. It then checks if SPM is available on the path, as it is a critical dependency for most neuroimaging preprocessing pipelines. If SPM is not found, a message box is displayed to the user.

Finally, the function creates a set of subdirectories within the specified `output_folder` to organize the results of the preprocessing workflow.

## Input Arguments

### `preproc_code_path`
The full path to the directory containing the main preprocessing scripts.

### `output_folder`
The full path to the main directory where all preprocessing output will be stored.

## Output Arguments

### `quality_control_path`
The full path to the newly created 'Quality_control' directory. This path can be used by subsequent functions to save output. Created Directories:
- <output_folder>/Quality_control/b_Head_motion
- <output_folder>/Quality_control/Error_Info
- <output_folder>/Quality_control/logs

## Examples

Example: preproc_path = 'C:\Users\User\my_preproc_code'; output_path = 'D:\project_data\preprocessed_output'; qc_path = whifun_addpath_and_create_preproc_folders(preproc_path, output_path); % The 'qc_path' variable now contains the full path to the 'Quality_control' folder.

See also ADDPATH, FULLFILE, WHICH, MKDIR, MSGBOX.

```matlab
quality_control_path = WHIFUN_ADDPATH_AND_CREATE_PREPROC_FOLDERS(preproc_code_path, output_folder)
```

## Author

Author: Pratik Jain
