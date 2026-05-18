- **Key Features:**
  - WHIFUN_QC_FINAL_FUNC_MNI Generates final quality control figures for normalized data. WHIFUN_QC_FINAL_FUNC_MNI(out_folder, final_func_MNI, GM_MNI, ..., over_write) creates a suite of visual quality control reports to assess the final preprocessed functional data after it has been normalized to MNI space. The function performs three main checks: 1. **Orthoslice Alignment**: It generates an SPM `check_registration` plot comparing the first volume of the normalized functional image to a standard MNI template. 2. **SLover Alignment**: It uses `whifun_qc_coreg_slover` to create a more detailed over
  - Internal calls detected: `whifun_create_file`, `whifun_qc_coreg_orthoslice`, `whifun_qc_coreg_slover`, `whifun_ts_mask_qc`, `whifun_ts_qc`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_final_func_MNI()`
- **Functional Purpose:** WHIFUN_QC_FINAL_FUNC_MNI Generates final quality control figures for normalized data. WHIFUN_QC_FINAL_FUNC_MNI(out_folder, final_func_MNI, GM_MNI, ..., over_write) creates a suite of visual quality control reports to assess the final preprocessed functional data after it has been normalized to MNI space. The function performs three main checks: 1. **Orthoslice Alignment**: It generates an SPM `check_registration` plot comparing the first volume of the normalized functional image to a standard MNI template. 2. **SLover Alignment**: It uses `whifun_qc_coreg_slover` to create a more detailed overlay plot, which provides a clear visualization of the normalized functional data on the MNI template
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `final_func_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `template_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `motion_txt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
