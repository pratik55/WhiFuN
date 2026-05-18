- **Key Features:**
  - WHIFUN_CREATE_SPHERE Generates a list of voxel coordinates within a sphere. vox_list = WHIFUN_CREATE_SPHERE(center_vox, radius_mm, vox_dim, vol_size) creates a list of 1-based voxel coordinates that fall inside a sphere of a given radius. This function is a core utility for defining spherical regions of interest (ROIs) in neuroimaging analysis. The function first calculates a cubic grid of candidate voxels around the center point. It then filters this grid, keeping only the voxels whose Euclidean distance from the center (in millimeters) is less than or equal to the specified radius. Finally, 
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_create_sphere()`
- **Functional Purpose:** WHIFUN_CREATE_SPHERE Generates a list of voxel coordinates within a sphere. vox_list = WHIFUN_CREATE_SPHERE(center_vox, radius_mm, vox_dim, vol_size) creates a list of 1-based voxel coordinates that fall inside a sphere of a given radius. This function is a core utility for defining spherical regions of interest (ROIs) in neuroimaging analysis. The function first calculates a cubic grid of candidate voxels around the center point. It then filters this grid, keeping only the voxels whose Euclidean distance from the center (in millimeters) is less than or equal to the specified radius. Finally, it clips the list of voxels to ensure they are all within the bounds of the image volume. Input Argu
- **Arguments:**
  - `center_vox` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `radius_mm` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vox_dim` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vol_size` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
