# fc_imshow

**Source:** `whifun_functions/fc_imshow.m:1`

## Signature

```matlab
function fc_imshow(map,sort_idx_val,net_names)
```

## Summary

FC_IMSHOW Displays a functional connectivity (FC) matrix with network boundaries and labels.

## Syntax

```matlab
FC_IMSHOW(MAP, SORT_IDX_VAL, NET_NAMES)
```

## Description

This function visualizes a functional connectivity matrix, typically one that has been reordered based on network assignments, and overlays black lines to demarcate the boundaries between the identified networks. It also labels the axes with the network names or indices.

## Input Arguments

### `MAP`
The functional connectivity matrix (N x N) to display. Should be symmetric and ideally sorted by network assignment.

### `SORT_IDX_VAL`
A vector (N x 1) containing the network index for each ROI/voxel in the MAP matrix. The map is assumed to be sorted such that all elements belonging to network 1 are first, then network 2, and so on.

### `NET_NAMES`
(Optional) A cell array of strings or a numeric vector containing the names/labels for each network. If omitted or only two arguments are provided, network indices (1, 2, 3...) will be used as labels. Usage:
1. Display the matrix using imagesc (scales colors automatically).
2. Overlay black lines to highlight the boundaries between networks based on changes in the SORT_IDX_VAL vector.
3. Center the tick marks and apply network labels on both axes.

## Examples

Example: % Assume 'FC_matrix' is 100x100 and 'network_labels' is 100x1 % and the matrix is already sorted. % net_names = {'Net A', 'Net B', 'Net C'}; % fc_imshow(FC_matrix, network_labels, net_names)

## Author

Author: Pratik Jain
