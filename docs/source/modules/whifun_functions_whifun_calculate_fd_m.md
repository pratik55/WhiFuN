- **Key Features:**
  - WHIFUN_CALCULATE_FD Calculates framewise displacement (FD). fd = WHIFUN_CALCULATE_FD(motion) computes the framewise displacement (FD) from motion parameters. FD is a measure of head motion between consecutive time points in an fMRI scan. This function takes either the path to a motion parameter text file (as a string or `dir` structure) or the motion parameters directly (as a numeric matrix). It then calculates the vector difference between each time point. The rotational parameters are converted to millimeters by assuming a brain radius of 50mm, and the absolute sum of all six derivative para
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB table/file I/O

## Function: `whifun_calculate_fd()`
- **Functional Purpose:** WHIFUN_CALCULATE_FD Calculates framewise displacement (FD). fd = WHIFUN_CALCULATE_FD(motion) computes the framewise displacement (FD) from motion parameters. FD is a measure of head motion between consecutive time points in an fMRI scan. This function takes either the path to a motion parameter text file (as a string or `dir` structure) or the motion parameters directly (as a numeric matrix). It then calculates the vector difference between each time point. The rotational parameters are converted to millimeters by assuming a brain radius of 50mm, and the absolute sum of all six derivative parameters is returned as the FD time series. This function is a core part of quality control for fMRI d
- **Arguments:**
  - `motion` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
