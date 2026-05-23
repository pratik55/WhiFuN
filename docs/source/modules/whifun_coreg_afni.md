# whifun_coreg_afni

**Source:** `whifun_functions/whifun_coreg_afni.m:1`

## Signature

```matlab
function output = whifun_coreg_afni(now_anat_path,now_func_path)
```

## Summary

WHIFUN_COREG_AFNI Performs T2*-to-T1 coregistration using AFNI's `align_epi_anat.py` and cleans up intermediate files.

## Syntax

```matlab
OUTPUT = WHIFUN_COREG_AFNI(NOW_ANAT_PATH, NOW_FUNC_PATH)
```

## Description

This function executes a coregistration step, aligning the functional EPI image (T2*) to the anatomical image (T1) using the AFNI (Analysis of Functional NeuroImages) tool `align_epi_anat.py`. It is designed to be used within a MATLAB pipeline, capturing command line output and managing temporary files.

## Input Arguments

### `NOW_ANAT_PATH`
A structure array (e.g., from `dir` or custom function) pointing to the anatomical (T1) NIfTI file. Must contain fields `folder` and `name`.

### `NOW_FUNC_PATH`
A structure array (must contain one entry) pointing to the functional (EPI) NIfTI file. Must contain fields `folder` and `name`. The output coregistered functional image will replace this file (due to overwrite).

## Output Arguments

### `OUTPUT`
A string concatenating the command window output from both AFNI commands (`align_epi_anat.py` and `3dcopy`).

## Process Steps

1. Change directory to the functional data folder.
2. Execute `align_epi_anat.py` to calculate the transformation and apply
it to the EPI image, creating an AFNI-native file (e.g., `rc_*_al+orig.BRIK.gz`).

3. Execute `3dcopy` to convert the coregistered AFNI file back to the
original NIfTI filename, overwriting the original functional file.

4. Delete the temporary AFNI BRIK/HEAD files.

## Requirements

Requires the AFNI software suite to be installed and accessible from the system path.

## Author

Author: Pratik Jain
