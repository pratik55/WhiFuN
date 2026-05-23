# whifun_slover

Source: `whifun_functions/whifun_slover.m:1`

```matlab
function obj = whifun_slover(imgs,itype,cmap,slices,cnt_range,img_view,wt,fg,cbar_)
```

## MATLAB Help

WHIFUN_SLOVER A wrapper function around the core 'slover' visualization engine,
  customized for WhiFuN's needs, particularly for image overlays and
  segmentation QC displays.

  OBJ = WHIFUN_SLOVER(IMGS, ITYPE, CMAP, SLICES, CNT_RANGE, IMG_VIEW, WT, FG, CBAR_)

  This function initializes and configures a 'slover' object to display
  multiple NIfTI images with custom colormaps, slices, and views, and then
  calls a drawing function (whifun_paint) to render the output.

  Input Arguments:
  IMGS            - Cell array of full paths to NIfTI files to be displayed.
  ITYPE           - Cell array of strings defining the image type for each image
                    (e.g., 'Structural', 'Blobs', 'Truecolour', 'Contours', etc.).
  CMAP            - Cell array of colormap matrices (e.g., {gray, hot, winter}) for each image.
  SLICES          - Vector of slice coordinates to display (e.g., -20:5:60).
  CNT_RANGE       - Vector [min_val max_val] defining the display/threshold range for
                    overlay images (Blobs, Contours).
  IMG_VIEW        - String defining the slice view ('axial', 'coronal', 'sagittal').
  WT              - (Optional) Vector of display weights/proportions for each image
                    when multiple images are set as 'truecolour' (e.g., for blending).
  FG              - (Optional) Handle of the figure window to draw the visualization into.
  CBAR_           - (Optional, default 0) Flag: 1 to force a colorbar for all images, 0 otherwise.

  Output Arguments:
  OBJ             - The configured 'slover' object structure after visualization.

  Dependencies: 'slover' (assumed external/SPM related), 'spm_vol', 'spm_figure',
                'spm_orthviews', 'whifun_paint' (assumed external/custom).

  Author: Pratik Jain
