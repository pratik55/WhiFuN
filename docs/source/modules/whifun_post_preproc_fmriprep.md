# whifun_post_preproc_fmriprep

**Source:** `whifun_functions/whifun_post_preproc_fmriprep.m:1`

## Signature

```matlab
function Subj_list_1 = whifun_post_preproc_fmriprep(quality_control_path, Subj_list_1, varargin)
```

## Summary

WHIFUN_POST_PREPROC_FMRIPREP Post-processing pipeline for fMRIPrep outputs.

## Syntax

```matlab
SUBJ_LIST_1 = WHIFUN_POST_PREPROC_FMRIPREP(QC_PATH, SUBJ_STRUCT, 'Name', Value)
```

## Description

takes the outputs of an fMRIPrep pipeline and performs additional processing steps: volume discarding, FD calculation, nuisance regression (using fMRIPrep's confound TSV), and spatial smoothing.

## Input Arguments

### `quality_control_path`
String. Path for logs and QC reports.

### `Subj_list_1`
Struct. Must contain .func_folder, .func_name, .anat_folder, and .anat_name. OPTIONAL PARAMETERS (Name-Value Pairs): 'over_write'
- Logical. If true, existing files are re-created. 'n_vol_dis'
- Integer. Initial volumes to discard (Default: 0). 'max_fd'
- Numeric. Framewise Displacement threshold (Default: 0.5). 'Reg_'
- Logical. Toggle nuisance regression (Default: 0). 'Reg_params'
- Cell array. List of confound names from fMRIPrep TSV to include (e.g., {'trans_x', 'csf'}). 'Smooth_'
- Logical. Toggle spatial smoothing (Default: 0). 'smooth_fwhm'
- Numeric. Smoothing kernel size in mm (Default: 4).

## Output Arguments

### `Subj_list_1`
Updated struct with paths to regressed and smoothed NIfTIs in MNI space.

## Examples

EXAMPLE: subj = whifun_post_preproc_fmriprep(qc_path, subj, 'Reg_', 1, ... 'Reg_params', {'trans_x', 'trans_y', 'trans_z', 'csf'});

See also WHIFUN_BIDS_JOIN, WHIFUN_REGRESS_ANY, WHIFUN_PARSE_BIDS_FILENAME. ---- input parser ----
