- **Key Features:**
  - WHIFUN_SHOW_SLICES_MULTIOVERLAY Display multiple slices (one per image) in a montage with overlay support. Inputs: volumes - cell array of file paths or 3D matrices overlay_types - cell array: {'structure','contour',...} cmaps - cell array of colormaps for each image slices - array of slice indices (one per image) orientation - 'axial' | 'sagittal' | 'coronal' Example: vols = {'sub1.nii','sub2.nii','sub3.nii'}; types = {'structure','contour','structure'}; cmaps = {hot, lines, gray}; slices = [40 45 50]; whifun_show_slices_multioverlay(vols, types, cmaps, slices, 'axial'); --- Input checks ---
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O, Image Processing Toolbox

## Function: `whifun_show_slices_multioverlay()`
- **Functional Purpose:** WHIFUN_SHOW_SLICES_MULTIOVERLAY Display multiple slices (one per image) in a montage with overlay support. Inputs: volumes - cell array of file paths or 3D matrices overlay_types - cell array: {'structure','contour',...} cmaps - cell array of colormaps for each image slices - array of slice indices (one per image) orientation - 'axial' | 'sagittal' | 'coronal' Example: vols = {'sub1.nii','sub2.nii','sub3.nii'}; types = {'structure','contour','structure'}; cmaps = {hot, lines, gray}; slices = [40 45 50]; whifun_show_slices_multioverlay(vols, types, cmaps, slices, 'axial'); --- Input checks ---
- **Arguments:**
  - `volumes` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `overlay_types` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `cmaps` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `orientation` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `capitalize()`
- **Functional Purpose:** WHIFUN_SHOW_SLICES_MULTIOVERLAY Display multiple slices (one per image) in a montage with overlay support. Inputs: volumes - cell array of file paths or 3D matrices overlay_types - cell array: {'structure','contour',...} cmaps - cell array of colormaps for each image slices - array of slice indices (one per image) orientation - 'axial' | 'sagittal' | 'coronal' Example: vols = {'sub1.nii','sub2.nii','sub3.nii'}; types = {'structure','contour','structure'}; cmaps = {hot, lines, gray}; slices = [40 45 50]; whifun_show_slices_multioverlay(vols, types, cmaps, slices, 'axial'); --- Input checks ---
- **Arguments:**
  - `str` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
