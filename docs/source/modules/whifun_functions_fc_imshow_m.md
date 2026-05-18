- **Key Features:**
  - FC_IMSHOW Displays a functional connectivity (FC) matrix with network boundaries and labels. FC_IMSHOW(MAP, SORT_IDX_VAL, NET_NAMES) This function visualizes a functional connectivity matrix, typically one that has been reordered based on network assignments, and overlays black lines to demarcate the boundaries between the identified networks. It also labels the axes with the network names or indices. Input Arguments: MAP - The functional connectivity matrix (N x N) to display. Should be symmetric and ideally sorted by network assignment. SORT_IDX_VAL - A vector (N x 1) containing the network 
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `fc_imshow()`
- **Functional Purpose:** FC_IMSHOW Displays a functional connectivity (FC) matrix with network boundaries and labels. FC_IMSHOW(MAP, SORT_IDX_VAL, NET_NAMES) This function visualizes a functional connectivity matrix, typically one that has been reordered based on network assignments, and overlays black lines to demarcate the boundaries between the identified networks. It also labels the axes with the network names or indices. Input Arguments: MAP - The functional connectivity matrix (N x N) to display. Should be symmetric and ideally sorted by network assignment. SORT_IDX_VAL - A vector (N x 1) containing the network index for each ROI/voxel in the MAP matrix. The map is assumed to be sorted such that all elements b
- **Arguments:**
  - `map` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `sort_idx_val` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `net_names` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
