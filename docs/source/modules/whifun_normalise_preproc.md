# whifun_normalise_preproc

Source: `whifun_functions/whifun_normalise_preproc.m:1`

```matlab
function [Subj_list_1,out_func_path,out_anat_path] = whifun_normalise_preproc(quality_control_path,Subj_list_1,in_func_path,in_anat_path,in_def_path,vox,Norm_pre,GM_path,WM_path,CSF_path,log_fileID,over_write)
```

## MATLAB Help

WHIFUN_NORMALISE_PREPROC Orchestrates normalization to MNI space.

  [Subj_list_1, out_func_path, out_anat_path] = WHIFUN_NORMALISE_PREPROC(...)
  is a high-level function that manages the spatial normalization step of
  a neuroimaging preprocessing pipeline. It applies a previously calculated
  deformation field (from the segmentation step) to both functional and
  anatomical images, transforming them from the subject's native space
  to a standard template space (MNI).

  The function performs the normalization in two separate steps:
  1.  **Functional Normalization**: It checks for an existing normalized
      functional file and, based on the `over_write` flag, either skips
      or calls `whifun_normalise` to perform the transformation.
  2.  **Anatomical Normalization**: Similarly, it checks for an existing
      normalized anatomical file and performs the normalization if needed.

  For each step, the function logs the process output to a file and updates
  the subject structure with the path to the newly created files. In case
  of an error during either normalization process, it catches the exception,
  updates the subject's `error` flag, and logs the detailed error
  information to a file.

  Input Arguments:
  quality_control_path - Path to the quality control directory for logs.
  Subj_list_1          - A single subject structure to be updated.
  in_func_path         - The path to the input functional file.
  in_anat_path         - The path to the input anatomical file.
  in_def_path          - The path to the deformation field file (`y_...nii`).
  vox                  - The voxel size for the normalized output.
  Norm_pre             - The prefix for the output normalized files (e.g., 'w').
  log_fileID           - File ID of the log file.
  over_write           - A logical value (0 or 1) to force overwriting.

  Output Arguments:
  Subj_list_1   - The updated subject structure, with `func_MNI` and `anat_MNI` paths.
  out_func_path - The full path to the normalized functional file.
  out_anat_path - The full path to the normalized anatomical file.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, WHIFUN_NORMALISE, TRY, CATCH.
