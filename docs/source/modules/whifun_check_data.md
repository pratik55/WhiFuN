# whifun_check_data

Source: `whifun_functions/whifun_check_data.m:1`

```matlab
function [report,n_image,tr,voxel_func,voxel_anat,mis_data] =  whifun_check_data(output_folder,Subj_list_all,comm_sess_name,func_folder_name,func_data_name,anat_folder_name,anat_data_name,d)
```

## MATLAB Help

WHIFUN_CHECK_DATA Performs an initial, comprehensive check on fMRI and anatomical
  data files for all subjects in a list, recording key metadata and flagging
  missing files.

  [REPORT, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA, SUBJ_LIST_ALL] = ...
      WHIFUN_CHECK_DATA(OUTPUT_FOLDER, SUBJ_LIST_ALL, COMM_SESS_NAME, FUNC_FOLDER_NAME, FUNC_DATA_NAME, ANAT_FOLDER_NAME, ANAT_DATA_NAME, D)

  This is typically the first step in a neuroimaging pipeline, ensuring all
  required files exist and have consistent properties before processing begins.

  Input Arguments:
  OUTPUT_FOLDER       - Path to the directory where the updated subject list CSV will be saved.
  SUBJ_LIST_ALL       - The master structure array containing subject names and metadata.
  COMM_SESS_NAME      - Common session name/pattern for functional data (e.g., 'ses-01').
  FUNC_FOLDER_NAME    - Name of the functional data subdirectory (e.g., 'func').
  FUNC_DATA_NAME      - Pattern or name of the functional data file (e.g., 'bold.nii').
  ANAT_FOLDER_NAME    - Name of the anatomical data subdirectory (e.g., 'anat').
  ANAT_DATA_NAME      - Pattern or name of the anatomical data file (e.g., 'T1w.nii').
  D                   - (Optional) Handle for a progress dialogue box (used in GUIs).

  Output Arguments:
  REPORT              - A string array containing status messages and any errors/warnings.
  N_IMAGE             - Vector of the number of time points (N) for each subject's functional data.
  TR                  - Vector of the Repetition Time (TR) for each subject's functional data.
  VOXEL_FUNC          - Matrix (N x 3) of functional voxel dimensions for each subject.
  VOXEL_ANAT          - Matrix (N x 3) of anatomical voxel dimensions for each subject.
  MIS_DATA            - Flag: 1 if any functional or anatomical files were missing and subjects were removed; 0 otherwise.
  SUBJ_LIST_ALL       - The updated master structure array, including new fields and exclusion flags.

  Dependencies:
  - `whifun_create_fields`, `whifun_initialise_manual_motion_error_fields`
  - `whifun_check_data_func`, `whifun_check_data_anat` (assumed to read NIfTI info and update subject list)
  - `whifun_isnan_or_empty`, `my_writetable`
  - `msgbox` (for displaying missing file summaries)

  Author: Pratik Jain
