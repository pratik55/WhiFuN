# whifun_get_best_k

**Source:** `whifun_functions/whifun_get_best_k.m:1`

## Signature

```matlab
function K = whifun_get_best_k(out_path,avg_vox_level_FC,K_range_l,K_range_h,CV_folds,num_replicates,size_chunk,d_flag,d,steps_,tot_steps)
```

## Summary

WHIFUN_GET_BEST_K Performs cross-validation stability analysis to determine the optimal number of clusters (K).

## Syntax

```matlab
[K, DICE_COEF, ELB] = WHIFUN_GET_BEST_K(OUT_PATH, AVG_VOX_LEVEL_FC, K_RANGE_L, K_RANGE_H, CV_FOLDS, NUM_REPLICATES, SIZE_CHUNK, ...)
```

## Description

This function implements a feature-based cross-validation strategy to measure the stability of k-means clustering solutions for a range of K values. Stability is calculated using the average maximum Dice similarity coefficient between the clustering solutions obtained from different subsets (folds) of the input feature matrix.

The principle is based on the idea that a clustering solution for the optimal K will be highly consistent (stable) even when trained on a different subset of features (Lange et al., Neural Comput 2004).

## Input Arguments

### `OUT_PATH`
Full path for saving the figure output (e.g., 'path/to/k_stability.png').

### `AVG_VOX_LEVEL_FC`
The group-level connectivity matrix used for clustering. Expected dimensions: N_Voxels x N_Features (e.g., Voxel_TS x N_Subjects*N_Timepoints).

### `K_RANGE_L`
Lower bound of the K range for the grid search.

### `K_RANGE_H`
Upper bound of the K range for the grid search.

### `CV_FOLDS`
Number of cross-validation folds (feature subsets) to divide the data into.

### `NUM_REPLICATES`
Number of k-means replicates to run for each fold and K (to avoid local minima).

### `SIZE_CHUNK`
Size of the chunk used for computing the adjacency matrices. This is used to reduce memory load when calculating the Dice coefficient for large voxel counts.

### `D_FLAG, D, STEPS_, TOT_STEPS`
(Optional) Parameters for progress dialogue box (GUI support).

## Output Arguments

### `K`
The optimal K value selected by the user after reviewing the stability plot.

### `DICE_COEFFICIENT_FOLDS_ALL`
Vector of the average maximum Dice coefficient stability metric for each K.

### `ELB`
Vector of the average k-means Sum of Squared Distances (Elbow) for each K.

## Requirements

'whifun_plot_dice_coef_and_elb'

## Author

Author: Pratik Jain
