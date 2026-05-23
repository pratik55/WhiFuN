# whifun_nuisance_regress_preproc

**Source:** `whifun_functions/whifun_nuisance_regress_preproc.m:1`

## Signature

```matlab
function [Subj_list_1,out_func_path,out_func_mask_path] = whifun_nuisance_regress_preproc(quality_control_path,Subj_list_1,in_func_path,in_anat_mask_subj_space_path,Reg_pre,n_pca,in_csf_mat_path,in_motion_txt_path,log_fileID,over_write) %#ok<INUSD>
```

## Summary

WHIFUN_NUISANCE_REGRESS_PREPROC Orchestrates nuisance regression.

## Syntax

```matlab
[Subj_list_1, out_func_path] = WHIFUN_NUISANCE_REGRESS_PREPROC(...)
```

## Description

is a high-level function that manages the nuisance regression step of a neuroimaging preprocessing pipeline. It automates the process of removing unwanted signals from the functional data, such as head motion artifacts and physiological noise.

The function first checks if a pre-regressed file already exists. Based on the `over_write` flag, it either skips the process or calls the `whifun_regress` function to perform the actual regression. This utility function ensures that the regression is performed only when needed.

The function updates the subject structure with the path to the newly regressed functional file and logs the process output to a file. In case of an error, it catches the exception, updates the subject's `error` flag, and logs the detailed error information.

## Input Arguments

### `quality_control_path`
Path to the quality control directory for logs.

### `Subj_list_1`
A single subject structure to be updated.

### `in_func_path`
Path to the input functional file.

### `in_anat_mask_subj_space_path`
Path to the anatomical mask file.
