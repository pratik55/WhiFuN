# whifun_create_avg_ts

Source: `whifun_functions/whifun_create_avg_ts.m:1`

```matlab
function [avg_ts_path,Subj_list] = whifun_create_avg_ts(out_folder,ROI_path,Subj_list,field,band_info,QC_plots,over_write,d_flag,d,steps_,tot_steps)
```

## MATLAB Help

WHIFUN_GET_AVG_TS Extracts the average time series for each region in a given ROI atlas.

  AVG_TS_PATH = WHIFUN_GET_AVG_TS(OUT_FOLDER, ROI_PATH, SUBJ_LIST, FIELD, BAND_INFO, QC_PLOTS, OVER_WRITE, D_FLAG, D, STEPS_, TOT_STEPS)

  This function reads functional MRI data for a list of subjects, resamples
  the specified Atlas (ROI), and extracts the mean BOLD time series for
  every non-zero region defined in the Atlas. It also handles optional
  bandpass filtering and checks for regions with missing functional data.

  Input Arguments:
  OUT_FOLDER      - Main output directory for saving results and QC plots.
  ROI_PATH        - Full path to the NIfTI file defining the ROI atlas.
  SUBJ_LIST       - (can be created with whifun_create_Subj_list)
                    Structure array containing subject information. Must include
                    a field (specified by `FIELD`) pointing to the subject's
                    preprocessed functional NIfTI file (e.g., 'final_func_MNI').
  FIELD           - (Optional, default 'final_func_MNI') The field name in
                    `Subj_list` that holds the path to the functional image.
  BAND_INFO       - (Optional) Structure array defining bandpass filters:
                    .hp       - High-pass frequency (Hz).
                    .lp       - Low-pass frequency (Hz).
                    .band_name - Name for the frequency band (e.g., 'slow_01').
  QC_PLOTS        - (Optional, default 0) Boolean (0 or 1) to generate QC plots
                    showing regions with partial/null data overlayed on the fMRI.
  OVER_WRITE      - (Optional, default 0) Boolean (0 or 1) to overwrite existing
                    average time series files.
  D_FLAG, D, STEPS_, TOT_STEPS - (Optional) Parameters for progress dialogue box
                                 (typically used in a GUI environment).

  Output Arguments:
  AVG_TS_PATH     - Full path to the directory where the average time series
                    MAT files are saved.

  Output Files (saved in AVG_TS_PATH or subdirectories):
  - <SubjectName>_<ROI_Name>_avg_ts.mat (Unfiltered)
    Contains: `avg_ts` (nT x N_ROI matrix), `Subj`, `voxels_with_data`.
  - <BandName>_<LP>-<HP>/<SubjectName>_<ROI_Name>_<BandName>_..._avg_ts.mat (Filtered)
    Contains: `avg_ts_freq` (filtered time series), `vox_count_in_reg`, `Subj`, `hp`, `lp`, `band_name`.

  Author: Pratik Jain
