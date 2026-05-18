- **Key Features:**
  - WHIFUN_COREG Performs coregistration using SPM. output = WHIFUN_COREG(now_anat_path, now_func_path, mean_func, nt) aligns a subject's functional images to their anatomical image. This is a critical step in fMRI preprocessing to ensure that functional data can be accurately localized to anatomical structures. The function configures and runs the SPM coregistration job. The anatomical image is set as the reference, and a mean functional image is set as the source. All functional volumes are included as "other" images, ensuring that the same transformation is applied to the entire time series. Ke
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SPM12, Shell/system execution

## Function: `whifun_coreg()`
- **Functional Purpose:** WHIFUN_COREG Performs coregistration using SPM. output = WHIFUN_COREG(now_anat_path, now_func_path, mean_func, nt) aligns a subject's functional images to their anatomical image. This is a critical step in fMRI preprocessing to ensure that functional data can be accurately localized to anatomical structures. The function configures and runs the SPM coregistration job. The anatomical image is set as the reference, and a mean functional image is set as the source. All functional volumes are included as "other" images, ensuring that the same transformation is applied to the entire time series. Key parameters are set for the job: - **Cost Function**: Normalized Mutual Information (`'nmi'`) is us
- **Arguments:**
  - `now_anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `now_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mean_func` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `nt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
