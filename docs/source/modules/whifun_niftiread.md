# whifun_niftiread

**Source:** `whifun_functions/whifun_niftiread.m:1`

## Signature

```matlab
function [volume,info] = whifun_niftiread(image_path)
```

## Summary

WHIFUN_NIFTIREAD Reads a NIfTI file and applies scaling factors.

## Syntax

```matlab
[volume, info] = WHIFUN_NIFTIREAD(image_path) reads a NIfTI file,
```

## Description

correctly applying the stored scaling and offset values from the file's header. This is a crucial step for ensuring that the voxel intensity values are interpreted correctly, as many NIfTI files store data as integers to save space and require a scaling factor to be applied for the correct floating-point representation.

The function first reads the volume data and the header information using MATLAB's built-in `niftiread` and `niftiinfo` functions. It then applies the formula: `y = AdditiveOffset + x * MultiplicativeScaling`, where `x` is the raw data and `y` is the corrected data.

## Input Arguments

### `image_path`
The full path to the NIfTI file to be read.

## Output Arguments

### `volume`
A numeric array containing the corrected voxel data.

### `info`
A structure containing the header information of the NIfTI file. See also NIFTIREAD, NIFTIINFO.

## Author

Author: Pratik Jain
