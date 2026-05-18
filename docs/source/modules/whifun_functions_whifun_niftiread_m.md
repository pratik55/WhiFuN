- **Key Features:**
  - WHIFUN_NIFTIREAD Reads a NIfTI file and applies scaling factors. [volume, info] = WHIFUN_NIFTIREAD(image_path) reads a NIfTI file, correctly applying the stored scaling and offset values from the file's header. This is a crucial step for ensuring that the voxel intensity values are interpreted correctly, as many NIfTI files store data as integers to save space and require a scaling factor to be applied for the correct floating-point representation. The function first reads the volume data and the header information using MATLAB's built-in `niftiread` and `niftiinfo` functions. It then applies 
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_niftiread()`
- **Functional Purpose:** WHIFUN_NIFTIREAD Reads a NIfTI file and applies scaling factors. [volume, info] = WHIFUN_NIFTIREAD(image_path) reads a NIfTI file, correctly applying the stored scaling and offset values from the file's header. This is a crucial step for ensuring that the voxel intensity values are interpreted correctly, as many NIfTI files store data as integers to save space and require a scaling factor to be applied for the correct floating-point representation. The function first reads the volume data and the header information using MATLAB's built-in `niftiread` and `niftiinfo` functions. It then applies the formula: `y = AdditiveOffset + x * MultiplicativeScaling`, where `x` is the raw data and `y` is
- **Arguments:**
  - `image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
