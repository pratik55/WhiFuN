# functional_connectivity

Source: `whifun_functions/functional_connectivity.m:1`

```matlab
function [vec,nan_sub] = functional_connectivity(reg_ts,Z,win,stride,nl)
```

## MATLAB Help

FUNCTIONAL_CONNECTIVITY Calculates Functional Connectivity (FC) from averaged ROI time series.

  [VEC, NAN_SUB] = FUNCTIONAL_CONNECTIVITY(REG_TS, Z, WIN, STRIDE, NL)

  Computes static or dynamic functional connectivity matrices (Pearson
  correlation or Non-linear Xi correlation) and returns the unique
  upper-triangle elements as a vector.

  Input Arguments:
  REG_TS   - Time series of the ROIs. Expected dimensions: T x ROI x Subj
             (Time points x Number of ROIs x Number of Subjects).
  Z        - (Optional, default 0) Flag for Fisher Z-transformation:
             Z = 1: Apply Fisher Z-transformation to Pearson correlation results.
             Z = 0: Do not apply transformation.
  WIN      - (Optional, default T) Window size for Dynamic Functional Connectivity (DFC).
             WIN = T calculates Static FC.
  STRIDE   - (Optional, default 1) Stride (step size) for sliding window in DFC.
  NL       - (Optional, default 0) Flag for Non-linear FC:
             NL = 1: Use Non-linear Xi correlation (requires xicor function).
             NL = 0: Use Pearson correlation (default).

  Output Arguments:
  VEC      - The vectorized upper-triangle of the FC matrices.
             - Static FC (NL=0, WIN=T): (ROI*(ROI-1)/2) x N_Subj
             - Dynamic FC (NL=0, WIN<T): (ROI*(ROI-1)/2) x N_Windows x N_Subj
             - Non-linear FC (NL=1): (ROI*(ROI-1)/2) x N_Subj (Static only)
  NAN_SUB  - A vector of subject indices for which NaN values were detected
             in the computed FC matrices (due to low-variance or missing data).

  Dependencies:
  - corrvec: Function to extract the unique upper-triangle elements of a matrix.
  - xicor: Function to compute the Non-linear Xi correlation (if NL=1).

  Author: Pratik Jain
