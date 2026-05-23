# whifun_create_brainnet_images

Source: `whifun_functions/whifun_create_brainnet_images.m:1`

```matlab
function whifun_create_brainnet_images(out_path,ROI_path,over_write)
```

## MATLAB Help

WHIFUN_CREATE_BRAINNET_IMAGES Generates a series of PNG images for each
  network in a labeled NIfTI volume using the BrainNet Viewer toolbox.

  WHIFUN_CREATE_BRAINNET_IMAGES(OUT_PATH, ROI_PATH, OVER_WRITE)

  This function iterates through all unique network labels in the input ROI
  NIfTI file and creates a visualization of each network from multiple
  standard viewing angles using BrainNet Viewer.

  Input Arguments:
  OUT_PATH    - The directory where the resulting PNG images will be saved.
  ROI_PATH    - The full path to the input NIfTI file containing the labeled
                Functional Network (FN) map (e.g., 'WM_clustering_K10.nii').
  OVER_WRITE  - Flag (0 or 1). If 0, image generation will be skipped if
                the first output file already exists.

  Output:
  A set of PNG files saved to OUT_PATH, named in the format:
  `<ROI_name>_<Network_Label>_<View_Name>.png`

  Dependencies:
  - MATLAB's `mfilename`, `fileparts`, `addpath`.
  - Custom functions: `whifun_niftiread`, `whifun_create_file`.
  - External tool: `BrainNet_MapCfg_WhifuN`.

  Assumptions:
  - The BrainNet Viewer toolbox folder structure is located at:
    `fileparts(fileparts(mfilename('fullpath'))) / BrainNetViewer_20191031`

  Author: Pratik Jain
