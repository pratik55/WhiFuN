# whifun_create_Subj_list

**Source:** `whifun_functions/whifun_create_Subj_list.m:1`

## Signature

```matlab
function [Subj_list,try_again] = whifun_create_Subj_list(output_folder,data_path,final_func_MNI,GM_MNI,WM_MNI,CSF_MNI,varargin)
```

## Summary

WHIFUN_CREATE_SUBJ_LIST Initializes, generates, and verifies the subject file list for the pipeline.

## Syntax

```matlab
[Subj_list, try_again] = WHIFUN_CREATE_SUBJ_LIST(output_folder, data_path, final_func_MNI, GM_MNI, WM_MNI, CSF_MNI)
[Subj_list, try_again] = WHIFUN_CREATE_SUBJ_LIST(..., 'Param1', Value1, 'Param2', Value2, ...)
```

## Description

validates the local environment paths, aggregates mandatory preprocessing paths, constructs a subject list, saves default pipeline parameters, initializes metadata tracking fields, and exports a 'Subj_list.csv'. Finally, it prompts the user to visually confirm the generated file.

accepts additional optional neuroimaging file templates using Name-Value pairs.

Environment Requirements:

- SPM toolbox must be present in the MATLAB search path (contains 'spm.m').
- Whifun toolbox must be present in the MATLAB search path (contains 'whifun.m').

## Input Arguments

### `output_folder`
String/char path where results and parameters will be saved. Automatically created if it does not exist.

### `data_path`
String/char path to the root directory containing source data.

### `final_func_MNI`
Path/template for the final functional MNI images.

### `GM_MNI`
Path/template for Gray Matter MNI maps.

### `WM_MNI`
Path/template for White Matter MNI maps.

### `CSF_MNI`
Path/template for CSF MNI maps. Optional Name-Value Pair Inputs: 'motion_txt'
- Path/template for motion parameters text files. 'anat_mask_MNI'
- Path/template for anatomical MNI brain masks. 'func_MNI'
- Path/template for intermediate functional MNI images. 'anat_MNI'
- Path/template for anatomical T1 MNI images. 'func_mask_MNI'
- Path/template for functional MNI masks. 'MNI_template'
- Path/template for the targeted MNI template.

## Output Arguments

### `Subj_list`
A structure array containing subject paths and initialized exclusion metrics ('error', 'manual_ex', 'motion_ex').

### `try_again`
Numeric flag indicating the user's validation choice: 0 = User accepted the CSV; safe to proceed. 1 = User rejected the CSV; loop or try generation again.

## Examples

Example: [subList, redo] = whifun_create_Subj_list('C:\Study\Output', 'C:\Study\Data', ... 'wfunc*.nii', 'wc1*.nii', 'wc2*.nii', 'wc3*.nii', ... 'motion_txt', 'rp_*.txt');

## Author

Author: Pratik Jain
