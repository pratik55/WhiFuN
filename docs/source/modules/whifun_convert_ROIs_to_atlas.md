# whifun_convert_ROIs_to_atlas

**Source:** `whifun_functions/whifun_convert_ROIs_to_atlas.m:1`

## Signature

```matlab
function whifun_convert_ROIs_to_atlas(folder_path,pattern,out_path)
```

## Summary

WHIFUN_CONVERT_ROIS_TO_ATLAS Combines multiple binary NIfTI ROI masks into a single

## Syntax

```matlab
WHIFUN_CONVERT_ROIS_TO_ATLAS(FOLDER_PATH, PATTERN, OUT_FOLDER)
```

## Description

labeled NIfTI atlas volume.

This function reads a collection of NIfTI files, where each file represents a binary Region of Interest (ROI) mask. It then assigns a unique integer label to the voxels belonging to each ROI and saves the result as a single NIfTI atlas file.

## Input Arguments

### `FOLDER_PATH`
Full path to the directory containing the NIfTI ROI mask files.

### `PATTERN`
(Optional, default '') A wildcard pattern (e.g., '*.nii' or 'ROI_*.nii') to match the files to be included as ROIs. If empty, all files in the folder are considered.

### `OUT_FOLDER`
(Optional, default current working directory) The directory where the resulting atlas NIfTI file will be saved. Output File: An atlas NIfTI file named 'atlasLR.nii' is saved in OUT_FOLDER. Voxel values in this atlas correspond to the index (1, 2, 3, ...) of the input ROI files in the sorted list.

## Requirements

'niftiinfo', 'niftiread', and 'niftisave' functions.

## Author

Author: Pratik Jain
