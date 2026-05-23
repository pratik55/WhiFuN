# whifun_segment

Source: `whifun_functions/whifun_segment.m:1`

```matlab
function output = whifun_segment(now_anat_path,spm_path)
```

## MATLAB Help

WHIFUN_SEGMENT Performs SPM-based segmentation and normalization.

  output = WHIFUN_SEGMENT(now_anat_path, spm_path) runs the SPM
  segmentation and normalization routine on a subject's anatomical image.

  This function configures and executes the `spm_jobman` for the
  `spm.spatial.preproc` module. The batch job is set up to:
  - **Bias Correct** the anatomical image and save the output.
  - **Segment** the image into six tissue types (Gray Matter, White Matter,
    CSF, skull, etc.) using the default Tissue Probability Map (TPM).
  - **Save** the native-space and MNI-normalized versions of the GM, WM, and
    CSF segments.
  - **Save** the forward and inverse deformation field maps, which are
    essential for normalizing other images (like functional data).
  - **Suppress** the SPM GUI for silent execution.

  This function is a core step in many preprocessing pipelines, as it
  generates the files needed for coregistration and normalization.

  Input Arguments:
  now_anat_path - A `dir` structure pointing to the anatomical NIfTI file.
  spm_path      - The path to the SPM installation directory.

  Output Arguments:
  output - A string containing the log output from the SPM jobman.

  Author: Pratik Jain
  See also SPM_JOBMAN, NIFTIINFO, FULLFILE, EVALC.
