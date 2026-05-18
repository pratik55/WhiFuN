- **Key Features:**
  - WHIFUN_SEGMENT Performs SPM-based segmentation and normalization. output = WHIFUN_SEGMENT(now_anat_path, spm_path) runs the SPM segmentation and normalization routine on a subject's anatomical image. This function configures and executes the `spm_jobman` for the `spm.spatial.preproc` module. The batch job is set up to: - **Bias Correct** the anatomical image and save the output. - **Segment** the image into six tissue types (Gray Matter, White Matter, CSF, skull, and related items.) using the default Tissue Probability Map (TPM). - **Save** the native-space and MNI-normalized versions of the GM, WM, and CSF
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB NIfTI I/O, SPM12, Shell/system execution

## Function: `whifun_segment()`
- **Functional Purpose:** WHIFUN_SEGMENT Performs SPM-based segmentation and normalization. output = WHIFUN_SEGMENT(now_anat_path, spm_path) runs the SPM segmentation and normalization routine on a subject's anatomical image. This function configures and executes the `spm_jobman` for the `spm.spatial.preproc` module. The batch job is set up to: - **Bias Correct** the anatomical image and save the output. - **Segment** the image into six tissue types (Gray Matter, White Matter, CSF, skull, and related items.) using the default Tissue Probability Map (TPM). - **Save** the native-space and MNI-normalized versions of the GM, WM, and CSF segments. - **Save** the forward and inverse deformation field maps, which are essential for normal
- **Arguments:**
  - `now_anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `spm_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
