- **Key Features:**
  - WHIFUN_QC_COREG_SLOVER Creates a quality control image using SLover. WHIFUN_QC_COREG_SLOVER(image_1_path, image_2_path, out_image_path, slover_slices, slover_contour_range, slover_view) generates a quality control image to visually inspect the alignment of two neuroimaging files, using a specialized function (`whifun_slover`) for creating overlaid slices. This function is an alternative to `spm_check_registration` for creating a quality control image. It sets up an invisible SPM figure, calls a helper function (`whifun_slover`) to perform the visualization with specific parameters, and then ex
  - Internal calls detected: `whifun_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_coreg_slover()`
- **Functional Purpose:** WHIFUN_QC_COREG_SLOVER Creates a quality control image using SLover. WHIFUN_QC_COREG_SLOVER(image_1_path, image_2_path, out_image_path, slover_slices, slover_contour_range, slover_view) generates a quality control image to visually inspect the alignment of two neuroimaging files, using a specialized function (`whifun_slover`) for creating overlaid slices. This function is an alternative to `spm_check_registration` for creating a quality control image. It sets up an invisible SPM figure, calls a helper function (`whifun_slover`) to perform the visualization with specific parameters, and then exports the resulting figure to a file. The visual output will show one image (e.g., anatomical) as a
- **Arguments:**
  - `image_1_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `image_2_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
