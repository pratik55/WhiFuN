# whifun_coreg

**Source:** `whifun_functions/whifun_coreg.m:1`

## Signature

```matlab
function output = whifun_coreg(now_anat_path,now_func_path,mean_func,nt)
```

## Summary

WHIFUN_COREG Performs coregistration using SPM.

## Description

aligns a subject's functional images to their anatomical image. This is a critical step in fMRI preprocessing to ensure that functional data can be accurately localized to anatomical structures.

The function configures and runs the SPM coregistration job. The anatomical image is set as the reference, and a mean functional image is set as the source. All functional volumes are included as "other" images, ensuring that the same transformation is applied to the entire time series.

Key parameters are set for the job:

- **Cost Function**: Normalized Mutual Information (`'nmi'`) is used to
find the optimal alignment.

- **Sampling and Smoothing**: The sampling separation and histogram
smoothing parameters are set to ensure an accurate and robust estimation.

The function suppresses the SPM GUI and returns the command-line output of the job.

## Input Arguments

### `now_anat_path`
A `dir` structure pointing to the anatomical file.

### `now_func_path`
A `dir` structure pointing to the functional file.

### `mean_func`
A `dir` structure pointing to the mean functional image.

### `nt`
The number of time points in the functional image series.

## Output Arguments

### `output`
A string containing the log output from the SPM jobman. See also SPM_JOBMAN, EVALC, FULLFILE.

## Author

Author: Pratik Jain

## Examples

```matlab
output = WHIFUN_COREG(now_anat_path, now_func_path, mean_func, nt)
```
