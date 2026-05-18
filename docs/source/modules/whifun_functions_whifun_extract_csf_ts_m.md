- **Key Features:**
  - WHIFUN_EXTRACT_CSF_TS Extracts the CSF time series from a functional scan. WHIFUN_EXTRACT_CSF_TS(in_csf_mask_func_path, now_func_path, pca_for_temp_reg, n_pca) extracts the time series of all voxels within a Cerebrospinal Fluid (CSF) mask from a functional neuroimaging data file. The function first reads the binary CSF mask and the functional data. It then reshapes both to a voxel x time points matrix to efficiently extract all the CSF time series. The function handles two methods for summarizing the time series: 1. **Principal Component Analysis (PCA)**: If `pca_for_temp_reg` is true, the fun
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O, Statistics and Machine Learning Toolbox, SPM12

## Function: `whifun_extract_csf_ts()`
- **Functional Purpose:** WHIFUN_EXTRACT_CSF_TS Extracts the CSF time series from a functional scan. WHIFUN_EXTRACT_CSF_TS(in_csf_mask_func_path, now_func_path, pca_for_temp_reg, n_pca) extracts the time series of all voxels within a Cerebrospinal Fluid (CSF) mask from a functional neuroimaging data file. The function first reads the binary CSF mask and the functional data. It then reshapes both to a voxel x time points matrix to efficiently extract all the CSF time series. The function handles two methods for summarizing the time series: 1. **Principal Component Analysis (PCA)**: If `pca_for_temp_reg` is true, the function performs PCA on the CSF time series and saves the first `n_pca` principal components. This is
- **Arguments:**
  - `in_csf_mask_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `now_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `pca_for_temp_reg` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n_pca` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
