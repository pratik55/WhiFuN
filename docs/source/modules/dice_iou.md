# dice_iou

**Source:** `whifun_functions/dice_iou.m:1`

## Signature

```matlab
function [dice,IOU,vox_num_1,vox_num_2] = dice_iou(kmeans_net_1_path,kmeans_net_2_path,align_net,fig_dice)
```

## Summary

DICE_IOU Computes the Dice Similarity Coefficient and Intersection of Union (IoU)

## Syntax

```matlab
[DICE, IOU, VOX_NUM_1, VOX_NUM_2] = DICE_IOU(KMEANS_NET_1_PATH, KMEANS_NET_2_PATH, ALIGN_NET, FIG_DICE)
```

## Description

between two functional network (FN) atlas NIfTI files. It can optionally align the second network to the first and generate a visualization of the similarity matrix.

## Input Arguments

### `KMEANS_NET_1_PATH`
Full path to the first FN NIfTI file, or the N-dimensional array itself.

### `KMEANS_NET_2_PATH`
Full path to the second FN NIfTI file, or the N-dimensional array itself.

### `ALIGN_NET`
(Optional, default 0) Flag to align net_2 to net_1:
- ALIGN_NET = 1: Relabels net_2 based on the maximum Dice match to net_1 and saves the aligned network.
- ALIGN_NET = 0: No alignment.

### `FIG_DICE`
(Optional, default 0) Flag to visualize the Dice matrix:
- FIG_DICE = 1: Displays a heatmap of the Dice matrix.
- FIG_DICE = 0: No plot generated.

## Output Arguments

### `DICE`
A matrix where DICE(i, j) is the Dice coefficient between network 'i' from the first map and network 'j' from the second map.

### `IOU`
A matrix where IOU(i, j) is the Jaccard Index (IoU) between network 'i' from the first map and network 'j' from the second map.

### `VOX_NUM_1`
A vector of voxel counts for each network in the first map.

### `VOX_NUM_2`
A vector of voxel counts for each network in the second map.

## Requirements

'niftiread', 'niftiinfo', 'niftisave', and 'whifun_convert_3d_to_4d_atlas' (assumed).

## Author

Author: Pratik Jain
