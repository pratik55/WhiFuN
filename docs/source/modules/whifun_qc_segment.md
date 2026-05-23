# whifun_qc_segment

Source: `whifun_functions/whifun_qc_segment.m:1`

```matlab
function whifun_qc_segment(out_folder,name,ref,GM_path,WM_path,CSF_path,slover_slices,slover_contour_range,slover_view,space_name,over_write)
```

## MATLAB Help

WHIFUN_QC_SEGMENT Generates quality control images for anatomical segmentation.

  WHIFUN_QC_SEGMENT(...) creates a visual report to assess the quality of
  the anatomical image segmentation. The function can generate two types of
  reports, one in the subject's native space and one in MNI space, depending
  on the input paths.

  The function performs the following steps:
  1.  **SPM Orthoslice Plot**: It creates a plot showing a reference image
      (`ref`) with overlaid contours of the segmented Gray Matter (GM),
      White Matter (WM), and Cerebrospinal Fluid (CSF). This provides a
      visual check of how well the segmentation process worked.
  2.  **SLover Plot**: It uses `whifun_slover` to display the segmented
      tissue maps in color on a black background, providing a clearer
      view of the segmentation results.
  3.  **File Management**: It checks if the output plots already exist
      and, based on the `over_write` flag, either skips or generates new ones.
      It also creates the necessary output directories.

  This function is essential for verifying that the SPM segmentation step
  has accurately classified the different tissue types.

  Input Arguments:
  out_folder           - Path to the root QC directory.
  name                 - The subject's name.
  ref                  - Path to the reference anatomical image .
  GM_path              - Path to the Gray Matter segmented file.
  WM_path              - Path to the White Matter segmented file.
  CSF_path             - Path to the CSF segmented file.
  slover_slices        - Slices for the SLover plot.
  slover_contour_range - Contour range for the SLover plot.
  slover_view          - The view to display slices in (e.g., 'axial').
  space_name           - The name of the space ('Subject' or 'MNI').
  over_write           - Logical flag to overwrite existing images.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, WHIFUN_CREATE_SEG_OVERLAPS, WHIFUN_SLOVER, MKDIR.
