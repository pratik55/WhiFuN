# mulmat

**Source:** `whifun_functions/mulmat.m:1`

## Signature

```matlab
function mul=mulmat(mat,f)
```

## Summary

MULMAT Calculates the element-wise product across the 3rd dimension.

## Syntax

```matlab
MUL = MULMAT(MAT) computes the cumulative product of all 2D slices
MUL = MULMAT(MAT, F) allows toggling the figure display. If F is 1
```

## Description

contained in the 3D matrix MAT. The result is a 2D matrix of the same height and width as the input slices.

(default), a new figure window is opened. If F is 0, it plots in the current axes.

## Input Arguments

### `mat`
A 3D numeric array (Height x Width x Slices).

### `f`
Binary flag (0 or 1). Determines if a new figure is created.

## Output Arguments

### `mul`
The resulting 2D product matrix. MATHEMATICAL NOTE: For each voxel (i,j), the output is calculated as: $$P(i,j) = \prod_{k=1}^{n} A(i,j,k)$$ where n is the number of slices in the 3rd dimension. See also PROD, IMAGESC, COLORBAR.

## Author

Author: Pratik Jain
