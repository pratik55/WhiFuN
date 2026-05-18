- **Key Features:**
  - CORRVEC Extracts the unique upper-triangular elements of a 2D or 3D correlation/adjacency matrix. CORR = CORRVEC(MAT, D) This function is primarily used to convert symmetric matrices (like correlation matrices or adjacency matrices) into a compact vector representation, which is often necessary before feeding data into clustering or multivariate statistical algorithms. Input Arguments: MAT - The input matrix (or matrices). - If 2D (N x N): A single symmetric matrix (e.g., a connectivity map). - If 3D (N x N x S): A stack of S symmetric matrices (e.g., dynamic FC windows, or multiple subjects).
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: Statistics and Machine Learning Toolbox

## Function: `corrvec()`
- **Functional Purpose:** CORRVEC Extracts the unique upper-triangular elements of a 2D or 3D correlation/adjacency matrix. CORR = CORRVEC(MAT, D) This function is primarily used to convert symmetric matrices (like correlation matrices or adjacency matrices) into a compact vector representation, which is often necessary before feeding data into clustering or multivariate statistical algorithms. Input Arguments: MAT - The input matrix (or matrices). - If 2D (N x N): A single symmetric matrix (e.g., a connectivity map). - If 3D (N x N x S): A stack of S symmetric matrices (e.g., dynamic FC windows, or multiple subjects). D - (Optional, default 0) Flag to determine whether to include the diagonal elements (the self-corr
- **Arguments:**
  - `mat` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
