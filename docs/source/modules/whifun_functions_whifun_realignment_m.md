- **Key Features:**
  - WHIFUN_REALIGNMENT Performs motion correction (realignment) using SPM. output = WHIFUN_REALIGNMENT(now_func_path, Realign_pre, nt) configures and executes the SPM realignment job to correct for head motion in a time series of functional images. This function creates an SPM batch job to: - **Estimate and Write**: Estimates the motion parameters and applies the transformations to create a new, realigned image series. - **Quality Settings**: Uses a high-quality estimation (`quality = 0.9`), a default separation, and a FWHM smoothing kernel of 5mm. - **Reference Image**: Registers all images to th
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SPM12, Shell/system execution

## Function: `whifun_realignment()`
- **Functional Purpose:** WHIFUN_REALIGNMENT Performs motion correction (realignment) using SPM. output = WHIFUN_REALIGNMENT(now_func_path, Realign_pre, nt) configures and executes the SPM realignment job to correct for head motion in a time series of functional images. This function creates an SPM batch job to: - **Estimate and Write**: Estimates the motion parameters and applies the transformations to create a new, realigned image series. - **Quality Settings**: Uses a high-quality estimation (`quality = 0.9`), a default separation, and a FWHM smoothing kernel of 5mm. - **Reference Image**: Registers all images to the first image in the series (`rtm = 0`). - **Interpolation**: Uses 2nd-degree B-spline for estimatio
- **Arguments:**
  - `now_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Realign_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `nt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
