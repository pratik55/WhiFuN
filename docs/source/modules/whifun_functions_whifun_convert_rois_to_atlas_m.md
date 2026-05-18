- **Key Features:**
  - WHIFUN_CONVERT_ROIS_TO_ATLAS Combines multiple binary NIfTI ROI masks into a single labeled NIfTI atlas volume. WHIFUN_CONVERT_ROIS_TO_ATLAS(FOLDER_PATH, PATTERN, OUT_FOLDER) This function reads a collection of NIfTI files, where each file represents a binary Region of Interest (ROI) mask. It then assigns a unique integer label to the voxels belonging to each ROI and saves the result as a single NIfTI atlas file. Input Arguments: FOLDER_PATH - Full path to the directory containing the NIfTI ROI mask files. PATTERN - (Optional, default '') A wildcard pattern (e.g., '*.nii' or 'ROI_*.nii') to ma
  - Internal calls detected: `niftisave`
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_convert_ROIs_to_atlas()`
- **Functional Purpose:** WHIFUN_CONVERT_ROIS_TO_ATLAS Combines multiple binary NIfTI ROI masks into a single labeled NIfTI atlas volume. WHIFUN_CONVERT_ROIS_TO_ATLAS(FOLDER_PATH, PATTERN, OUT_FOLDER) This function reads a collection of NIfTI files, where each file represents a binary Region of Interest (ROI) mask. It then assigns a unique integer label to the voxels belonging to each ROI and saves the result as a single NIfTI atlas file. Input Arguments: FOLDER_PATH - Full path to the directory containing the NIfTI ROI mask files. PATTERN - (Optional, default '') A wildcard pattern (e.g., '*.nii' or 'ROI_*.nii') to match the files to be included as ROIs. If empty, all files in the folder are considered. OUT_FOLDER -
- **Arguments:**
  - `folder_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `pattern` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
