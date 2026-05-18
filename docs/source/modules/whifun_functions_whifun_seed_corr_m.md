- **Key Features:**
  - WHIFUN_SEED_CORR Performs Seed-Based Functional Connectivity (FC) Analysis. [OUT_MAP, MATLAB_COR, THRESH] = WHIFUN_SEED_CORR(FUNC_IMAGE_PATH, SEED, RADIUS, OUTPUT_PATH, THRESH, MASK) This function calculates the Pearson correlation map between the mean time series of a spherical seed region (defined in MNI coordinates) and the time series of every other voxel in the brain. It saves the resulting correlation map and optionally saves two thresholded maps (positive and negative correlations). Input Arguments: FUNC_IMAGE_PATH - Full path to the 4D NIfTI file of the functional image. SEED - 3-eleme
  - Internal calls detected: `niftisave`, `whifun_convert_coords`, `whifun_create_sphere`, `whifun_extract_ts_from_vox`, `whifun_niftiread`
  - External dependencies detected: MATLAB NIfTI I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_seed_corr()`
- **Functional Purpose:** WHIFUN_SEED_CORR Performs Seed-Based Functional Connectivity (FC) Analysis. [OUT_MAP, MATLAB_COR, THRESH] = WHIFUN_SEED_CORR(FUNC_IMAGE_PATH, SEED, RADIUS, OUTPUT_PATH, THRESH, MASK) This function calculates the Pearson correlation map between the mean time series of a spherical seed region (defined in MNI coordinates) and the time series of every other voxel in the brain. It saves the resulting correlation map and optionally saves two thresholded maps (positive and negative correlations). Input Arguments: FUNC_IMAGE_PATH - Full path to the 4D NIfTI file of the functional image. SEED - 3-element vector [x, y, z] in MNI space defining the center of the spherical seed region (e.g., [-4 58 20])
- **Arguments:**
  - `func_image_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `seed` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `radius` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `output_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
