# whifun_coreg_preproc

Source: `whifun_functions/whifun_coreg_preproc.m:1`

```matlab
function Subj_list_1  = whifun_coreg_preproc(quality_control_path,Subj_list_1,in_func_path_bef,in_func_path_after,in_anat_path,log_fileID,over_write,no_mean_func)
```

## MATLAB Help

WHIFUN_COREG_PREPROC Orchestrates SPM-based anatomical-functional coregistration.

  Subj_list_1 = WHIFUN_COREG_PREPROC(quality_control_path, ..., over_write)
  is a high-level function that manages the coregistration step of a
  neuroimaging preprocessing pipeline. Coregistration is the process of
  aligning a subject's functional scans to their high-resolution
  anatomical scan.

  The function first checks if a coregistration has already been performed
  by comparing the transformation matrices of the input and image before realigned
  functional files. If they are different or `over_write` is enabled, it
  proceeds. The function then calls `whifun_coreg` to perform the actual
  SPM coregistration job. The new file paths are implicitly handled by SPM.
  The process output is logged to a specified file.

  In case of an error, the function catches the exception, updates the
  subject's `error` flag, and logs the detailed error information to a file.

  Input Arguments:
  quality_control_path - Path to the quality control directory for logs.
  Subj_list_1          - A single subject structure to be updated.
  in_func_path_bef     - Path to the functional file *before* coregistration.
  in_func_path_after   - Path to the functional file *after* coregistration.
  in_anat_path         - Path to the anatomical file.
  log_fileID           - File ID of the log file for writing process output.
  over_write           - A logical value (0 or 1) to force overwriting.

  Output Arguments:
  Subj_list_1 - The updated subject structure, showing any errors found using the error flag.

  Author: Pratik Jain
  See also WHIFUN_COREG, NIFTIINFO, TRY, CATCH.
