- **Key Features:**
  - WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC Creates the group-average Voxel-Level Functional Connectivity (FC) matrix. [AVG_VOX_LEVEL_FC, GROUP_MASK_VOXELS] = WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC(CLUSTER_FOLDER, SUBJ_LIST, GROUP_MASK_PATH, SUB_SAMPLE_CHOOSE, WM_OR_GM, FOCUS_REGION_CHECK, FOCUS_REGION_MASK_PATH, OVER_WRITE, ...) This function computes the group-average FC matrix between all voxels in a target mask (e.g., WM or GM) and either all or a subsampled subset of those voxels. This average matrix is then used as the input feature matrix for group-level clustering. The function includes memory checks a
  - Internal calls detected: `reslice_data`, `whifun_create_file`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox, ANTs command-line suite

## Function: `whifun_create_avg_voxel_level_fc_noise_with_GM()`
- **Functional Purpose:** WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC Creates the group-average Voxel-Level Functional Connectivity (FC) matrix. [AVG_VOX_LEVEL_FC, GROUP_MASK_VOXELS] = WHIFUN_CREATE_AVG_VOXEL_LEVEL_FC(CLUSTER_FOLDER, SUBJ_LIST, GROUP_MASK_PATH, SUB_SAMPLE_CHOOSE, WM_OR_GM, FOCUS_REGION_CHECK, FOCUS_REGION_MASK_PATH, OVER_WRITE, ...) This function computes the group-average FC matrix between all voxels in a target mask (e.g., WM or GM) and either all or a subsampled subset of those voxels. This average matrix is then used as the input feature matrix for group-level clustering. The function includes memory checks and handles individual subject-specific segmentation masks. Input Arguments: CLUSTER_FOLDER - Output
- **Arguments:**
  - `cluster_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `wm_group_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `gm_group_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `sub_sample_choose` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
