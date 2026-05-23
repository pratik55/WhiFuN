# whifun_create_group_mask

**Source:** `whifun_functions/whifun_create_group_mask.m:1`

## Signature

```matlab
function [group_mask_WM_path,group_mask_GM_path,d] = whifun_create_group_mask(out_analysis_path,Subj_list,grp_WM_mask_name,indi_thres_wm,grp_thres_wm,grp_GM_mask_name,indi_thres_gm,grp_thres_gm,over_write,d_flag,d,steps_,tot_steps)
```

## Summary

WHIFUN_CREATE_GROUP_MASK Creates group-level White Matter (WM) and Gray Matter (GM) masks.

## Syntax

```matlab
[GROUP_MASK_WM_PATH, GROUP_MASK_GM_PATH, D] = WHIFUN_CREATE_GROUP_MASK(OUT_ANALYSIS_PATH, SUBJ_LIST, GRP_WM_MASK_NAME, INDI_THRES_WM, GRP_THRES_WM, GRP_GM_MASK_NAME, INDI_THRES_GM, GRP_THRES_GM, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS)
```

## Description

This function creates group-level WM and GM masks based on individual segmentation maps (e.g., from SPM/CAT) and functional data coverage.

## Input Arguments

### `OUT_ANALYSIS_PATH`
Main output directory where 'Group_Masks' folder will be created.

### `SUBJ_LIST`
Structure array containing subject information, including paths to individual WM ('WM_MNI'), GM ('GM_MNI') segmentation maps in MNI space, and final functional images ('final_func_MNI').

### `GRP_WM_MASK_NAME`
Filename for the output group WM mask (e.g., 'group_wm_mask.nii').

### `INDI_THRES_WM`
Individual-level WM probability threshold (e.g., 0.8).

### `GRP_THRES_WM`
Group-level WM consensus threshold (0-100%) for final inclusion. A voxel is included if its WM probability (from INDI_THRES_WM step) is above this threshold in a GRP_THRES_WM percentage of subjects.

### `GRP_GM_MASK_NAME`
Filename for the output group GM mask (e.g., 'group_gm_mask.nii').

### `INDI_THRES_GM`
Individual-level GM probability threshold (e.g., 0.6) for initial count.

### `GRP_THRES_GM`
Group-level GM consensus threshold (0-100%) for final inclusion.

### `OVER_WRITE`
Boolean (0 or 1) indicating whether to overwrite existing group masks.

### `D_FLAG, D, STEPS_, TOT_STEPS`
(Optional) Parameters for progress dialogue box (typically used in a GUI environment).

## Output Arguments

### `GROUP_MASK_WM_PATH`
Full path to the created or existing group WM mask file.

### `GROUP_MASK_GM_PATH`
Full path to the created or existing group GM mask file.

### `D`
Updated progress dialogue handle.

## Process Steps

1. **Initialization:** Checks for optional arguments and creates the output directory.
2. **Consensus Mask Creation:** For each subject, counts voxels where WM/GM
probability is above `INDI_THRES_WM`/`INDI_THRES_GM`.

3. **Normalization:** Converts voxel counts to a probability (proportion of subjects).
4. **Subcortical Removal:** Removes voxels corresponding to subcortical structures
(Putamen, GP, etc.) from the WM mask (and assigns them to GM) using the Harvard-Oxford Atlas to address segmentation artifacts.

5. **Group Thresholding:** Applies the `GRP_THRES_WM`/`GRP_THRES_GM` to finalize
the WM and GM masks. The GM mask is also constrained to be non-overlapping with the WM mask.

6. **Functional Data Coverage Check:** Removes WM/GM voxels where functional data
is not present (non-NaN/non-zero) in less than 80% of participants to exclude regions like the spinal cord.

7. **Saving:** The final group masks are saved as NIfTI files.

## Requirements

'whifun_create_file', 'reslice_data', 'niftiread', 'niftiinfo', 'niftisave' functions from the WhiFuN toolbox and compatible NIfTI handling.

## Author

Author: Pratik Jain
