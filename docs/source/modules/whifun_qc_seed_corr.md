# whifun_qc_seed_corr

Source: `whifun_functions/whifun_qc_seed_corr.m:1`

```matlab
function whifun_qc_seed_corr(out_folder,final_func_MNI,name,thresh,rad,slover_slices_mni,slover_view,over_write,func_mask_MNI)
```

## MATLAB Help

WHIFUN_QC_SEED_CORR Generates quality control images for seed-based functional connectivity.

  WHIFUN_QC_SEED_CORR(out_folder, final_func_MNI, name, thresh, rad, slover_slices_mni, slover_view, over_write, func_mask_MNI)
  creates a visual quality control report to assess the quality of a subject's
  functional data by performing a simple seed-to-voxel correlation.

  The function calculates the correlation map for three standard
  functional networks:
  1.  **Default Mode Network (DMN)**: Seeded in the left Posterior Cingulate Cortex (PCC).
  2.  **Visual Network**: Seeded in the right visual cortex.
  3.  **Auditory Network**: Seeded in the left auditory cortex.

  For each network, the function performs the following steps:
  -   **Checks Existence**: It checks if the output plot already exists and,
      based on the `over_write` flag, either skips or proceeds.
  -   **Calculates Correlation**: It calls `whifun_seed_corr_qc_plot` to
      calculate the seed-to-voxel correlation map and save the result.
  -   **Generates Plot**: It creates a SLover plot visualizing the
      correlation map, allowing for a visual assessment of the expected
      network activity. A healthy and clean dataset should show a
      well-defined network.

  This function is a valuable final check of the preprocessing pipeline,
  confirming that the data is clean and ready for functional connectivity
  analysis.

  Input Arguments:
  out_folder           - The root directory for saving all QC output.
  final_func_MNI       - The full path to the final normalized functional file.
  name                 - The subject's name.
  thresh               - A 1x2 vector with the negative and positive correlation thresholds.
  rad                  - The radius of the spherical seed in mm.
  slover_slices_mni    - A vector of slice locations for the SLover plot.
  slover_view          - The view to display slices in (e.g., 'axial').
  over_write           - A logical value (0 or 1) to force overwriting existing
                         QC images.
  func_mask_MNI        - (Optional) The path to the functional mask in MNI space.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, WHIFUN_SEED_CORR_QC_PLOT, MKDIR.
