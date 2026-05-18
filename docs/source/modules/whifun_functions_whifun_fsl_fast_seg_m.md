- **Key Features:**
  - WHIFUN_FSL_FAST_SEG Performs anatomical segmentation with optional skull stripping using FSL. [gm_prob_path, wm_prob_path, csf_prob_path] = WHIFUN_FSL_FAST_SEG(t1_path, out_dir, do_skullstrip) is a MATLAB wrapper function that automates the process of performing anatomical segmentation using FSL's `fast` tool. It also provides an option to run FSL's `bet` for skull stripping prior to segmentation. The function performs the following steps: 1. **Skull Stripping (optional)**: If `do_skullstrip` is true, it uses `bet` to remove non-brain tissue from the T1 image, saving a new file with `_brain` a
  - Internal calls detected: `niftisave`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, FSL command-line suite, Shell/system execution

## Function: `whifun_fsl_fast_seg()`
- **Functional Purpose:** WHIFUN_FSL_FAST_SEG Performs anatomical segmentation with optional skull stripping using FSL. [gm_prob_path, wm_prob_path, csf_prob_path] = WHIFUN_FSL_FAST_SEG(t1_path, out_dir, do_skullstrip) is a MATLAB wrapper function that automates the process of performing anatomical segmentation using FSL's `fast` tool. It also provides an option to run FSL's `bet` for skull stripping prior to segmentation. The function performs the following steps: 1. **Skull Stripping (optional)**: If `do_skullstrip` is true, it uses `bet` to remove non-brain tissue from the T1 image, saving a new file with `_brain` appended to its name. 2. **Segmentation**: It then runs `fast` on either the original T1 image or the
- **Arguments:**
  - `t1_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_dir` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `do_skullstrip` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
