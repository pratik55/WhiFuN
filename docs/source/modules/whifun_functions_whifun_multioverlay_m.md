- **Key Features:**
  - whifun_multiOverlay Display multiple slices with overlays from volumes Inputs: volumes - 3D matrix or cell array of volumes (or file paths) overlayTypes - cell array: {'structure','contours'} for each volume colormaps - cell array of colormaps (e.g., {'gray','jet'}) slices - vector of slice indices (e.g. [20 30 40]) sliceType - 'axial','coronal','sagittal' Example: vol1 = rand(50,50,50); vol2 = rand(50,50,50) > 0.7; whifun_multiOverlay({vol1,vol2},{'structure','contours'},{'gray','jet'},[10 20 30],'axial'); % --- Load Volumes ---
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_multiOverlay()`
- **Functional Purpose:** whifun_multiOverlay Display multiple slices with overlays from volumes Inputs: volumes - 3D matrix or cell array of volumes (or file paths) overlayTypes - cell array: {'structure','contours'} for each volume colormaps - cell array of colormaps (e.g., {'gray','jet'}) slices - vector of slice indices (e.g. [20 30 40]) sliceType - 'axial','coronal','sagittal' Example: vol1 = rand(50,50,50); vol2 = rand(50,50,50) > 0.7; whifun_multiOverlay({vol1,vol2},{'structure','contours'},{'gray','jet'},[10 20 30],'axial'); % --- Load Volumes ---
- **Arguments:**
  - `volumes` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `overlayTypes` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `colormaps` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `sliceType` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
