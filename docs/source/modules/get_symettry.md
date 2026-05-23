# get_symettry

**Source:** `whifun_functions/get_symettry.m:1`

## Signature

```matlab
function Dice_coef_LR = get_symettry(current_clustering_solution)
```

## Summary

GET_SYMETTRY Measures the spatial symmetry of a functional network clustering solution

## Syntax

```matlab
DICE_COEF_LR = GET_SYMETTRY(CURRENT_CLUSTERING_SOLUTION)
```

## Description

by comparing the clustering patterns in the Left and Right hemispheres.

This function quantifies the degree to which a functional network solution is mirror-symmetric across the mid-sagittal plane. It achieves this by:

1. Separating the clustering volume into Left (L) and Right (R) halves.
2. Flipping the Right half along the Left-Right axis (Dim 1) so it aligns
with the Left half.

3. Masking both halves to only include voxels present in both.
4. Converting the L and R clustering solutions into Adjacency Matrices (AMs)
based on whether pairs of voxels belong to the same cluster.

5. Calculating the Dice similarity coefficient between the L-AM and R-AM.

## Input Arguments

### `CURRENT_CLUSTERING_SOLUTION`
A 3D NIfTI volume (X x Y x Z) where each non-zero voxel contains a cluster/network label (K). The X dimension is assumed to be the Left-Right axis.

## Output Arguments

### `DICE_COEF_LR`
The Dice coefficient (ranging from 0 to 1) representing the similarity between the Left and Right hemispheric clustering solutions. Assumptions:
- The first dimension (Dim 1) corresponds to the Left-Right axis.
- The image is oriented such that indices [1 : Mid_sagittal_slice] constitute one hemisphere (e.g., Left) and the rest is the other.
- Flipping Dim 1 of the whole volume and taking the first half aligns the mirrored Right hemisphere with the original Left hemisphere.

## Author

Author: Pratik Jain
