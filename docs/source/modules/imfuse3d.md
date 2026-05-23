# imfuse3d

**Source:** `whifun_functions/imfuse3d.m:1`

## Signature

```matlab
function out = imfuse3d(A,B)
```

## Summary

IMFUSE3D Performs slice-wise image fusion for 3D volumes.

## Syntax

```matlab
OUT = IMFUSE3D(A, B) iterates through the third dimension of two
```

## Description

volumes, A and B, and fuses each corresponding pair of 2D slices using the IMFUSE function. The resulting color composite is converted back to grayscale by taking the mean across color channels.

## Input Arguments

### `A`
A 3D numeric array (e.g., anatomical reference).

### `B`
A 3D numeric array of the same size as A (e.g., overlay).

## Output Arguments

### `out`
A 3D numeric array containing the fused intensity values.

## Examples

EXAMPLE: % Fuse a T1 anatomical with a T2 or functional volume fused_vol = imfuse3d(t1_vol, t2_vol); whifun_figure_montage(fused_vol, 8, 8);

NOTES:

- This function requires the Image Processing Toolbox.
- By default, imfuse creates a "falsecolor" composite. Taking the
mean across the 3rd dimension of the output of imfuse converts the RGB fusion back into a single intensity value.

See also IMFUSE, RGB2GRAY, WHIFUN_FIGURE_MONTAGE.
