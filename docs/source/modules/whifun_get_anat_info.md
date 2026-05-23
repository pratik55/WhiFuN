# whifun_get_anat_info

Source: `whifun_functions/whifun_get_anat_info.m:1`

```matlab
function [Subj_list_1,voxel_anat] = whifun_get_anat_info(now_anat_path,Subj_list_1,output_folder)
```

## MATLAB Help

WHIFUN_GET_ANAT_INFO Extracts information from an anatomical NIfTI file.

  [Subj_list_1, voxel_anat] = WHIFUN_GET_ANAT_INFO(now_anat_path, Subj_list_1)
  reads metadata from an anatomical neuroimaging NIfTI file specified by
  `now_anat_path`. The function updates a subject structure with the
  extracted information and returns the voxel dimensions.

  This function is a core part of a neuroimaging pipeline, as it retrieves
  critical anatomical parameters (like voxel size) that are essential for
  subsequent preprocessing steps such as coregistration and normalization.
  It handles cases where metadata might be corrupted or missing.

  Input Arguments:
  now_anat_path - A `dir` structure (from a call to `dir`) pointing to
                  the anatomical NIfTI file.
  Subj_list_1   - A single subject structure, which will be updated
                  with the file information.

  Output Arguments:
  Subj_list_1  - The updated subject structure, now containing fields for
                 the anatomical file path, name, and dimensions (`x_Anat`,
                 `y_Anat`, `z_Anat`).
  voxel_anat   - A 1x3 array of the anatomical data's voxel dimensions [x, y, z].

  Author: Pratik Jain
  See also NIFTIINFO, FULLFILE, DISP.
