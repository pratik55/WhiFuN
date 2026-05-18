- **Key Features:**
  - WHIFUN_GET_FN_KMEANS Performs k-means clustering on the Voxel-Level Functional Connectivity (FC) matrix to create a Functional Network (FN) map. WHIFUN_GET_FN_KMEANS(OUT_PATH, K, AVG_VOX_LEVEL_FC, WMMASK_, HEADER_FILE, OVER_WRITE, ...) This function takes a group-average FC matrix (where rows are voxels and columns are features) and clusters the voxels into K networks based on the correlation distance metric. The result is saved as a NIfTI volume. Input Arguments: OUT_PATH - Full path to save the resulting FN NIfTI file (e.g., '.../WM_FN_K10.nii'). K - The number of clusters (networks) to crea
  - Internal calls detected: `niftisave`, `whifun_create_file`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_get_FN_kmeans()`
- **Functional Purpose:** WHIFUN_GET_FN_KMEANS Performs k-means clustering on the Voxel-Level Functional Connectivity (FC) matrix to create a Functional Network (FN) map. WHIFUN_GET_FN_KMEANS(OUT_PATH, K, AVG_VOX_LEVEL_FC, WMMASK_, HEADER_FILE, OVER_WRITE, ...) This function takes a group-average FC matrix (where rows are voxels and columns are features) and clusters the voxels into K networks based on the correlation distance metric. The result is saved as a NIfTI volume. Input Arguments: OUT_PATH - Full path to save the resulting FN NIfTI file (e.g., '.../WM_FN_K10.nii'). K - The number of clusters (networks) to create. Can be a scalar or a vector (though the provided loop suggests it only handles one K at a time).
- **Arguments:**
  - `out_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `K` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `avg_vox_level_FC` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WMmask_` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `header_file` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `num_replicates` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
