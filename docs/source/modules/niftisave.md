# niftisave

**Source:** `whifun_functions/niftisave.m:1`

## Signature

```matlab
function niftisave(niftiimage,filename,info,add_offset,multi_scale)
```

## Summary

NIFTISAVE Saves a MATLAB array as a NIfTI-1 file, updating essential header

## Syntax

```matlab
NIFTISAVE(NIFTIIMAGE, FILENAME, INFO, ADD_OFFSET, MULTI_SCALE)
```

## Description

information from a provided info structure.

This is a utility wrapper for MATLAB's built-in `niftiwrite` function. It ensures that the NIfTI header information (INFO) is correctly updated to reflect the dimensions, datatype, and name of the image data being saved.

## Input Arguments

### `NIFTIIMAGE`
The MATLAB array (2D, 3D, or 4D) containing the image data to be saved as a NIfTI file.

### `FILENAME`
The desired full path and filename (with extension, e.g., '.nii') for the output NIfTI file.

### `INFO`
A structure, typically obtained from a previous `niftiread` call, containing the NIfTI header information (metadata) to use for the new file.

### `ADD_OFFSET`
(Optional) Value to set as the 'AdditiveOffset' (qform/sform `qoffset_b` or `srow_b`) in the NIfTI header, used for adding offset.

### `MULTI_SCALE`
(Optional) Value to set as the 'MultiplicativeScaling' (sform/qform `qfac` or `srow_a`) in the NIfTI header, used for scaling. Output: A NIfTI file is saved to the location specified by FILENAME.

## Author

Author: Pratik Jain
