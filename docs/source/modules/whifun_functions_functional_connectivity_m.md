- **Key Features:**
  - FUNCTIONAL_CONNECTIVITY Calculates Functional Connectivity (FC) from averaged ROI time series. [VEC, NAN_SUB] = FUNCTIONAL_CONNECTIVITY(REG_TS, Z, WIN, STRIDE, NL) Computes static or dynamic functional connectivity matrices (Pearson correlation or Non-linear Xi correlation) and returns the unique upper-triangle elements as a vector. Input Arguments: REG_TS - Time series of the ROIs. Expected dimensions: T x ROI x Subj (Time points x Number of ROIs x Number of Subjects). Z - (Optional, default 0) Flag for Fisher Z-transformation: Z = 1: Apply Fisher Z-transformation to Pearson correlation resul
  - Internal calls detected: `corrvec`
  - External dependencies detected: Statistics and Machine Learning Toolbox, Parallel Computing Toolbox

## Function: `functional_connectivity()`
- **Functional Purpose:** FUNCTIONAL_CONNECTIVITY Calculates Functional Connectivity (FC) from averaged ROI time series. [VEC, NAN_SUB] = FUNCTIONAL_CONNECTIVITY(REG_TS, Z, WIN, STRIDE, NL) Computes static or dynamic functional connectivity matrices (Pearson correlation or Non-linear Xi correlation) and returns the unique upper-triangle elements as a vector. Input Arguments: REG_TS - Time series of the ROIs. Expected dimensions: T x ROI x Subj (Time points x Number of ROIs x Number of Subjects). Z - (Optional, default 0) Flag for Fisher Z-transformation: Z = 1: Apply Fisher Z-transformation to Pearson correlation results. Z = 0: Do not apply transformation. WIN - (Optional, default T) Window size for Dynamic Function
- **Arguments:**
  - `reg_ts` (numeric time-series matrix, commonly T x R, V x T, or T x R x S): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Z` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `win` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `stride` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `nl` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
