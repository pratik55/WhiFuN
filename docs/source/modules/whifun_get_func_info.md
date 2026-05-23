# whifun_get_func_info

Source: `whifun_functions/whifun_get_func_info.m:2`

```matlab
function [Subj_list_1,voxel_func,n_image] = whifun_get_func_info(now_func_path,Subj_list_1,output_folder)
```

## MATLAB Help

WHIFUN_GET_FUNC_INFO Extracts information from a functional NIfTI file.

  [Subj_list_1, voxel_func, n_image] = WHIFUN_GET_FUNC_INFO(now_func_path, Subj_list_1)
  reads metadata from a functional neuroimaging NIfTI file specified by
  `now_func_path`. The function updates a subject structure with the
  extracted information and returns the voxel dimensions and number of
  time points.

  This is a core function in a neuroimaging pipeline, as it retrieves
  critical parameters (like voxel size and number of volumes) that are
  essential for subsequent preprocessing steps. It handles cases where
  metadata might be corrupted or missing.

  Input Arguments:
  now_func_path - A `dir` structure (from a call to `dir`) pointing to
                  the functional NIfTI file.
  Subj_list_1   - A single subject structure, which will be updated
                  with the file information.

  Output Arguments:
  Subj_list_1  - The updated subject structure, now containing fields for
                 the functional file path, name, dimensions (`x_func`, `y_func`,
                 `z_func`), and number of time points (`nt`).
  voxel_func   - A 1x3 array of the functional data's voxel dimensions [x, y, z].
  n_image      - The number of images (time points) in the functional file.

  Author: Pratik Jain
  See also NIFTIINFO, FULLFILE, DISP.
