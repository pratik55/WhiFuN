# whifun_create_seg_overlaps

Source: `whifun_functions/whifun_create_seg_overlaps.m:1`

```matlab
function whifun_create_seg_overlaps(GM_path,WM_path,CSF_path,ref,caption_1,caption_2)
```

## MATLAB Help

WHIFUN_CREATE_SEG_OVERLAPS Visualizes the overlap of Gray Matter (GM),
  White Matter (WM), and Cerebrospinal Fluid (CSF) segmentation masks onto
  a reference image using SPM's `spm_orthviews`.

  WHIFUN_CREATE_SEG_OVERLAPS(GM_PATH, WM_PATH, CSF_PATH, REF, CAPTION_1, CAPTION_2)

  This function is used for quality control (QC) in neuroimaging
  pipelines, allowing a visual check of the accuracy of tissue segmentation
  (e.g., from SPM's 'New Segment' or 'Segment' tools) by overlaying the
  masks in distinct colors onto a T1-weighted or normalized reference image.

  Input Arguments:
  GM_PATH   - Full path to the NIfTI file containing the Gray Matter segmentation mask (e.g., c1T1.nii).
  WM_PATH   - Full path to the NIfTI file containing the White Matter segmentation mask (e.g., c2T1.nii).
  CSF_PATH  - Full path to the NIfTI file containing the CSF segmentation mask (e.g., c3T1.nii).
  REF       - Full path to the NIfTI file to be used as the background reference image (e.g., T1.nii or rT1.nii).
  CAPTION_1 - Caption/Title for the first displayed image (usually the segmentation mask).
  CAPTION_2 - Caption/Title for the second displayed image (the reference image).

  Output:
  A SPM Graphics window displaying the reference image with the three tissue masks
  overlaid as color blobs: GM (Red), WM (Green), and CSF (Blue).

  Dependencies: Requires the SPM (Statistical Parametric Mapping) toolbox.
  - `spm_check_registration`, `spm_orthviews`, `spm_vol`.

  Author: Pratik Jain
