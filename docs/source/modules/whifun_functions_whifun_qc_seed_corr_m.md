- **Key Features:**
  - WHIFUN_QC_SEED_CORR Generates quality control images for seed-based functional connectivity. WHIFUN_QC_SEED_CORR(out_folder, final_func_MNI, name, thresh, rad, slover_slices_mni, slover_view, over_write, func_mask_MNI) creates a visual quality control report to assess the quality of a subject's functional data by performing a simple seed-to-voxel correlation. The function calculates the correlation map for three standard functional networks: 1. **Default Mode Network (DMN)**: Seeded in the left Posterior Cingulate Cortex (PCC). 2. **Visual Network**: Seeded in the right visual cortex. 3. **Aud
  - Internal calls detected: `whifun_create_file`, `whifun_seed_corr_qc_plot`
  - External dependencies detected: SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_seed_corr()`
- **Functional Purpose:** WHIFUN_QC_SEED_CORR Generates quality control images for seed-based functional connectivity. WHIFUN_QC_SEED_CORR(out_folder, final_func_MNI, name, thresh, rad, slover_slices_mni, slover_view, over_write, func_mask_MNI) creates a visual quality control report to assess the quality of a subject's functional data by performing a simple seed-to-voxel correlation. The function calculates the correlation map for three standard functional networks: 1. **Default Mode Network (DMN)**: Seeded in the left Posterior Cingulate Cortex (PCC). 2. **Visual Network**: Seeded in the right visual cortex. 3. **Auditory Network**: Seeded in the left auditory cortex. For each network, the function performs the fol
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `final_func_MNI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `thresh` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `rad` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices_mni` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_mask_MNI` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
