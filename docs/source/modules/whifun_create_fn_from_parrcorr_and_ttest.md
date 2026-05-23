# whifun_create_fn_from_parrcorr_and_ttest

**Source:** `whifun_functions/whifun_create_fn_from_parrcorr_and_ttest.m:1`

## Signature

```matlab
function fn_path = whifun_create_fn_from_parrcorr_and_ttest(WM_or_GM,pcor_ts_path,mask_path,Subj_list,K,over_write,d_flag,d,wm_steps,tot_wm_steps)
```

## Summary

WHIFUN_CREATE_FN_FROM_PARRCORR_AND_TTEST Creates a new Functional Network (FN) map

## Syntax

```matlab
FN_PATH = WHIFUN_CREATE_FN_FROM_PARRCORR_AND_TTEST(WM_OR_GM, PCOR_TS_PATH, MASK_PATH, SUBJ_LIST, K, OVER_WRITE, ...)
```

## Description

by assigning each voxel in a target mask (e.g., Corpus Callosum) to the existing network (e.g., WM or GM) with which it shares the maximal significant partial correlation.

This is used to extend existing FN definitions (like WM-FNs) into other regions (like the Corpus Callosum or Cerebellum) based on connectivity. The assignment metric is the group-level t-statistic of the partial correlation across subjects.

## Input Arguments

### `WM_OR_GM`
String ('WM' or 'GM') indicating the type of network used as the base for partial correlation calculation.

### `PCOR_TS_PATH`
Path to the folder containing subject-specific partial correlation (.mat) files. These files hold the partial correlation between each voxel in the MASK_PATH and the K base networks.

### `MASK_PATH`
Full path to the NIfTI file of the target mask (e.g., CC mask).

### `SUBJ_LIST`
Structure array containing subject information.

### `K`
The number of networks (clusters) in the base solution.

### `OVER_WRITE`
(Optional, default 0) Flag: 1 to overwrite existing output NIfTI file.

### `D_FLAG, D, WM_STEPS, TOT_WM_STEPS`
(Optional) Parameters for progress dialogue box (GUI support).

## Output Arguments

### `FN_PATH`
The full path to the newly created NIfTI file containing the assigned network map (e.g., '.../CC_FN_from_WM_K10.nii').

## Requirements

'whifun_create_file', 'whifun_niftiread', 'niftisave'.

## Author

Author: Pratik Jain
