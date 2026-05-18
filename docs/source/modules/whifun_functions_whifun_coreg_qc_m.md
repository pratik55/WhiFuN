- **Key Features:**
  - WHIFUN_COREG_QC Generates automated QC images for Coregistration. Author: Pratik Jain This function creates two types of visual checks: 1. Orthoslice View: A standard SPM-style three-pane check with contours. 2. Slice View: A detailed multi-slice layout using the 'slover' engine. INPUTS: name_ - String. Subject ID or session name. now_anat_path - Struct. Anatomical file info (from dir()). now_func_path - Struct. Functional file info (from dir()). slover_slices - Vector. Indices of slices to display. slover_contour_range - Vector. Range for contour levels (e.g., [0.5 0.5]). slover_view - String
  - Internal calls detected: `spm_check_registration_evalc`, `whifun_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_coreg_qc()`
- **Functional Purpose:** WHIFUN_COREG_QC Generates automated QC images for Coregistration. Author: Pratik Jain This function creates two types of visual checks: 1. Orthoslice View: A standard SPM-style three-pane check with contours. 2. Slice View: A detailed multi-slice layout using the 'slover' engine. INPUTS: name_ - String. Subject ID or session name. now_anat_path - Struct. Anatomical file info (from dir()). now_func_path - Struct. Functional file info (from dir()). slover_slices - Vector. Indices of slices to display. slover_contour_range - Vector. Range for contour levels (e.g., [0.5 0.5]). slover_view - String. 'axial', 'sagittal', or 'coronal'. ss - Boolean. Space toggle (1 = Subject, 0 = MNI). quality_cont
- **Arguments:**
  - `name_` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `now_anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `now_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ss` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `quality_control_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
