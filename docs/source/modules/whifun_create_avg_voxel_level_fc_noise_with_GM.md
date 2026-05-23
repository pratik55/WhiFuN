# whifun_create_avg_voxel_level_fc_noise_with_GM

Source: `whifun_functions/whifun_create_avg_voxel_level_fc_noise_with_GM.m:1`

```matlab
function [avg_vox_level_FC,wm_group_mask_voxels] = whifun_create_avg_voxel_level_fc_noise_with_GM(cluster_folder,Subj_list,wm_group_mask_path,gm_group_mask_path,sub_sample_choose,over_write,d_flag,d,steps_,tot_steps)
```

## MATLAB Help

WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC Creates the group-average Voxel-Level Functional Connectivity (FC) matrix.

  [AVG_VOX_LEVEL_FC, GROUP_MASK_VOXELS] = WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC(CLUSTER_FOLDER, SUBJ_LIST, GROUP_MASK_PATH, SUB_SAMPLE_CHOOSE, WM_OR_GM, FOCUS_REGION_CHECK, FOCUS_REGION_MASK_PATH, OVER_WRITE, ...)

  This function computes the group-average FC matrix between all voxels in a
  target mask (e.g., WM or GM) and either all or a subsampled subset of
  those voxels. This average matrix is then used as the input feature matrix
  for group-level clustering. The function includes memory checks and
  handles individual subject-specific segmentation masks.

  Input Arguments:
  CLUSTER_FOLDER      - Output directory for saving the final FC matrix and intermediate files.
  SUBJ_LIST           - Structure array containing subject information and file paths.
  GROUP_MASK_PATH     - Full path to the NIfTI file of the group-level target mask (e.g., WM or GM mask).
  SUB_SAMPLE_CHOOSE   - String flag: 'Subsample' or 'Use entire FC'. Determines if a subsample of voxels is used for features (columns).
  WM_OR_GM            - String flag: 'WM' or 'GM', used for subsampling density and segmentation checks.
  FOCUS_REGION_CHECK  - (Optional, default 0) Flag: 1 to exclude a focus region (e.g., Corpus Callosum) from the group mask.
  FOCUS_REGION_MASK_PATH - (Optional) Path to the NIfTI file of the focus region mask.
  OVER_WRITE          - (Optional, default 0) Flag: 1 to overwrite existing files, 0 to skip.
  D_FLAG, D, STEPS_, TOT_STEPS - (Optional) Parameters for progress dialogue box (GUI support).

  Output Arguments:
  AVG_VOX_LEVEL_FC    - The final group-average FC matrix (N_Voxels_Masked x N_Features).
  GROUP_MASK_VOXELS   - The linear indices of the remaining valid voxels in the group mask.

  Dependencies: 'whifun_niftiread', 'niftiread', 'whifun_create_file',
                'complete_filepath', 'reslice_data'.

  Author: Pratik Jain
