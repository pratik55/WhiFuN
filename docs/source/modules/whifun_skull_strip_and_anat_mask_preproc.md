# whifun_skull_strip_and_anat_mask_preproc

Source: `whifun_functions/whifun_skull_strip_and_anat_mask_preproc.m:1`

```matlab
function [Subj_list_1,out_ss_path,out_anat_mask_native_path] = whifun_skull_strip_and_anat_mask_preproc(quality_control_path,Subj_list_1,in_anat_path,skull_pre,GM_native,WM_native,CSF_native,log_fileID,over_write)
```

## MATLAB Help

WHIFUN_SKULL_STRIP_AND_ANAT_MASK_PREPROC Performs skull stripping and anatomical mask creation.

  [Subj_list_1, out_ss_path, out_anat_mask_subj_space_path, out_wanat_mask_MNI_path] = whifun_skull_strip_and_anat_mask_preproc(...)
  is a high-level function that manages three key preprocessing steps for
  anatomical data: skull stripping and creating a brain mask in native space,

  The function first checks for the input anatomical file and resolves
  ambiguities. It then performs the following steps, each with an
  overwriting check:
  1.  **Skull Stripping**: Calls `whifun_skullstrip` to remove non-brain tissue
      from the bias-corrected anatomical image.
  2.  **Anatomical Mask (Native Space)**: Calls `whifun_anat_mask` to
      create a brain mask from the segmented tissue images (GM, WM, CSF)
      in the subject's native space.

  The function updates the subject structure with the paths to all the
  generated files and logs the output of each step to a file. In case of
  an error, it catches the exception, updates the subject's error flag,
  and logs the detailed error information.

  Input Arguments:
  quality_control_path - Path to the quality control directory for logs.
  Subj_list_1          - A single subject structure to be updated.
  in_anat_path         - The path to the input anatomical NIfTI file.
  skull_pre            - The prefix for the skull-stripped output file.
  log_fileID           - File ID of the log file for writing process output.
  over_write           - A logical value (0 or 1) to force overwriting.

  Output Arguments:
  Subj_list_1                   - The updated subject structure.
  out_ss_path                   - Full path to the skull-stripped file.
  out_anat_mask_subj_space_path - Full path to the brain mask in native space.

  Author: Pratik Jain
  See also WHIFUN_MULTIPLE_FILE_FOUND, WHIFUN_CREATE_FILE, WHIFUN_SKULLSTRIP, WHIFUN_ANAT_MASK.
