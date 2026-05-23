# whifun_fsl_fast_seg

Source: `whifun_functions/whifun_fsl_fast_seg.m:1`

```matlab
function [gm_prob_path, wm_prob_path, csf_prob_path,t1_input_brain] = whifun_fsl_fast_seg(t1_path, out_dir, do_skullstrip)
```

## MATLAB Help

WHIFUN_FSL_FAST_SEG Performs anatomical segmentation with optional skull stripping using FSL.

  [gm_prob_path, wm_prob_path, csf_prob_path] = WHIFUN_FSL_FAST_SEG(t1_path, out_dir, do_skullstrip)
  is a MATLAB wrapper function that automates the process of performing
  anatomical segmentation using FSL's `fast` tool. It also provides an
  option to run FSL's `bet` for skull stripping prior to segmentation.

  The function performs the following steps:
  1.  **Skull Stripping (optional)**: If `do_skullstrip` is true, it uses `bet`
      to remove non-brain tissue from the T1 image, saving a new file with
      `_brain` appended to its name.
  2.  **Segmentation**: It then runs `fast` on either the original T1
      image or the skull-stripped version to segment the brain into three
      tissue types: Gray Matter (GM), White Matter (WM), and Cerebrospinal
      Fluid (CSF).
  3.  **File Management**: It ensures the output directory exists and defines
      the expected output paths for the GM, WM, and CSF partial volume
      estimate files, which are saved in `nii.gz` format.

  Input Arguments:
  t1_path       - The full path to the input T1-weighted anatomical image.
  out_dir       - The path to the directory where the output segmentation
                  files will be saved.
  do_skullstrip - (Optional) A logical value. If true (default), it performs
                  skull stripping using `bet` before segmentation. If false,
                  it skips the skull stripping step.

  Output Arguments:
  gm_prob_path  - The full path to the Gray Matter partial volume estimate file.
  wm_prob_path  - The full path to the White Matter partial volume estimate file.
  csf_prob_path - The full path to the Cerebrospinal Fluid partial volume
                  estimate file.

  Note: This function requires FSL to be installed and correctly configured
        in the system's PATH.

  Author: Pratik Jain
  See also SYSTEM, FILEPARTS, MKDIR.
Default: skull strip
