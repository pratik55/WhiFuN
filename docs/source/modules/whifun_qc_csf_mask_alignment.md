# whifun_qc_csf_mask_alignment

Source: `whifun_functions/whifun_qc_csf_mask_alignment.m:1`

```matlab
function whifun_qc_csf_mask_alignment(out_folder,func_image_path,CSF_mask_func_path,name,slover_slices_ss,slover_contour_range_ss,slover_view,over_write)
```

## MATLAB Help

WHIFUN_QC_CSF_MASK_ALIGNMENT Generates a quality control figure for CSF mask alignment.

  WHIFUN_QC_CSF_MASK_ALIGNMENT(out_folder, func_image_path, CSF_mask_func_path, name, slover_slices_ss, slover_contour_range_ss, slover_view, over_write)
  creates visual quality control reports to assess the alignment of the
  Cerebrospinal Fluid (CSF) mask with the functional data for a given
  subject.

  The function generates two types of plots:
  1.  **SPM Orthoslice Plot**: It uses SPM's `check_registration` to create a
      plot. The functional image is used as the underlay, and the CSF mask
      is used as the overlay. This provides a visual check of how well the
      CSF mask aligns with the brain ventricles in the functional data.
  2.  **SLover Plot**: It uses `whifun_qc_coreg_slover` to create a
      specialized overlay plot, which provides an alternative and often
      clearer visualization of the alignment.

  This is a crucial quality control step, as an accurately aligned CSF mask
  is essential for effective nuisance regression. The `over_write` flag
  prevents redundant image generation.

  Input Arguments:
  out_folder             - The root directory for saving all QC output.
  func_image_path        - The full path to the functional image.
  CSF_mask_func_path     - The full path to the CSF mask in functional space.
  name                   - The subject's name.
  slover_slices_ss       - A vector of slice locations for the SLover plot.
  slover_contour_range_ss- A two-element vector for the contour range.
  slover_view            - The view to display slices in (e.g., 'axial').
  over_write             - A logical value (0 or 1) to force overwriting of
                           existing QC images.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, WHIFUN_QC_COREG_ORTHOSLICE, WHIFUN_QC_COREG_SLOVER.
