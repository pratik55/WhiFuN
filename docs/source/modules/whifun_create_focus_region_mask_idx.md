# whifun_create_focus_region_mask_idx

**Source:** `whifun_functions/whifun_create_focus_region_mask_idx.m:1`

## Signature

```matlab
function whifun_create_focus_region_mask_idx(out_fr_vox_idx_file,fr_mask_filename, over_write,d_flag,d,steps_,tot_steps)
```

## Summary

WHIFUN_CREATE_FOCUS_REGION_MASK_IDX Generates a labeled index NIfTI file

## Syntax

```matlab
WHIFUN_CREATE_FOCUS_REGION_MASK_IDX(OUT_FR_VOX_IDX_FILE, FR_MASK_FILENAME, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS)
```

## Description

from a binary Focus Region (FR) mask, where each non-zero voxel is assigned a unique sequential index.

This function is crucial for converting a simple binary mask into an indexed list, which is often required for subsequent processing steps like extracting time series or constructing connectivity matrices based on voxel order. The output NIfTI volume has the same dimensions as the input mask, but non-zero voxels are re-labeled from 1 up to the total number of voxels in the FR.

## Input Arguments

### `OUT_FR_VOX_IDX_FILE`
The desired full path and filename for the output NIfTI file containing the sequential voxel indices.

### `FR_MASK_FILENAME`
The full path to the input binary NIfTI mask file (Focus Region, e.g., Corpus Callosum mask).

### `OVER_WRITE`
(Optional, default 0) Flag to force overwriting of the output file if it exists.

### `D_FLAG, D, STEPS_, TOT_STEPS`
(Optional) Parameters for GUI progress dialogue box. Output File: A NIfTI file saved at OUT_FR_VOX_IDX_FILE with voxels sequentially labeled from 1 to N_voxels.

## Requirements

- `whifun_create_file` (Checks for existence and handles `over_write`).
- `whifun_niftiread` (Reads NIfTI data and header).
- `niftisave` (Saves the resulting indexed volume).

## Author

Author: Pratik Jain
