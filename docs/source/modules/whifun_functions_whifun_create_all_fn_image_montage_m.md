- **Key Features:**
  - WHIFUN_CREATE_ALL_FN_IMAGE_MONTAGE Consolidates network views into a large grid. This function scans a folder for brain network visualizations (PNGs), extracts their network IDs, and tiles them into a large canvas. Each row represents a specific Functional Network (FN), and each column represents a specific anatomical view (Left, Dorsal, Posterior). INPUTS: inputFolder - String. Directory containing the individual network PNGs. outputPrefix - String. Filename prefix for the final montage (e.g., 'Group_ICA'). tissueTypes - Cell Array. e.g., {'WM', 'GM'} to process White and Grey matter. FILE NA
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_create_all_fn_image_montage()`
- **Functional Purpose:** WHIFUN_CREATE_ALL_FN_IMAGE_MONTAGE Consolidates network views into a large grid. This function scans a folder for brain network visualizations (PNGs), extracts their network IDs, and tiles them into a large canvas. Each row represents a specific Functional Network (FN), and each column represents a specific anatomical view (Left, Dorsal, Posterior). INPUTS: inputFolder - String. Directory containing the individual network PNGs. outputPrefix - String. Filename prefix for the final montage (e.g., 'Group_ICA'). tissueTypes - Cell Array. e.g., {'WM', 'GM'} to process White and Grey matter. FILE NAMING CONVENTION EXPECTED: [Tissue]_FN_K[TotalNets]_[NetID]_[View].png Example: GM_FN_K17_5_left.png
- **Arguments:**
  - `inputFolder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `outputPrefix` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tissueTypes` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
