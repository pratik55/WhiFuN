# corrvec

**Source:** `whifun_functions/corrvec.m:1`

## Signature

```matlab
function Corr = corrvec(mat,d)
```

## Summary

CORRVEC Extracts the unique upper-triangular elements of a 2D or 3D correlation/adjacency matrix.

## Syntax

```matlab
CORR = CORRVEC(MAT, D)
```

## Description

This function is primarily used to convert symmetric matrices (like correlation matrices or adjacency matrices) into a compact vector representation, which is often necessary before feeding data into clustering or multivariate statistical algorithms.

## Input Arguments

### `MAT`
The input matrix (or matrices).
- If 2D (N x N): A single symmetric matrix (e.g., a connectivity map).
- If 3D (N x N x S): A stack of S symmetric matrices (e.g., dynamic FC windows, or multiple subjects).

### `D`
(Optional, default 0) Flag to determine whether to include the diagonal elements (the self-correlations, which are usually 1):
- D = 0: Exclude the diagonal (upper off-diagonal triangle only).
- D = 1: Include the diagonal (upper triangle including diagonal).

## Output Arguments

### `CORR`
The vectorized form of the unique elements.
- If MAT is N x N: Output size is (N*(N-1)/2) x 1 (if D=0) or (N*(N+1)/2) x 1 (if D=1).
- If MAT is N x N x S: Output size is (N*(N-1)/2) x S (if D=0) or (N*(N+1)/2) x S (if D=1).

## Author

Author: Pratik Jain
