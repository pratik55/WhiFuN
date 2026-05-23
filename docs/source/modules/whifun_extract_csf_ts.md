# whifun_extract_csf_ts

**Source:** `whifun_functions/whifun_extract_csf_ts.m:1`

## Signature

```matlab
function whifun_extract_csf_ts(in_csf_mask_func_path,now_func_path,pca_for_temp_reg,n_pca)
```

## Summary

WHIFUN_EXTRACT_CSF_TS Extracts the CSF time series from a functional scan.

## Syntax

```matlab
WHIFUN_EXTRACT_CSF_TS(in_csf_mask_func_path, now_func_path, pca_for_temp_reg, n_pca)
```

## Description

extracts the time series of all voxels within a Cerebrospinal Fluid (CSF) mask from a functional neuroimaging data file.

The function first reads the binary CSF mask and the functional data. It then reshapes both to a voxel x time points matrix to efficiently extract all the CSF time series. The function handles two methods for summarizing the time series:

1.  **Principal Component Analysis (PCA)**: If `pca_for_temp_reg` is true,
the function performs PCA on the CSF time series and saves the first `n_pca` principal components. This is a common method for reducing the dimensionality of the nuisance signal.

2.  **Mean Time Series**: If `pca_for_temp_reg` is false, the function
calculates the mean time series across all CSF voxels.

The extracted time series (either the PCA components or the mean) is saved to a `.mat` file in the same directory as the functional data. The function includes a check to handle cases where the CSF mask is empty, throwing a clear error to the user.

## Input Arguments

### `in_csf_mask_func_path`
The full path to the CSF binary mask file.

### `now_func_path`
A `dir` structure pointing to the functional file.

### `pca_for_temp_reg`
A logical value (0 or 1). If 1, PCA is performed.

### `n_pca`
The number of principal components to extract if `pca_for_temp_reg` is
1. See also SPM_VOL, SPM_READ_VOLS, NIFTIREAD, RESHAPE, PCA.

## Author

Author: Pratik Jain
