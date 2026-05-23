# whifun_seed_corr

Source: `whifun_functions/whifun_seed_corr.m:1`

```matlab
function [out_map,matlab_cor,thresh] = whifun_seed_corr(func_image_path,seed,radius,output_path,thresh,mask)
```

## MATLAB Help

WHIFUN_SEED_CORR Performs Seed-Based Functional Connectivity (FC) Analysis.

  [OUT_MAP, MATLAB_COR, THRESH] = WHIFUN_SEED_CORR(FUNC_IMAGE_PATH, SEED, RADIUS, OUTPUT_PATH, THRESH, MASK)

  This function calculates the Pearson correlation map between the mean time
  series of a spherical seed region (defined in MNI coordinates) and the time
  series of every other voxel in the brain. It saves the resulting correlation
  map and optionally saves two thresholded maps (positive and negative correlations).

  Input Arguments:
  FUNC_IMAGE_PATH - Full path to the 4D NIfTI file of the functional image.
  SEED            - 3-element vector [x, y, z] in MNI space defining the center
                    of the spherical seed region (e.g., [-4 58 20]).
  RADIUS          - The radius of the spherical seed region in mm.
  OUTPUT_PATH     - Full path to save the unthresholded correlation map NIfTI file.
  THRESH          - (Optional) 2-element vector [negative_threshold, positive_threshold]
                    used to create and save two thresholded output maps.
                    e.g., [-0.3 0.3]. If not provided, no thresholding is done.
  MASK            - (Optional) Path to a NIfTI file or a 3D numeric volume to
                    mask the resulting correlation map. Can be NaN to skip masking.

  Output Arguments:
  OUT_MAP         - The 3D volume of unthresholded correlation values (Fisher Z-transformed if the input was).
  MATLAB_COR      - The 3-element vector [x, y, z] of the seed center in voxel coordinates.
  THRESH          - The input threshold vector (unchanged, but returned for consistency).

  Dependencies: 'whifun_niftiread', 'whifun_convert_coords', 'whifun_create_sphere',
                'whifun_extract_ts_from_vox', 'niftisave'.

  Author: Pratik Jain
