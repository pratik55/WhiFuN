- **Key Features:**
  - WHIFUN_NORMALISE_PREPROC Orchestrates normalization to MNI space. [Subj_list_1, out_func_path, out_anat_path] = WHIFUN_NORMALISE_PREPROC(...) is a high-level function that manages the spatial normalization step of a neuroimaging preprocessing pipeline. It applies a previously calculated deformation field (from the segmentation step) to both functional and anatomical images, transforming them from the subject's native space to a standard template space (MNI). The function performs the normalization in two separate steps: 1. **Functional Normalization**: It checks for an existing normalized func
  - Internal calls detected: `reslice_data`, `whifun_anat_mask`, `whifun_create_file`, `whifun_normalise`, `write_error`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_normalise_preproc()`
- **Functional Purpose:** WHIFUN_NORMALISE_PREPROC Orchestrates normalization to MNI space. [Subj_list_1, out_func_path, out_anat_path] = WHIFUN_NORMALISE_PREPROC(...) is a high-level function that manages the spatial normalization step of a neuroimaging preprocessing pipeline. It applies a previously calculated deformation field (from the segmentation step) to both functional and anatomical images, transforming them from the subject's native space to a standard template space (MNI). The function performs the normalization in two separate steps: 1. **Functional Normalization**: It checks for an existing normalized functional file and, based on the `over_write` flag, either skips or calls `whifun_normalise` to perform
- **Arguments:**
  - `quality_control_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_def_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vox` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Norm_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `log_fileID` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
