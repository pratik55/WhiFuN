- **Key Features:**
  - NIFTISAVE Saves a MATLAB array as a NIfTI-1 file, updating essential header information from a provided info structure. NIFTISAVE(NIFTIIMAGE, FILENAME, INFO, ADD_OFFSET, MULTI_SCALE) This is a utility wrapper for MATLAB's built-in `niftiwrite` function. It ensures that the NIfTI header information (INFO) is correctly updated to reflect the dimensions, datatype, and name of the image data being saved. Input Arguments: NIFTIIMAGE - The MATLAB array (2D, 3D, or 4D) containing the image data to be saved as a NIfTI file. FILENAME - The desired full path and filename (with extension, e.g., '.nii') f
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `niftisave()`
- **Functional Purpose:** NIFTISAVE Saves a MATLAB array as a NIfTI-1 file, updating essential header information from a provided info structure. NIFTISAVE(NIFTIIMAGE, FILENAME, INFO, ADD_OFFSET, MULTI_SCALE) This is a utility wrapper for MATLAB's built-in `niftiwrite` function. It ensures that the NIfTI header information (INFO) is correctly updated to reflect the dimensions, datatype, and name of the image data being saved. Input Arguments: NIFTIIMAGE - The MATLAB array (2D, 3D, or 4D) containing the image data to be saved as a NIfTI file. FILENAME - The desired full path and filename (with extension, e.g., '.nii') for the output NIfTI file. INFO - A structure, typically obtained from a previous `niftiread` call, c
- **Arguments:**
  - `niftiimage` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `info` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `add_offset` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `multi_scale` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
