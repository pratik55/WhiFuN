# whifun_regress

**Source:** `whifun_functions/whifun_regress.m:1`

## Signature

```matlab
function func_mask_path = whifun_regress(in_func_path,in_anat_mask_subj_space_path,in_csf_mat_path,in_motion_txt_path,out_func_path,n_pca)
```

## Summary

WHIFUN_REGRESS Performs nuisance regression on functional data.

## Description

nuisance regression on a functional neuroimaging time series. This process removes signals from non-neuronal sources, such as head motion and physiological noise.

The function first loads the functional data and creates a brain mask by reslicing an anatomical mask into functional space. It then constructs a design matrix (`b_init`) of nuisance regressors, which can include:

- **CSF Signal**: Loaded from `in_csf_mat_path`. The signal can be either
the mean CSF time series or a set of PCA components.

- **Motion Parameters**: Loaded from `in_motion_txt_path`. If `motion_reg`
is true, it includes the 6 rigid body motion parameters, their squares, and their first derivatives and squared derivatives (a total of 24 regressors, often referred to as "Friston-24").

Finally, the function performs a voxel-wise linear regression. For each voxel, the nuisance regressors are fit to the time series, and the residuals (the signal that is not explained by the regressors) are saved. The mean of the original time series is added back to preserve signal magnitude.

## Input Arguments

### `in_func_path`
The path to the input functional file.

### `in_anat_mask_subj_space_path`
Path to the anatomical brain mask in subject space.

### `in_csf_mat_path`
Path to the `.mat` file containing the CSF time series.

### `in_motion_txt_path`
Path to the motion parameter `.txt` file.

### `out_func_path`
The desired path for the output regressed file.

### `motion_reg`
A logical value (0 or 1) to include motion parameters as regressors.

### `n_pca`
The number of PCA components for CSF regression.

## Output Arguments

### `func_mask_path`
The path to the created functional mask. See also WHIFUN_CREATE_REST_MASK, NIFTIINFO, NIFTIREAD, NIFTISAVE, REGRESS.

## Author

Author: Pratik Jain

## Examples

```matlab
func_mask_path = WHIFUN_REGRESS(in_func_path, ..., n_pca) performs
```
