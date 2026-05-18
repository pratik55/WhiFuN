- **Key Features:**
  - WHIFUN_QC_COREG Generates quality control images for coregistration. WHIFUN_QC_COREG(out_folder, func_image_path, anat_image_path, name, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates visual quality control reports to assess the alignment of a subject's functional data to their anatomical data after coregistration. The function generates two types of plots to check the alignment: 1. **SPM Orthoslice Plot**: It calls `whifun_qc_coreg_orthoslice` to generate a plot using SPM's `check_registration`. The skull-stripped anatomical image is used as the underlay, and the 
  - Internal calls detected: `whifun_create_file`, `whifun_qc_coreg_orthoslice`, `whifun_qc_coreg_slover`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_coreg()`
- **Functional Purpose:** WHIFUN_QC_COREG Generates quality control images for coregistration. WHIFUN_QC_COREG(out_folder, func_image_path, anat_image_path, name, slover_slices_ss, slover_contour_range_ss, slover_view, over_write) creates visual quality control reports to assess the alignment of a subject's functional data to their anatomical data after coregistration. The function generates two types of plots to check the alignment: 1. **SPM Orthoslice Plot**: It calls `whifun_qc_coreg_orthoslice` to generate a plot using SPM's `check_registration`. The skull-stripped anatomical image is used as the underlay, and the first volume of the realigned functional image is used as an overlay. This plot allows for a quick v
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range_ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
