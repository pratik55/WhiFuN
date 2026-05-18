- **Key Features:**
  - WHIFUN_SEPERATE_LEFT_RIGHT Separates a Functional Network (FN) NIfTI volume into left and right hemispheric components based on the mid-sagittal slice. WHIFUN_SEPERATE_LEFT_RIGHT(FN_FILE_PATH, ONE_IMAGE) This utility function is used to create separate NIfTI files for the left (L) and right (R) halves of a clustered network map (e.g., WM-FN). Input Arguments: FN_FILE_PATH - Full path to the NIfTI file containing the clustered Functional Network. (e.g., 'WM_FN_K10.nii'). ONE_IMAGE - (Optional, default 0) Flag to determine output format: ONE_IMAGE = 0: Saves two separate NIfTI files: '_L' and '_
  - Internal calls detected: `niftisave`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_seperate_left_right()`
- **Functional Purpose:** WHIFUN_SEPERATE_LEFT_RIGHT Separates a Functional Network (FN) NIfTI volume into left and right hemispheric components based on the mid-sagittal slice. WHIFUN_SEPERATE_LEFT_RIGHT(FN_FILE_PATH, ONE_IMAGE) This utility function is used to create separate NIfTI files for the left (L) and right (R) halves of a clustered network map (e.g., WM-FN). Input Arguments: FN_FILE_PATH - Full path to the NIfTI file containing the clustered Functional Network. (e.g., 'WM_FN_K10.nii'). ONE_IMAGE - (Optional, default 0) Flag to determine output format: ONE_IMAGE = 0: Saves two separate NIfTI files: '_L' and '_R'. ONE_IMAGE = 1: Saves a single NIfTI file '_L_R_seperated' where the right hemisphere's network l
- **Arguments:**
  - `FN_file_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `one_image` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
