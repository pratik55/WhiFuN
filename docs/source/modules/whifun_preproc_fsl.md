# whifun_preproc_fsl

**Source:** `whifun_functions/whifun_preproc_fsl.m:1`

## Signature

```matlab
function Subj_list_1 = whifun_preproc_fsl(quality_control_path, Subj_list_1, varargin)
```

## Summary

WHIFUN_PREPROC_FSL Comprehensive FSL-based fMRI preprocessing pipeline.

## Syntax

```matlab
SUBJ_LIST_1 = WHIFUN_PREPROC_FSL(QC_PATH, SUBJ_STRUCT, 'Name', Value)
```

## Description

executes a full preprocessing workflow for a single subject, including volume discarding, motion correction (MCFLIRT), FD calculation, anatomical processing (fsl_anat), normalization to MNI space, nuisance regression, and spatial smoothing.

## Input Arguments

### `quality_control_path`
String. Path to the directory where logs and QC outputs will be stored.

### `Subj_list_1`
Struct. Contains subject-specific fields: .name        : Subject ID .func_folder : Path to functional data .func_name   : Name of functional NIfTI .anat_folder : Path to anatomical data .anat_name   : Name of anatomical NIfTI OPTIONAL PARAMETERS (Name-Value Pairs): 'over_write'
- Logical. Re-run steps even if files exist (Default: 0). 'FSLDIR'
- String. Path to FSL installation. 'n_vol_dis'
- Integer. Number of initial volumes to discard (Default: 0). 'max_fd'
- Numeric. Framewise Displacement threshold (Default: 0.5). 'Reg_CSF'
- Logical. Perform CSF nuisance regression (Default: 0). 'motion_reg'
- Logical. Perform motion nuisance regression (Default: 0). 'smooth_fwhm'
- Numeric. Smoothing kernel size in mm (Default: 4). 'WM_GM_seperate'
- Logical. Use tissue-specific smoothing (Default: 1).

## Output Arguments

### `Subj_list_1`
Updated struct containing paths to all processed files (e.g., .func_MNI, .GM_MNI).

## Requirements

FSL (mcflirt, fsl_anat, epi_reg, applywarp, fslmaths, FAST).

See also MCFLIRT, FSL_ANAT, WHIFUN_REGRESS_ANY. ---- input parser ----
