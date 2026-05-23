# whifun_check_data_anat

Source: `whifun_functions/whifun_check_data_anat.m:1`

```matlab
function [Subj_list_1,voxel_anat,no_anat,report] = whifun_check_data_anat(Subj_list_1,comm_sess_name,anat_folder_name,anat_data_name,output_folder,report)
```

## MATLAB Help

WHIFUN_CHECK_DATA_ANAT Checks for the existence and retrieves metadata of the anatomical NIfTI file for a single subject.

  [SUBJ_LIST_1, VOXEL_ANAT, NO_ANAT, REPORT] = WHIFUN_CHECK_DATA_ANAT(SUBJ_LIST_1, COMM_SESS_NAME, ANAT_FOLDER_NAME, ANAT_DATA_NAME, REPORT)

  This is a helper function for the initial data quality check process. It
  locates the anatomical file, handles cases where multiple files are
  found, and records the file's metadata and status.

  Input Arguments:
  SUBJ_LIST_1      - A single-element structure from the subject list, containing the subject's name and path information.
  COMM_SESS_NAME   - Common session name/pattern for anatomical data (e.g., 'ses-01').
  ANAT_FOLDER_NAME - Name of the anatomical data subdirectory (e.g., 'anat').
  ANAT_DATA_NAME   - Pattern or name of the anatomical data file (e.g., 'T1w.nii').
  REPORT           - (Optional) A string array containing previous report messages.

  Output Arguments:
  SUBJ_LIST_1      - The updated subject structure, including anatomical file path and metadata.
  VOXEL_ANAT       - A 1x3 vector containing the anatomical voxel dimensions [X, Y, Z].
  NO_ANAT          - A flag: 0 if the anatomical file was found, 1 if it was missing.
  REPORT           - The updated report string array, including any new warnings or errors.

  Dependencies:
  - `whifun_check_anat_file`
  - `whifun_get_anat_info` 

  Author: Pratik Jain
