- **Key Features:**
  - WHIFUN_TS_MASK_QC Generates quality control images for tissue masks. WHIFUN_TS_MASK_QC(output_path, GM_mask_path, WM_mask_path, deep_WM_mask_path, CSF_mask_path, func_path, name, slover_slices, slover_contour_range, slover_view) creates a visual report to assess the quality and alignment of multiple brain tissue masks. This is a crucial step for verifying that the masks used to extract time series data are accurate. The function generates two types of plots: 1. **SPM Orthoslice Plot**: A plot showing the functional image as the underlay, with overlaid contours of the GM, WM, deep WM, and CSF m
  - Internal calls detected: `whifun_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers, Shell/system execution

## Function: `whifun_ts_mask_qc()`
- **Functional Purpose:** WHIFUN_TS_MASK_QC Generates quality control images for tissue masks. WHIFUN_TS_MASK_QC(output_path, GM_mask_path, WM_mask_path, deep_WM_mask_path, CSF_mask_path, func_path, name, slover_slices, slover_contour_range, slover_view) creates a visual report to assess the quality and alignment of multiple brain tissue masks. This is a crucial step for verifying that the masks used to extract time series data are accurate. The function generates two types of plots: 1. **SPM Orthoslice Plot**: A plot showing the functional image as the underlay, with overlaid contours of the GM, WM, deep WM, and CSF masks. Each tissue type is displayed in a different color (GM-red, WM-green, deep WM-yellow, CSF-blue
- **Arguments:**
  - `output_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `deep_WM_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
