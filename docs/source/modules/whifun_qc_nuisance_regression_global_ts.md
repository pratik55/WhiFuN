# whifun_qc_nuisance_regression_global_ts

**Source:** `whifun_functions/whifun_qc_nuisance_regression_global_ts.m:1`

## Signature

```matlab
function whifun_qc_nuisance_regression_global_ts(out_folder,Subj_list_1,REG_CSF,motion_reg,pca_for_temp_reg,over_write,n_pca)
```

## Summary

WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS Generates a global time series QC plot for nuisance regression.

## Syntax

```matlab
WHIFUN_QC_NUISANCE_REGRESSION_GLOBAL_TS(...) creates a visual quality
```

## Description

control report to assess the effect of nuisance regression on the mean global signal of a functional scan.

The function performs the following steps:

1.  **Check Existence**: It checks if the output plot already exists and,
based on the `over_write` flag, either skips or generates a new one.

2.  **Data Loading**: It reads the functional data before and after
nuisance regression. It also loads the motion parameters and the CSF covariates (either PCA components or the mean time series).

3.  **Plotting**: It creates a single plot with three main components:
-   The mean global time series *before* regression (mean subtracted).
-   The mean global time series *after* regression (mean subtracted).
-   The CSF nuisance regressors themselves (either CSF PCA components or
mean CSF signal).

This plot provides a clear visual comparison of the functional data's global signal before and after the nuisance regression, allowing a user to see how much of the signal was explained by the regressors.

## Input Arguments

### `out_folder`
The path to the quality control directory for saving the figure.

### `Subj_list_1`
A single subject structure with relevant file paths and TR.

### `motion_reg`
A logical value (0 or 1) indicating if motion regressors were used during the pipeline run.

### `pca_for_temp_reg`
A logical value (0 or 1) indicating if PCA was used for the CSF regressors.

### `over_write`
A logical value (0 or 1) to force overwriting existing QC images.

### `n_pca`
The number of PCA components used (if applicable). See also WHIFUN_CREATE_FILE, WHIFUN_NIFTIREAD, ZSCORE, LOAD, PLOT, LEGEND, EXPORTGRAPHICS.

## Author

Author: Pratik Jain
