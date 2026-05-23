# whifun_seed_corr_qc_plot

Source: `whifun_functions/whifun_seed_corr_qc_plot.m:1`

```matlab
function whifun_seed_corr_qc_plot(output_path,func_path,seed,rad,seed_cor_output_path,thresh,slover_slices_mni,slover_view,mask)
```

## MATLAB Help

WHIFUN_SEED_CORR_QC_PLOT Computes seed-based functional connectivity (FC)
  and generates a quality control (QC) visualization using the Slover tool.

  WHIFUN_SEED_CORR_QC_PLOT(OUTPUT_PATH, FUNC_PATH, SEED, RAD, SEED_COR_OUTPUT_PATH, THRESH, SLICES_MNI, VIEW, MASK)

  This function first calculates the seed-to-voxel correlation map for a
  given seed location. It then creates two temporary thresholded versions
  of the correlation map and visualizes them simultaneously using Slover
  (e.g., one for positive correlation, one for negative) on top of the
  structural image for QC purposes. The temporary files are deleted after
  plotting.

  Input Arguments:
  OUTPUT_PATH          - Full path to save the final QC plot graphic (e.g., PNG).
  FUNC_PATH            - Full path to the 4D functional NIfTI file.
  SEED                 - 1x3 vector of MNI coordinates [x, y, z] for the seed center.
  RAD                  - Radius (in mm) of the spherical seed region.
  SEED_COR_OUTPUT_PATH - Full path to save the unthresholded seed correlation NIfTI map.
  THRESH               - 1x2 vector [thresh_neg, thresh_pos] for negative and positive
                         correlation thresholds (e.g., [-0.3, 0.3]).
  SLOVER_SLICES_MNI    - Vector of slice coordinates or method for Slover visualization (e.g., [4, 8, 12]).
  SLOVER_VIEW          - String defining the view for Slover (e.g., 'axial').
  MASK                 - (Optional) Full path to a NIfTI mask file to constrain the correlation analysis.

  Dependencies: 'whifun_seed_corr', 'spm_figure', 'whifun_slover'.

  Author: Pratik Jain
