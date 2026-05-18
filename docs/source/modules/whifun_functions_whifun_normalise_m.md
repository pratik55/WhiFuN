- **Key Features:**
  - WHIFUN_NORMALISE Normalizes images to MNI space using SPM. output = WHIFUN_NORMALISE(in_def_path, ..., func_anat) applies a pre-existing deformation field to either a functional or an anatomical image, transforming it from the subject's native space to a standard template space (MNI). setenv The function configures and executes the `spm.spatial.normalise.write` job. The process involves: 1. **Inputting Deformation Field**: It takes the deformation field (generated during the segmentation step) as the key input for the transformation. 2. **Resampling**: Based on the `func_anat` flag, it either 
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SPM12, Shell/system execution

## Function: `whifun_normalise()`
- **Functional Purpose:** WHIFUN_NORMALISE Normalizes images to MNI space using SPM. output = WHIFUN_NORMALISE(in_def_path, ..., func_anat) applies a pre-existing deformation field to either a functional or an anatomical image, transforming it from the subject's native space to a standard template space (MNI). setenv The function configures and executes the `spm.spatial.normalise.write` job. The process involves: 1. **Inputting Deformation Field**: It takes the deformation field (generated during the segmentation step) as the key input for the transformation. 2. **Resampling**: Based on the `func_anat` flag, it either resamples the entire functional time series or the anatomical image. 3. **Output Voxel Size**: The o
- **Arguments:**
  - `in_def_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `nt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vox` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Norm_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_anat` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
