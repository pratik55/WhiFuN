# whifun_regress_any

**Source:** `whifun_functions/whifun_regress_any.m:1`

## Signature

```matlab
function func_mask_path = whifun_regress_any(in_func_path,in_anat_mask,confounds_matrix,out_func_path)
```

## Summary

WHIFUN_REGRESS_ANY Performs voxel-wise nuisance regression on a 4D NIfTI.

## Syntax

```matlab
FUNC_MASK_PATH = WHIFUN_REGRESS_ANY(IN_FUNC_PATH, IN_ANAT_MASK, ...
```

## Description

CONFOUNDS_MATRIX, OUT_FUNC_PATH) reads a functional NIfTI file, removes signals defined in the confounds matrix using linear regression, adds the mean signal back, and saves the result.

## Input Arguments

### `in_func_path`
String. Path to the input 4D functional NIfTI.

### `in_anat_mask`
String. Path to the anatomical mask NIfTI.

### `confounds_matrix`
Matrix (T x N). Nuisance regressors (e.g., motion parameters, CSF signal) where T matches the number of timepoints.

### `out_func_path`
String. Path where the regressed NIfTI will be saved.

## Output Arguments

### `func_mask_path`
String. Path to the generated functional mask. NOTES:
- The confounds are z-scored before regression.
- The mean image is added back to the residuals to maintain the original signal's baseline intensity.
- The output is re-scaled to match the original NIfTI's MultiplicativeScaling and AdditiveOffset. See also REGRESS, ZSCORE, WHIFUN_NIFTIREAD.
