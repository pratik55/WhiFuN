- **Key Features:**
  - WHIFUN_QC_SMOOTH Generates a quality control image for spatial smoothing. WHIFUN_QC_SMOOTH(out_folder, func_image, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates a visual quality control report to assess the effect of spatial smoothing on a functional image. The function performs the following steps: 1. **File Management**: It checks for the existence of previous quality control images (both orthoslice and slover views). Based on the `over_write` flag, it determines whether to generate new plots. It also creates the necessary output directories if they don't exist.
  - Internal calls detected: `whifun_create_file`, `whifun_ortho_slover_single_image_save`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_smooth()`
- **Functional Purpose:** WHIFUN_QC_SMOOTH Generates a quality control image for spatial smoothing. WHIFUN_QC_SMOOTH(out_folder, func_image, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates a visual quality control report to assess the effect of spatial smoothing on a functional image. The function performs the following steps: 1. **File Management**: It checks for the existence of previous quality control images (both orthoslice and slover views). Based on the `over_write` flag, it determines whether to generate new plots. It also creates the necessary output directories if they don't exist. 2. **Plotting**: It calls a helper function, `whifun_ortho_slover_single_image_save`, to generate t
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_image` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
