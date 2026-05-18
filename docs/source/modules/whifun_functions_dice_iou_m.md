- **Key Features:**
  - DICE_IOU Computes the Dice Similarity Coefficient and Intersection of Union (IoU) between two functional network (FN) atlas NIfTI files. It can optionally align the second network to the first and generate a visualization of the similarity matrix. [DICE, IOU, VOX_NUM_1, VOX_NUM_2] = DICE_IOU(KMEANS_NET_1_PATH, KMEANS_NET_2_PATH, ALIGN_NET, FIG_DICE) Input Arguments: KMEANS_NET_1_PATH - Full path to the first FN NIfTI file, or the N-dimensional array itself. KMEANS_NET_2_PATH - Full path to the second FN NIfTI file, or the N-dimensional array itself. ALIGN_NET - (Optional, default 0) Flag to al
  - Internal calls detected: `niftisave`, `whifun_convert_3d_to_4d_atlas`
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `dice_iou()`
- **Functional Purpose:** DICE_IOU Computes the Dice Similarity Coefficient and Intersection of Union (IoU) between two functional network (FN) atlas NIfTI files. It can optionally align the second network to the first and generate a visualization of the similarity matrix. [DICE, IOU, VOX_NUM_1, VOX_NUM_2] = DICE_IOU(KMEANS_NET_1_PATH, KMEANS_NET_2_PATH, ALIGN_NET, FIG_DICE) Input Arguments: KMEANS_NET_1_PATH - Full path to the first FN NIfTI file, or the N-dimensional array itself. KMEANS_NET_2_PATH - Full path to the second FN NIfTI file, or the N-dimensional array itself. ALIGN_NET - (Optional, default 0) Flag to align net_2 to net_1: ALIGN_NET = 1: Relabels net_2 based on the maximum Dice match to net_1 and saves
- **Arguments:**
  - `kmeans_net_1_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `kmeans_net_2_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `align_net` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `fig_dice` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
