- **Key Features:**
  - WHIFUN_GET_BEST_K Performs cross-validation stability analysis to determine the optimal number of clusters (K). [K, DICE_COEF, ELB] = WHIFUN_GET_BEST_K(OUT_PATH, AVG_VOX_LEVEL_FC, K_RANGE_L, K_RANGE_H, CV_FOLDS, NUM_REPLICATES, SIZE_CHUNK, ...) This function implements a feature-based cross-validation strategy to measure the stability of k-means clustering solutions for a range of K values. Stability is calculated using the average maximum Dice similarity coefficient between the clustering solutions obtained from different subsets (folds) of the input feature matrix. The principle is based on 
  - Internal calls detected: `whifun_plot_dice_coef_and_elb`
  - External dependencies detected: MATLAB table/file I/O, Statistics and Machine Learning Toolbox

## Function: `whifun_get_best_k()`
- **Functional Purpose:** WHIFUN_GET_BEST_K Performs cross-validation stability analysis to determine the optimal number of clusters (K). [K, DICE_COEF, ELB] = WHIFUN_GET_BEST_K(OUT_PATH, AVG_VOX_LEVEL_FC, K_RANGE_L, K_RANGE_H, CV_FOLDS, NUM_REPLICATES, SIZE_CHUNK, ...) This function implements a feature-based cross-validation strategy to measure the stability of k-means clustering solutions for a range of K values. Stability is calculated using the average maximum Dice similarity coefficient between the clustering solutions obtained from different subsets (folds) of the input feature matrix. The principle is based on the idea that a clustering solution for the optimal K will be highly consistent (stable) even when t
- **Arguments:**
  - `out_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `avg_vox_level_FC` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `K_range_l` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `K_range_h` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CV_folds` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `num_replicates` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `size_chunk` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d_flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `steps_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `tot_steps` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
