# whifun_plot_data_check_figures

Source: `whifun_functions/whifun_plot_data_check_figures.m:1`

```matlab
function whifun_plot_data_check_figures(quality_control_path,n_image,tr,voxel_func,voxel_anat,mis_data)
```

## MATLAB Help

WHIFUN_PLOT_DATA_CHECK_FIGURES Generates and saves quality control figures
  summarizing scanning parameters (time points, TR, and voxel sizes) across
  all participants.

  WHIFUN_PLOT_DATA_CHECK_FIGURES(QUALITY_CONTROL_PATH, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA)

  This function creates two figures:
  1. Bar plots of scanning parameters for each participant.
  2. Histograms of scanning parameters to check for homogeneity across the group.

  Input Arguments:
  QUALITY_CONTROL_PATH - The directory where the output figures will be saved.
  N_IMAGE              - Vector containing the number of fMRI time points for each participant.
  TR                   - Vector containing the Repetition Time (TR) for each participant.
  VOXEL_FUNC           - Matrix (N_participants x 3) containing the voxel dimensions [x, y, z] for fMRI images.
  VOXEL_ANAT           - Matrix (N_participants x 3) containing the voxel dimensions [x, y, z] for structural images.
  MIS_DATA             - Logical flag (1 or 0) indicating whether any data was missing (used to add an annotation).

  Output:
  Saves two PNG files to the QUALITY_CONTROL_PATH:
  - 'Q1a_scanning_parameters.png' (Bar Plots)
  - 'Q1a_scanning_parameters_histogram.png' (Histograms)

  Author: Pratik Jain
