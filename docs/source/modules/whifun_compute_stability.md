# whifun_compute_stability

Source: `whifun_functions/whifun_compute_stability.m:1`

```matlab
function [avg_max_dice,diceij_all,vox_num_all] = whifun_compute_stability(net_list,net_include)
```

## MATLAB Help

WHIFUN_COMPUTE_STABILITY Calculates the stability of Functional Networks (FNs)
  using the average maximum Dice similarity coefficient across all unique
  pairwise comparisons of network maps.

  [AVG_MAX_DICE, DICEIJ_ALL, VOX_NUM_ALL] = WHIFUN_COMPUTE_STABILITY(NET_LIST, NET_INCLUDE)

  This is typically used in cross-validation/bootstrapping steps of FN
  creation (e.g., k-means clustering) to assess how consistently networks
  are identified across different partitions of the data.

  Input Arguments:
  NET_LIST    - A structure array (e.g., from MATLAB's `dir` function)
                where each element points to a NIfTI file containing the
                labeled Functional Network map for a specific data fold.
  NET_INCLUDE - (Optional, default []) The number of top-ranked networks
                to include in the calculation of the average maximum Dice
                coefficient.
                - If empty ([]), it uses the minimum number of networks
                  between the two maps being compared (standard practice
                  when the number of clusters K is the same, or for
                  fair comparison when K differs slightly).
                - If a number (e.g., K), it uses the top K matches.

  Output Arguments:
  AVG_MAX_DICE - A vector where each element is the average maximum Dice
                 coefficient computed for one unique pairwise comparison
                 between the networks in NET_LIST.
  DICEIJ_ALL   - A cell array (Upper triangular) storing the raw Dice
                 similarity matrices for each pairwise comparison.
                 DICEIJ_ALL{i, j} is a matrix where entry (m, n) is the
                 Dice coefficient between network m from map i and network n from map j.
  VOX_NUM_ALL  - A cell array storing the voxel count for each network in
                 the maps. VOX_NUM_ALL{i} is a vector of voxel counts for
                 the networks in map i.

  Dependencies: 'dice_iou' function (a custom utility that
                calculates Dice/IoU similarity and returns voxel counts).

  Author: Pratik Jain
