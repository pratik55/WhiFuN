- **Key Features:**
  - WHIFUN_CREATE_BRAINNET_IMAGES Generates a series of PNG images for each network in a labeled NIfTI volume using the BrainNet Viewer toolbox. WHIFUN_CREATE_BRAINNET_IMAGES(OUT_PATH, ROI_PATH, OVER_WRITE) This function iterates through all unique network labels in the input ROI NIfTI file and creates a visualization of each network from multiple standard viewing angles using BrainNet Viewer. Input Arguments: OUT_PATH - The directory where the resulting PNG images will be saved. ROI_PATH - The full path to the input NIfTI file containing the labeled Functional Network (FN) map (e.g., 'WM_clusteri
  - Internal calls detected: `BrainNet_MapCfg_WhifuN`, `whifun_create_file`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, BrainNet Viewer

## Function: `whifun_create_brainnet_images()`
- **Functional Purpose:** WHIFUN_CREATE_BRAINNET_IMAGES Generates a series of PNG images for each network in a labeled NIfTI volume using the BrainNet Viewer toolbox. WHIFUN_CREATE_BRAINNET_IMAGES(OUT_PATH, ROI_PATH, OVER_WRITE) This function iterates through all unique network labels in the input ROI NIfTI file and creates a visualization of each network from multiple standard viewing angles using BrainNet Viewer. Input Arguments: OUT_PATH - The directory where the resulting PNG images will be saved. ROI_PATH - The full path to the input NIfTI file containing the labeled Functional Network (FN) map (e.g., 'WM_clustering_K10.nii'). OVER_WRITE - Flag (0 or 1). If 0, image generation will be skipped if the first output
- **Arguments:**
  - `out_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ROI_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
