# whifun_partial_corr

Source: `whifun_functions/whifun_partial_corr.m:1`

```matlab
function pcor_ts_path = whifun_partial_corr(WM_or_GM,mask_subj_ts_folder,avg_ts_path,fr_mask_path,Subj_list,K,over_write,d_flag,d,steps,tot_steps)
```

## MATLAB Help

WHIFUN_PARTIAL_CORR Computes the partial correlation between the time series
  of voxels in a target mask and the average time series of a set of
  functional networks (FNs), controlling for all other FNs.

  PCOR_TS_PATH = WHIFUN_PARTIAL_CORR(WM_OR_GM, MASK_SUBJ_TS_FOLDER, AVG_TS_PATH, FR_MASK_PATH, SUBJ_LIST, K, OVER_WRITE, D_FLAG, D, STEPS, TOT_STEPS)

  This function calculates the individual-level partial correlation maps
  (Fisher-z transformed) between every voxel's time series in the target
  `fr_mask` and each of the K functional networks (WM-FN or GM-FN), while
  regressing out the influence of the other K-1 networks.

  Input Arguments:
  WM_OR_GM            - String indicating the network type (e.g., 'WM' or 'GM').
  MASK_SUBJ_TS_FOLDER - Full path to the folder containing MAT files with the
                        individual voxel time series extracted from the target mask
                        (e.g., callosal voxels, gray matter mask).
                        Files should be named: <SubjectName>_<MaskName>_ts.mat.
  AVG_TS_PATH         - Full path to the folder containing the average time series
                        of the Functional Networks (FNs).
                        Files should be named: <SubjectName>_<WM_or_GM>_FN_K<K>_avg_ts.mat.
  FR_MASK_PATH        - Full path to the NIfTI file of the target mask (e.g., callosum).
  SUBJ_LIST           - Structure array containing subject information.
  K                   - The number of functional networks (clusters) used in the FN analysis.
  OVER_WRITE          - (Optional, default 0) Boolean (0 or 1) to overwrite existing
                        partial correlation results.
  D_FLAG, D, STEPS, TOT_STEPS - (Optional) Parameters for progress dialogue box
                                (typically used in a GUI environment).

  Output Arguments:
  PCOR_TS_PATH        - Full path to the output directory where subject-specific
                        partial correlation results are saved.

  Output Files (saved in PCOR_TS_PATH):
  - <SubjectName>_parcorr_result_K<K>.mat
    Contains: `parcorr_result` (N_Voxels x K matrix of Fisher-z transformed
              partial correlation values) and `Subj`.

  Author: Pratik Jain
