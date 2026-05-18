- **Key Features:**
  - WHIFUN_QC_INITIAL_ALIGN_CHECK Creates quality control images for initial data alignment. WHIFUN_QC_INITIAL_ALIGN_CHECK(out_folder, template_path, Subj_list_1, slover_slices, slover_contour_range, slover_view, over_write) generates visual quality control reports to assess the initial alignment of a subject's functional and anatomical data to a standard MNI template. The function performs two main tasks: 1. **Anatomical Alignment Check**: It creates QC images comparing the subject's anatomical file to an MNI template. 2. **Functional Alignment Check**: It creates QC images comparing the first vo
  - Internal calls detected: `whifun_create_file`, `whifun_multiple_file_found`, `whifun_qc_coreg_orthoslice`, `whifun_qc_coreg_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_initial_align_check()`
- **Functional Purpose:** WHIFUN_QC_INITIAL_ALIGN_CHECK Creates quality control images for initial data alignment. WHIFUN_QC_INITIAL_ALIGN_CHECK(out_folder, template_path, Subj_list_1, slover_slices, slover_contour_range, slover_view, over_write) generates visual quality control reports to assess the initial alignment of a subject's functional and anatomical data to a standard MNI template. The function performs two main tasks: 1. **Anatomical Alignment Check**: It creates QC images comparing the subject's anatomical file to an MNI template. 2. **Functional Alignment Check**: It creates QC images comparing the first volume of the subject's functional file to the same MNI template. For each alignment check, a helper f
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `template_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `store_ortho_slover_images()`
- **Functional Purpose:** WHIFUN_QC_INITIAL_ALIGN_CHECK Creates quality control images for initial data alignment. WHIFUN_QC_INITIAL_ALIGN_CHECK(out_folder, template_path, Subj_list_1, slover_slices, slover_contour_range, slover_view, over_write) generates visual quality control reports to assess the initial alignment of a subject's functional and anatomical data to a standard MNI template. The function performs two main tasks: 1. **Anatomical Alignment Check**: It creates QC images comparing the subject's anatomical file to an MNI template. 2. **Functional Alignment Check**: It creates QC images comparing the first vo
- **Arguments:**
  - `image_1_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `image_2_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_ortho_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_slover_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
