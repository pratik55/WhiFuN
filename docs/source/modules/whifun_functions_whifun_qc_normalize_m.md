- **Key Features:**
  - WHIFUN_QC_NORMALIZE Generates quality control figures for normalization. WHIFUN_QC_NORMALIZE(out_folder, Subj_list_1, template_path, slover_slices_mni, slover_contour_range_mni, slover_view, over_write) creates a visual report to assess the quality of spatial normalization. The function checks if the subject's functional data has been accurately warped into a standard template space (e.g., MNI). The function performs three main checks: 1. **Orthoslice Alignment**: It generates an SPM `check_registration` plot. It uses the first volume of the normalized functional image as the underlay and a st
  - Internal calls detected: `whifun_create_file`, `whifun_qc_coreg_orthoslice`, `whifun_qc_coreg_slover`, `whifun_ts_mask_qc`, `whifun_ts_qc`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_normalize()`
- **Functional Purpose:** WHIFUN_QC_NORMALIZE Generates quality control figures for normalization. WHIFUN_QC_NORMALIZE(out_folder, Subj_list_1, template_path, slover_slices_mni, slover_contour_range_mni, slover_view, over_write) creates a visual report to assess the quality of spatial normalization. The function checks if the subject's functional data has been accurately warped into a standard template space (e.g., MNI). The function performs three main checks: 1. **Orthoslice Alignment**: It generates an SPM `check_registration` plot. It uses the first volume of the normalized functional image as the underlay and a standard MNI template as the overlay. This provides a quick visual check of the alignment. 2. **SLover
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `template_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
