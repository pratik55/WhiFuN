# whifun_multiOverlay

Source: `whifun_functions/whifun_multiOverlay.m:1`

```matlab
function whifun_multiOverlay(volumes, overlayTypes, colormaps, slices, sliceType)
```

## MATLAB Help

WHIFUN_MULTIOVERLAY Displays a montage of structural MRI slices with contour overlays.

  WHIFUN_MULTIOVERLAY(volumes, overlayTypes, colormaps, slices, sliceType)
  extracts specified slices along a given anatomical plane, processes structural 
  backgrounds, computes edge contours for overlays, and bundles them into a 
  clean, multi-slice RGB montage figure.

  Processing Details:
      - Automatically loads NIfTI file paths or handles pre-loaded 3D/4D arrays.
      - Truncates 4D volumes to their first frame automatically.
      - Uses a Canny edge detector to extract contour overlays.
      - Requires exactly one volume designated as 'Structural' to serve as the background.

  Inputs:
      volumes      - A single string/char path, numeric array, or a cell array 
                     containing a mix of file paths and 3D/4D matrices.
      overlayTypes - Cell array of strings corresponding to each item in 'volumes'.
                     Supported types:
                       'Structural' - Used as the grayscale background slice.
                       'contours'   - Edge detected and blended onto the background.
      colormaps    - Cell array of strings or function handles specifying colormaps 
                     for each volume (e.g., {'gray', 'hot'}). The last color 
                     of the contour's colormap is used for its edge color.
      slices       - Vector of integers denoting the slice numbers to display.
      sliceType    - String specifying the viewing plane. Options are:
                     'axial', 'coronal', or 'sagittal'.

  Outputs:
      Generates a standard MATLAB figure containing the tiled slice montage.

  Example:
      vols     = {'C:\Data\T1.nii', 'C:\Data\LesionMask.nii'};
      types    = {'Structural', 'contours'};
      cmaps    = {'gray', 'hot'};
      sliceVec = [45, 50, 55, 60];
      whifun_multiOverlay(vols, types, cmaps, sliceVec, 'axial');
  Author: Pratik Jain
