- **Key Features:**
  - WHIFUN_CREATE_FOCUS_REGION_MASK_IDX Generates a labeled index NIfTI file from a binary Focus Region (FR) mask, where each non-zero voxel is assigned a unique sequential index. WHIFUN_CREATE_FOCUS_REGION_MASK_IDX(OUT_FR_VOX_IDX_FILE, FR_MASK_FILENAME, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS) This function is crucial for converting a simple binary mask into an indexed list, which is often required for subsequent processing steps like extracting time series or constructing connectivity matrices based on voxel order. The output NIfTI volume has the same dimensions as the input mask, but non-zero 
  - Internal calls detected: `niftisave`, `whifun_create_file`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_create_focus_region_mask_idx()`
- **Functional Purpose:** WHIFUN_CREATE_FOCUS_REGION_MASK_IDX Generates a labeled index NIfTI file from a binary Focus Region (FR) mask, where each non-zero voxel is assigned a unique sequential index. WHIFUN_CREATE_FOCUS_REGION_MASK_IDX(OUT_FR_VOX_IDX_FILE, FR_MASK_FILENAME, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS) This function is crucial for converting a simple binary mask into an indexed list, which is often required for subsequent processing steps like extracting time series or constructing connectivity matrices based on voxel order. The output NIfTI volume has the same dimensions as the input mask, but non-zero voxels are re-labeled from 1 up to the total number of voxels in the FR. Input Arguments: OUT_FR_VOX
- **Arguments:**
  - `out_fr_vox_idx_file` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `fr_mask_filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
