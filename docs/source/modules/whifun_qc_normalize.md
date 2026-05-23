# whifun_qc_normalize

Source: `whifun_functions/whifun_qc_normalize.m:1`

```matlab
function whifun_qc_normalize(out_folder,Subj_list_1,template_path,slover_slices_mni,slover_contour_range_mni,slover_view,over_write)
```

## MATLAB Help

WHIFUN_QC_NORMALIZE Generates quality control figures for normalization.

  WHIFUN_QC_NORMALIZE(out_folder, Subj_list_1, template_path, slover_slices_mni, slover_contour_range_mni, slover_view, over_write)
  creates a visual report to assess the quality of spatial normalization.
  The function checks if the subject's functional data has been
  accurately warped into a standard template space (e.g., MNI).

  The function performs three main checks:
  1.  **Orthoslice Alignment**: It generates an SPM `check_registration`
      plot. It uses the first volume of the normalized functional image
      as the underlay and a standard MNI template as the overlay. This
      provides a quick visual check of the alignment.
  2.  **SLover Alignment**: It uses `whifun_qc_coreg_slover` to create a
      more detailed overlay plot, which provides a clear visualization of
      the normalized functional data on the MNI template.
  3.  **Voxel Time Series**: It generates a time series plot from a
      pre-existing function, `whifun_ts_qc`, to show the signal from
      different tissue types (GM, WM, CSF) and head motion. This confirms
      that the time series data remains consistent and is not distorted
      by the normalization process.

  This function is a critical final quality control step in the
  preprocessing pipeline. The `over_write` flag prevents redundant
  image generation.

  Input Arguments:
  out_folder             - The root directory for saving all QC output.
  Subj_list_1            - A single subject structure with `func_MNI`,
                           `motion_txt`, and MNI-space mask paths.
  template_path          - The full path to the MNI template file.
  slover_slices_mni      - A vector of slice locations for the SLover plot.
  slover_contour_range_mni- A two-element vector for the contour range.
  slover_view            - The view to display slices in (e.g., 'axial').
  over_write             - A logical value (0 or 1) to force overwriting.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, WHIFUN_QC_COREG_ORTHOSLICE, WHIFUN_QC_COREG_SLOVER, WHIFUN_TS_QC, MKDIR.
