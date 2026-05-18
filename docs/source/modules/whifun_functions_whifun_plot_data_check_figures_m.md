- **Key Features:**
  - WHIFUN_PLOT_DATA_CHECK_FIGURES Generates and saves quality control figures summarizing scanning parameters (time points, TR, and voxel sizes) across all participants. WHIFUN_PLOT_DATA_CHECK_FIGURES(QUALITY_CONTROL_PATH, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA) This function creates two figures: 1. Bar plots of scanning parameters for each participant. 2. Histograms of scanning parameters to check for homogeneity across the group. Input Arguments: QUALITY_CONTROL_PATH - The directory where the output figures will be saved. N_IMAGE - Vector containing the number of fMRI time points for eac
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: ANTs command-line suite

## Function: `whifun_plot_data_check_figures()`
- **Functional Purpose:** WHIFUN_PLOT_DATA_CHECK_FIGURES Generates and saves quality control figures summarizing scanning parameters (time points, TR, and voxel sizes) across all participants. WHIFUN_PLOT_DATA_CHECK_FIGURES(QUALITY_CONTROL_PATH, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA) This function creates two figures: 1. Bar plots of scanning parameters for each participant. 2. Histograms of scanning parameters to check for homogeneity across the group. Input Arguments: QUALITY_CONTROL_PATH - The directory where the output figures will be saved. N_IMAGE - Vector containing the number of fMRI time points for each participant. TR - Vector containing the Repetition Time (TR) for each participant. VOXEL_FUNC - Ma
- **Arguments:**
  - `quality_control_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_image` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tr` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `voxel_func` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `voxel_anat` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mis_data` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
