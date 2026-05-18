- **Key Features:**
  - WHIFUN_QC_CSF_MASK_ALIGNMENT Generates a quality control figure for CSF mask alignment. WHIFUN_QC_CSF_MASK_ALIGNMENT(out_folder, func_image_path, CSF_mask_func_path, name, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates visual quality control reports to assess the alignment of the Cerebrospinal Fluid (CSF) mask with the functional data for a given subject. The function generates two types of plots: 1. **SPM Orthoslice Plot**: It uses SPM's `check_registration` to create a plot. The functional image is used as the underlay, and the CSF mask is used as the overlay. Th
  - Internal calls detected: `whifun_create_file`, `whifun_qc_coreg_orthoslice`, `whifun_qc_coreg_slover`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_csf_mask_alignment()`
- **Functional Purpose:** WHIFUN_QC_CSF_MASK_ALIGNMENT Generates a quality control figure for CSF mask alignment. WHIFUN_QC_CSF_MASK_ALIGNMENT(out_folder, func_image_path, CSF_mask_func_path, name, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates visual quality control reports to assess the alignment of the Cerebrospinal Fluid (CSF) mask with the functional data for a given subject. The function generates two types of plots: 1. **SPM Orthoslice Plot**: It uses SPM's `check_registration` to create a plot. The functional image is used as the underlay, and the CSF mask is used as the overlay. This provides a visual check of how well the CSF mask aligns with the brain ventricles in the function
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_mask_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
