- **Key Features:**
  - No leading help block was present; behavior was inferred from signatures and static calls.
  - Internal calls detected: `whifun_convert_coords`, `whifun_create_sphere`, `whifun_extract_ts_from_vox`
  - External dependencies detected: MATLAB NIfTI I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_seed_corr()`
- **Functional Purpose:** Routine has no dedicated help block; purpose was inferred from its name, surrounding module, and static call context.
- **Arguments:**
  - `func_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `seed` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `radius` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
