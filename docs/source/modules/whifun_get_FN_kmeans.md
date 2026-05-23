# whifun_get_FN_kmeans

Source: `whifun_functions/whifun_get_FN_kmeans.m:1`

```matlab
function whifun_get_FN_kmeans(out_path,K,avg_vox_level_FC,WMmask_,header_file,num_replicates,over_write,d_flag,d,steps_,tot_steps)
```

## MATLAB Help

WHIFUN_GET_FN_KMEANS Performs k-means clustering on the Voxel-Level Functional
  Connectivity (FC) matrix to create a Functional Network (FN) map.

  WHIFUN_GET_FN_KMEANS(OUT_PATH, K, AVG_VOX_LEVEL_FC, WMMASK_, HEADER_FILE, OVER_WRITE, ...)

  This function takes a group-average FC matrix (where rows are voxels and
  columns are features) and clusters the voxels into K networks based on
  the correlation distance metric. The result is saved as a NIfTI volume.

  Input Arguments:
  OUT_PATH            - Full path to save the resulting FN NIfTI file (e.g., '.../WM_FN_K10.nii').
  K                   - The number of clusters (networks) to create. Can be a scalar or a vector
                        (though the provided loop suggests it only handles one K at a time).
  AVG_VOX_LEVEL_FC    - The group-average FC matrix (N_Voxels x N_Features) used as input for clustering.
  WMMASK_             - Input mask specifying voxel locations. Can be a file path (string/char),
                        a 3D numeric volume (mask), or a linear index vector.
  HEADER_FILE         - (Required if WMMASK_ is numeric) NIfTI header structure (from niftiinfo)
                        or a NIfTI volume used as template for the output image geometry.
  OVER_WRITE          - (Optional, default 0) Flag: 1 to overwrite existing output NIfTI file.
  D_FLAG, D, STEPS_, TOT_STEPS - (Optional) Parameters for progress dialogue box (GUI support).

  Output:
  Saves a NIfTI file at OUT_PATH containing the K-means cluster indices
  (1 to K) for the masked voxels.

  Dependencies: 'niftiread', 'niftiinfo', 'niftisave', 'whifun_create_file'.

  Author: Pratik Jain
