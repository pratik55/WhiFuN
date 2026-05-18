- **Key Features:**
  - WHIFUN_BUILD_NET Manages the decision process for building Functional Networks (FNs). [BUILD_NET, K] = WHIFUN_BUILD_NET(CLUSTER_FOLDER, OUT_PATTERN, OVER_WRITE) This function checks if previously clustered FN files exist in the specified folder. If files are found, it prompts the user to either rebuild the networks or select an existing cluster solution (K value) to proceed with. Input Arguments: CLUSTER_FOLDER - Full path to the directory where FN cluster results are stored. OUT_PATTERN - The filename pattern used for the clustered NIfTI files (e.g., 'WM_FN_K*.nii', where * is the K value). O
  - Internal calls detected: `whifun_create_file`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_build_net()`
- **Functional Purpose:** WHIFUN_BUILD_NET Manages the decision process for building Functional Networks (FNs). [BUILD_NET, K] = WHIFUN_BUILD_NET(CLUSTER_FOLDER, OUT_PATTERN, OVER_WRITE) This function checks if previously clustered FN files exist in the specified folder. If files are found, it prompts the user to either rebuild the networks or select an existing cluster solution (K value) to proceed with. Input Arguments: CLUSTER_FOLDER - Full path to the directory where FN cluster results are stored. OUT_PATTERN - The filename pattern used for the clustered NIfTI files (e.g., 'WM_FN_K*.nii', where * is the K value). OVER_WRITE - (Optional, default 0) Flag to bypass prompts if set to 1. Output Arguments: BUILD_NET -
- **Arguments:**
  - `cluster_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_pattern` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
