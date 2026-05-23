# whifun_get_ts_from_mask

Source: `whifun_functions/whifun_get_ts_from_mask.m:1`

```matlab
function [mask_analysis_folder_path,mask_subj_ts_folder,mask_name] = whifun_get_ts_from_mask(out_analysis_path,mask_path,Subj_list,resample_mask,over_write,d_flag,d,steps_,tot_steps)
```

## MATLAB Help

WHIFUN_GET_TS_FROM_MASK Extracts time series data for each subject from voxels
  defined by a specified NIfTI mask file.

  [MASK_ANALYSIS_FOLDER_PATH, MASK_SUBJ_TS_FOLDER, MASK_NAME] = WHIFUN_GET_TS_FROM_MASK(OUT_ANALYSIS_PATH, MASK_PATH, SUBJ_LIST, RESAMPLE_MASK, OVER_WRITE, ...)

  This function prepares an analysis folder structure, optionally resamples
  the input mask, and then iterates through all subjects to extract the
  functional time series for the voxels defined by the mask.

  Input Arguments:
  OUT_ANALYSIS_PATH   - The root directory where all analysis results for the
                        entire study will be stored.
  MASK_PATH           - Full path to the NIfTI file used as the mask (e.g., an ROI or atlas).
  SUBJ_LIST           - Structure array containing subject information,
                        including the path to the final preprocessed functional data
                        (SUBJ_LIST(i).final_func_MNI).
  RESAMPLE_MASK       - (Optional, default 1) Flag to resample the mask:
                        RESAMPLE_MASK = 1: Resamples the mask to the functional resolution of the first subject.
                        RESAMPLE_MASK = 0: Copies the mask without resampling.
  OVER_WRITE          - (Optional, default 0) Flag: 1 to overwrite existing subject time series files.
  D_FLAG, D, STEPS_, TOT_STEPS - (Optional) Parameters for progress dialogue box (GUI support).

  Output Arguments:
  MASK_ANALYSIS_FOLDER_PATH - Full path to the copied/resampled mask file in the analysis folder.
  MASK_SUBJ_TS_FOLDER       - Full path to the directory where subject time series files are saved.
  MASK_NAME                 - The clean name of the mask file (without extension).

  Dependencies: 'whifun_niftiread', 'whifun_create_file', 'reslice_data', 'y_Read' (assumed external function).

  Author: Pratik Jain
