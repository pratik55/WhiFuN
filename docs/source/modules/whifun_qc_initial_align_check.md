# whifun_qc_initial_align_check

Source: `whifun_functions/whifun_qc_initial_align_check.m:1`

```matlab
function whifun_qc_initial_align_check(out_folder,template_path,Subj_list_1,slover_slices,slover_contour_range,slover_view,over_write)
```

## MATLAB Help

WHIFUN_QC_INITIAL_ALIGN_CHECK Creates quality control images for initial data alignment.

  WHIFUN_QC_INITIAL_ALIGN_CHECK(out_folder, template_path, Subj_list_1, slover_slices, slover_contour_range, slover_view, over_write)
  generates visual quality control reports to assess the initial alignment
  of a subject's functional and anatomical data to a standard MNI template.

  The function performs two main tasks:
  1.  **Anatomical Alignment Check**: It creates QC images comparing the
      subject's anatomical file to an MNI template.
  2.  **Functional Alignment Check**: It creates QC images comparing the
      first volume of the subject's functional file to the same MNI template.

  For each alignment check, a helper function `store_ortho_slover_images`
  is called to generate two types of plots:
  -   **Orthoslice View**: A standard SPM `spm_check_registration` plot.
  -   **SLover View**: A specialized overlay plot using `whifun_qc_coreg_slover`.

  This function is a crucial early-stage quality control step to ensure that
  the data has the expected orientation and is a good starting point for
  subsequent processing steps like coregistration. The `over_write` flag
  prevents redundant image generation.

  Input Arguments:
  out_folder           - The root directory for saving all QC output.
  template_path        - The full path to the MNI template file.
  Subj_list_1          - A single subject structure.
  slover_slices        - A vector of slice locations to display.
  slover_contour_range - A two-element vector for contour range.
  slover_view          - The view to display slices in (e.g., 'axial').
  over_write           - (Optional) A logical value (0 or 1) to force
                         overwriting of existing QC images. Defaults to 0.

  Author: Pratik Jain
  See also WHIFUN_MULTIPLE_FILE_FOUND, WHIFUN_CREATE_FILE, WHIFUN_QC_COREG_ORTHOSLICE, WHIFUN_QC_COREG_SLOVER.
