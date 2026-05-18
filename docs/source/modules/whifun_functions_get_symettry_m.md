- **Key Features:**
  - GET_SYMETTRY Measures the spatial symmetry of a functional network clustering solution by comparing the clustering patterns in the Left and Right hemispheres. DICE_COEF_LR = GET_SYMETTRY(CURRENT_CLUSTERING_SOLUTION) This function quantifies the degree to which a functional network solution is mirror-symmetric across the mid-sagittal plane. It achieves this by: 1. Separating the clustering volume into Left (L) and Right (R) halves. 2. Flipping the Right half along the Left-Right axis (Dim 1) so it aligns with the Left half. 3. Masking both halves to only include voxels present in both. 4. Conve
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `get_symettry()`
- **Functional Purpose:** GET_SYMETTRY Measures the spatial symmetry of a functional network clustering solution by comparing the clustering patterns in the Left and Right hemispheres. DICE_COEF_LR = GET_SYMETTRY(CURRENT_CLUSTERING_SOLUTION) This function quantifies the degree to which a functional network solution is mirror-symmetric across the mid-sagittal plane. It achieves this by: 1. Separating the clustering volume into Left (L) and Right (R) halves. 2. Flipping the Right half along the Left-Right axis (Dim 1) so it aligns with the Left half. 3. Masking both halves to only include voxels present in both. 4. Converting the L and R clustering solutions into Adjacency Matrices (AMs) based on whether pairs of voxel
- **Arguments:**
  - `current_clustering_solution` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
