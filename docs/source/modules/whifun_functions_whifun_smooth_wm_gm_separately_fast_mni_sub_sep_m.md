- **Key Features:**
  - loading the data and reslicing the anatomical images to functional resolution
  - Internal calls detected: `niftisave`, `reslice_data`, `whifun_create_file`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, SPM12, Shell/system execution

## Function: `whifun_smooth_WM_GM_separately_fast_MNI_sub_sep()`
- **Functional Purpose:** loading the data and reslicing the anatomical images to functional resolution
- **Arguments:**
  - `in_func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_file_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_file_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `smooth_pre` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `gaussian_FWHM` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
