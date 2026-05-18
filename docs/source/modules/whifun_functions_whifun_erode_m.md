- **Key Features:**
  - WHIFUN_ERODE Erodes a binary mask. out_mask_path = WHIFUN_ERODE(path_, num_erosions, out_pre) performs morphological erosion on a binary or probabilistic mask image. Erosion removes voxels from the boundary of a mask, making it smaller. This is often used to create a more central "deep" mask of a tissue type, for example, a deep white matter mask to avoid contamination from gray matter. The function performs the following steps: 1. **Read Image**: It reads the input NIfTI mask file. 2. **Erode**: It iteratively applies SPM's `spm_erode` function a specified number of times (`num_erosions`). 3.
  - Internal calls detected: `niftisave`
  - External dependencies detected: MATLAB NIfTI I/O, SPM12

## Function: `whifun_erode()`
- **Functional Purpose:** WHIFUN_ERODE Erodes a binary mask. out_mask_path = WHIFUN_ERODE(path_, num_erosions, out_pre) performs morphological erosion on a binary or probabilistic mask image. Erosion removes voxels from the boundary of a mask, making it smaller. This is often used to create a more central "deep" mask of a tissue type, for example, a deep white matter mask to avoid contamination from gray matter. The function performs the following steps: 1. **Read Image**: It reads the input NIfTI mask file. 2. **Erode**: It iteratively applies SPM's `spm_erode` function a specified number of times (`num_erosions`). 3. **Save Output**: The eroded mask is saved as a new NIfTI file with a name that includes the number
- **Arguments:**
  - `path_` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `num_erosions` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
