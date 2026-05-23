# whifun_skullstrip

Source: `whifun_functions/whifun_skullstrip.m:1`

```matlab
function output = whifun_skullstrip(m_file,now_anat_path,skull_pre)
```

## MATLAB Help

WHIFUN_SKULLSTRIP Performs SPM-based skull stripping using imcalc.

  output = WHIFUN_SKULLSTRIP(m_file, now_anat_path, skull_pre)
  creates a skull-stripped version of a bias-corrected anatomical image
  by using SPM's `imcalc` function.

  The function performs the following steps:
  1.  **Selects Inputs**: It takes the bias-corrected anatomical image (`m_file` , (`i1`))
      and the native-space segmented images for Gray Matter (`c1`), White
      Matter (`c2`), and CSF (`c3`) as input.
  2.  **Defines the Expression**: It applies a logical expression
      `i1.*((i2+i3+i4)>0.5)` to the input images. This expression performs an
      element-wise multiplication (`.*`) of the anatomical image (`i1`)
      with a binary mask. The mask is created by summing the segmented
      GM, WM, and CSF images (`i2+i3+i4`) and setting any voxel with a
      combined probability greater than 0.5 to 1, and others to 0. This
      effectively keeps only the brain tissue.
  3.  **Sets Output**: The output file is named with the specified prefix
      (`skull_pre`) and saved in the same directory as the input image.
  4.  **Runs Job**: The function executes the `imcalc` job through SPM's
      job manager, suppressing the GUI.

  Input Arguments:
  m_file        - A `dir` structure pointing to the bias-corrected anatomical file.
  now_anat_path - A `dir` structure pointing to the original anatomical file,
                  used for path and name information.
  skull_pre     - The prefix for the skull-stripped output file.

  Output Arguments:
  output - A string containing the log output from the SPM jobman.

  Author: Pratik Jain
  See also SPM_JOBMAN, FULLFILE, EVALC.
