# whifun_qc_global_ts

**Source:** `whifun_functions/whifun_qc_global_ts.m:1`

## Signature

```matlab
function whifun_qc_global_ts(out_folder,initial_func,final_func_MNI,motion_txt,func_mask_MNI,name,Reg_,over_write,csf_covariate_path,n_pca,pca_for_temp_reg)
```

## Summary

WHIFUN_QC_GLOBAL_TS Generates a quality control figure for global time series.

## Syntax

```matlab
WHIFUN_QC_GLOBAL_TS(out_folder, initial_func, final_func_MNI, motion_txt, func_mask_MNI, name, Reg_, over_write, csf_covariate_path, n_pca, pca_for_temp_reg)
```

## Description

creates a visual report to assess the quality of the mean global time series of a subject's functional data. The function plots the mean time series of the original and normalized data, as well as the head motion.

The function first checks if the output plot already exists and, based on the `over_write` flag, either skips or generates a new one. It then calls a helper function, `whifun_ts_check` (which is not provided in this file, but is assumed to handle the plotting logic), to generate a figure. This figure is designed to provide a comprehensive overview of the global signal before and after preprocessing, along with the nuisance regressors.

This function is useful for a final check to ensure that the global time series is stable and that normalization has not introduced any unexpected distortions.

## Input Arguments

### `out_folder`
The path to the quality control directory for saving the figure.

### `initial_func`
The full path to the initial functional file (after motion correction).

### `final_func_MNI`
The full path to the final normalized functional file.

### `motion_txt`
Path to the motion parameter `.txt` file.

### `func_mask_MNI`
Path to the functional mask in MNI space.

### `name`
The subject's name.

### `Reg_`
Logical flag for nuisance regression.

### `over_write`
A logical value (0 or 1) to force overwriting existing QC images.

### `csf_covariate_path`
(Optional) Path to the CSF time series `.mat` file.

### `n_pca`
(Optional) The number of PCA components used for regression.

### `pca_for_temp_reg`
(Optional) A logical flag to indicate if PCA was used. See also WHIFUN_CREATE_FILE, WHIFUN_TS_CHECK, MKDIR.

## Author

Author: Pratik Jain
