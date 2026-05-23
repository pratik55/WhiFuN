# whifun_create_fields_preproc

**Source:** `whifun_functions/whifun_create_fields_preproc.m:1`

## Signature

```matlab
function Subj_list_all = whifun_create_fields_preproc(Subj_list_all)
```

## Summary

WHIFUN_CREATE_FIELDS_PREPROC Adds preprocessing-specific fields to a subject list.

## Description

function that ensures a subject list structure array contains all the necessary fields for tracking files and data generated during a neuroimaging preprocessing pipeline.

This function calls an internal helper function `create_field` for a comprehensive list of fields. If a field does not exist in the structure, it is added to the first element of the array with an empty value. This pre-allocation is a robust way to prepare a subject list for subsequent data storage without throwing errors.

The fields added by this function include:

- **File paths**: `nii_func`, `nii_anat`, `motion_txt`
`initial_vol_cut`, `realigned`, `bias_corrected`, `skull_stripped`, `coregistered_func`, `nuisance_regressed`, `filtered`, `smoothed`, `func_MNI`, `anat_MNI`

- **Segmentation and masks** paths: `GM_native`, `WM_native`, `CSF_native`,
`GM_MNI`, `WM_MNI`, `CSF_MNI`, `deformation_field`, `anat_mask_native`, `anat_mask_MNI`, `CSF_mask_func`

## Input Arguments

### `Subj_list_all`
A structure array containing subject data.

## Output Arguments

### `Subj_list_all`
The same structure array, with any missing fields from the predefined list added.

## Examples

Example: % Assuming a subject list `Subj_list` is loaded from a Subj_list CSV file.

% This function will add all the specified preprocessing fields. % Subj_list = whifun_create_fields_preproc(Subj_list);

See also ISFIELD.

```matlab
Subj_list_all = WHIFUN_CREATE_FIELDS_PREPROC(Subj_list_all) is a utility
```

## Author

Author: Pratik Jain
