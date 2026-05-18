- **Key Features:**
  - WHIFUN_COMPUTE_STABILITY Calculates the stability of Functional Networks (FNs) using the average maximum Dice similarity coefficient across all unique pairwise comparisons of network maps. [AVG_MAX_DICE, DICEIJ_ALL, VOX_NUM_ALL] = WHIFUN_COMPUTE_STABILITY(NET_LIST, NET_INCLUDE) This is typically used in cross-validation/bootstrapping steps of FN creation (e.g., k-means clustering) to assess how consistently networks are identified across different partitions of the data. Input Arguments: NET_LIST - A structure array (e.g., from MATLAB's `dir` function) where each element points to a NIfTI file
  - Internal calls detected: `dice_iou`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_compute_stability()`
- **Functional Purpose:** WHIFUN_COMPUTE_STABILITY Calculates the stability of Functional Networks (FNs) using the average maximum Dice similarity coefficient across all unique pairwise comparisons of network maps. [AVG_MAX_DICE, DICEIJ_ALL, VOX_NUM_ALL] = WHIFUN_COMPUTE_STABILITY(NET_LIST, NET_INCLUDE) This is typically used in cross-validation/bootstrapping steps of FN creation (e.g., k-means clustering) to assess how consistently networks are identified across different partitions of the data. Input Arguments: NET_LIST - A structure array (e.g., from MATLAB's `dir` function) where each element points to a NIfTI file containing the labeled Functional Network map for a specific data fold. NET_INCLUDE - (Optional, de
- **Arguments:**
  - `net_list` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `net_include` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
