- **Key Features:**
  - VECCORR Converts a vectorized upper-triangular matrix back into a full square matrix. MAT = VECCORR(VEC) This function reconstructs a symmetric matrix (e.g., a correlation matrix) from its compact vector representation of the unique upper-off-diagonal elements. Input Arguments: VEC - The input vector or matrix containing the vectorized upper-off-diagonal elements. Expected dimensions: (N*(N-1)/2) x S, where N is the number of regions/ROIs and S is the number of matrices (e.g., subjects, windows). Output Arguments: MAT - The reconstructed full matrix (or stack of matrices). Expected dimensions:
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `veccorr()`
- **Functional Purpose:** VECCORR Converts a vectorized upper-triangular matrix back into a full square matrix. MAT = VECCORR(VEC) This function reconstructs a symmetric matrix (e.g., a correlation matrix) from its compact vector representation of the unique upper-off-diagonal elements. Input Arguments: VEC - The input vector or matrix containing the vectorized upper-off-diagonal elements. Expected dimensions: (N*(N-1)/2) x S, where N is the number of regions/ROIs and S is the number of matrices (e.g., subjects, windows). Output Arguments: MAT - The reconstructed full matrix (or stack of matrices). Expected dimensions: N x N x S. The diagonal elements are set to NaN. Derivation of N (Number of Regions): The number of
- **Arguments:**
  - `vec` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
