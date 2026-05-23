# whifun_create_FN_Kmeans_WM_GM

**Source:** `whifun_functions/whifun_create_FN_Kmeans_WM_GM.m:1`

## Signature

```matlab
function whifun_create_FN_Kmeans_WM_GM(output_folder,WM_or_GM,K_range_l,K_range_h,group_mask_path_wm,group_mask_path_gm,varargin)
```

## Summary

WHIFUN_CREATE_FN_KMEANS Creates WM/GM Functional Networks using K-means clustering

## Description

whifun_create_FN_Kmeans(...) performs K-means clustering on the average voxel-level functional connectivity matrix across subjects and generates functional networks (FNs). It also saves BrainNet images and average time series for each FN.

Required Inputs: output_folder    - Path to output folder WM_or_GM         - 'WM-GM' or 'GM-WM' K_range_l        - Lower bound for K (clusters) K_range_h        - Upper bound for K group_mask_path  - Path to group-level brain mask (NIfTI)

Optional Inputs: sub_sample_choose- Subsample flag/strategy (default: 'Sub sample') CV_folds         - Number of cross-validation folds (default: 4) focus_check      - Apply focus mask (default: 0) focus_mask_path  - Focus mask path or 0 if unused (default: 0) num_replicates   - Replicates for K-means (default: 10) size_chunk       - Chunk size for computation (default: 100) over_write       - Overwrite existing files (default: 0) d                - Progress bar handle (default: 0) d_flag           - Display flag for progress bar (default: 0) steps_           - Current pipeline step (default: 0) tot_steps        - Total steps in pipeline (default: 0)

## Examples

Example: whifun_create_FN_Kmeans('output_folder','/path/out',... 'WM_or_GM','WM','K_range_l',2,'K_range_h',10,... 'group_mask_path','mask.nii');

## Author

Author: Pratik Jain
