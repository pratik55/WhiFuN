- **Key Features:**
  - WHIFUN_SEED_CORR_QC_PLOT Computes seed-based functional connectivity (FC) and generates a quality control (QC) visualization using the Slover tool. WHIFUN_SEED_CORR_QC_PLOT(OUTPUT_PATH, FUNC_PATH, SEED, RAD, SEED_COR_OUTPUT_PATH, THRESH, SLICES_MNI, VIEW, MASK) This function first calculates the seed-to-voxel correlation map for a given seed location. It then creates two temporary thresholded versions of the correlation map and visualizes them simultaneously using Slover (e.g., one for positive correlation, one for negative) on top of the structural image for QC purposes. The temporary files a
  - Internal calls detected: `whifun_seed_corr`, `whifun_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_seed_corr_qc_plot()`
- **Functional Purpose:** WHIFUN_SEED_CORR_QC_PLOT Computes seed-based functional connectivity (FC) and generates a quality control (QC) visualization using the Slover tool. WHIFUN_SEED_CORR_QC_PLOT(OUTPUT_PATH, FUNC_PATH, SEED, RAD, SEED_COR_OUTPUT_PATH, THRESH, SLICES_MNI, VIEW, MASK) This function first calculates the seed-to-voxel correlation map for a given seed location. It then creates two temporary thresholded versions of the correlation map and visualizes them simultaneously using Slover (e.g., one for positive correlation, one for negative) on top of the structural image for QC purposes. The temporary files are deleted after plotting. Input Arguments: OUTPUT_PATH - Full path to save the final QC plot graphi
- **Arguments:**
  - `output_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `seed` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `rad` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `seed_cor_output_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mask` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
