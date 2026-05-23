# whifun_ts_check

**Source:** `whifun_functions/whifun_ts_check.m:1`

## Signature

```matlab
function whifun_ts_check(func_path_raw,func_path_pro,txt_path,in_func_mni_mask_path,out_image_path,Reg_,csf_covariate_path,n_pca,pca_for_temp_reg)
```

## Summary

WHIFUN_TS_CHECK Generates a comprehensive time series quality check figure.

## Syntax

```matlab
WHIFUN_TS_CHECK(func_path_raw, func_path_pro, txt_path, in_anat_mni_mask_path, out_func_mni_mask_path, out_image_path, Reg_, csf_covariate_path, n_pca, pca_for_temp_reg)
```

## Description

creates a multi-panel figure to visually inspect the effect of the preprocessing pipeline on a subject's functional time series. The function provides a detailed comparison of data quality before and after key preprocessing steps.

The function generates ten plots in a 2x5 grid:

- **Global Mean (Raw)**: The mean signal of the raw data.
- **Pairwise Variance (Raw)**: A measure of signal change between time points.
- **Rigid Body Motion**: The 6 head motion parameters.
- **Framewise Displacement (FD)**: A single metric summarizing motion.
- **CSF Time Series & Derivatives**: The CSF time series and its derivative, if regression was performed.
- **Global Mean (Preprocessed)**: The mean signal of the final processed data.
- **Pairwise Variance (Preprocessed)**: The signal change after processing.
- **Correlation Matrix (Raw)**: A correlation heatmap of raw data metrics.
- **Correlation Matrix (Derivatives)**: A correlation heatmap of derivative metrics.
This function is a powerful diagnostic tool, helping to confirm that nuisance signals have been effectively removed and that the preprocessing steps have not introduced new artifacts.

## Input Arguments

### `func_path_raw`
Path to the raw (realigned) functional file.

### `func_path_pro`
Path to the preprocessed functional file.

### `txt_path`
Path to the motion parameter `.txt` file.

### `in_anat_mni_mask_path`
Path to the anatomical brain mask in MNI space.

### `out_func_mni_mask_path`
Output path for the resliced functional mask.

### `out_image_path`
Path where the final QC image will be saved.

### `Reg_`
Logical flag for nuisance regression.

### `csf_covariate_path`
Path to the CSF time series `.mat` file.

### `n_pca`
Number of PCA components used for CSF regression.

### `pca_for_temp_reg`
Logical flag to indicate if PCA was used. See also NIFTIREAD, RESLICE_DATA, WHIFUN_CALCULATE_FD, CORR, IMAGESC, SUBPLOT.

## Author

Author: Pratik Jain, Xin Di
