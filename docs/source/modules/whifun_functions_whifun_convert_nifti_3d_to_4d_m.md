- **Key Features:**
  - WHIFUN_CONVERT_NIFTI_3D_TO_4D Combines a series of 3D NIfTI volumes into a single 4D NIfTI file (e.g., creating a functional time series from individual 3D volumes). A = WHIFUN_CONVERT_NIFTI_3D_TO_4D(FOLDER, FILTER, TR, OUT_FILENAME, ATLAS) This function is useful for aggregating individual 3D image acquisitions (e.g., single time points from a scanner) into the standard 4D time series format. Input Arguments: FOLDER - The directory path containing the 3D NIfTI files. FILTER - The common filename pattern (wildcard) to match the 3D NIfTI files (e.g., 'f*.nii'). TR - The Temporal Resolution (Rep
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_convert_nifti_3d_to_4d()`
- **Functional Purpose:** WHIFUN_CONVERT_NIFTI_3D_TO_4D Combines a series of 3D NIfTI volumes into a single 4D NIfTI file (e.g., creating a functional time series from individual 3D volumes). A = WHIFUN_CONVERT_NIFTI_3D_TO_4D(FOLDER, FILTER, TR, OUT_FILENAME, ATLAS) This function is useful for aggregating individual 3D image acquisitions (e.g., single time points from a scanner) into the standard 4D time series format. Input Arguments: FOLDER - The directory path containing the 3D NIfTI files. FILTER - The common filename pattern (wildcard) to match the 3D NIfTI files (e.g., 'f*.nii'). TR - The Temporal Resolution (Repetition Time) in seconds. This value is written to the 4th dimension of the NIfTI header's PixelDime
- **Arguments:**
  - `folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `TR` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `atlas` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
