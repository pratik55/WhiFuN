# whifun_create_all_fn_image_montage

Source: `whifun_functions/whifun_create_all_fn_image_montage.m:1`

```matlab
function whifun_create_all_fn_image_montage(inputFolder, outputPrefix, tissueTypes)
```

## MATLAB Help

WHIFUN_CREATE_ALL_FN_IMAGE_MONTAGE Consolidates network views into a large grid.

  This function scans a folder for brain network visualizations (PNGs), 
  extracts their network IDs, and tiles them into a large canvas. Each row 
  represents a specific Functional Network (FN), and each column 
  represents a specific anatomical view (Left, Dorsal, Posterior).

  INPUTS:
      inputFolder  - String. Directory containing the individual network PNGs.
      outputPrefix - String. Filename prefix for the final montage (e.g., 'Group_ICA').
      tissueTypes  - Cell Array. e.g., {'WM', 'GM'} to process White and Grey matter.

  FILE NAMING CONVENTION EXPECTED:
      [Tissue]_FN_K[TotalNets]_[NetID]_[View].png
      Example: GM_FN_K17_5_left.png (Grey Matter, 17 total nets, Net #5, Left view).

  See also IMREAD, IMWRITE, REGEXP.
  Author: Pratik Jain
