- **Key Features:**
  - WHIFUN_QC_COREG_ORTHOSLICE Creates a quality control image for coregistration. WHIFUN_QC_COREG_ORTHOSLICE(image_1_path, image_2_path, out_image_path, caption_1, caption_2) generates a quality control image to visually inspect the alignment of two neuroimaging files (e.g., a functional image and an anatomical image) after coregistration. The function uses SPM's `spm_check_registration_evalc` and `spm_orthviews` to create a plot showing three orthogonal slices of `image_2` with an overlay contour of `image_1`. This visual check is essential for verifying the accuracy of the coregistration step. 
  - Internal calls detected: `spm_check_registration_evalc`
  - External dependencies detected: SPM12

## Function: `whifun_qc_coreg_orthoslice()`
- **Functional Purpose:** WHIFUN_QC_COREG_ORTHOSLICE Creates a quality control image for coregistration. WHIFUN_QC_COREG_ORTHOSLICE(image_1_path, image_2_path, out_image_path, caption_1, caption_2) generates a quality control image to visually inspect the alignment of two neuroimaging files (e.g., a functional image and an anatomical image) after coregistration. The function uses SPM's `spm_check_registration_evalc` and `spm_orthviews` to create a plot showing three orthogonal slices of `image_2` with an overlay contour of `image_1`. This visual check is essential for verifying the accuracy of the coregistration step. The function performs the following steps: 1. **Input Handling**: It checks if custom captions are p
- **Arguments:**
  - `image_1_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `image_2_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `out_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `caption_1` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `caption_2` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
