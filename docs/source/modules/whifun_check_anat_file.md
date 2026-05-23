# whifun_check_anat_file

Source: `whifun_functions/whifun_check_anat_file.m:1`

```matlab
function [now_anat_path,report] = whifun_check_anat_file(Subj_list_1,comm_sess_name,anat_folder_name,anat_data_name)
```

## MATLAB Help

WHIFUN_CHECK_ANAT_FILE Verifies the existence of an anatomical data file.

  [now_anat_path, report] = WHIFUN_CHECK_ANAT_FILE(Subj_list_1, comm_sess_name, anat_folder_name)
  searches for an anatomical neuroimaging data file (`.nii` or `.nii.gz`)
  for a given subject. It constructs the expected file path and checks if
  the file exists.

  The function first uses the path information from the subject structure
  and checks for a NIfTI file with a `.nii*` extension. If the file is
  not found, it generates a detailed error report, including which part of
  the path (session folder, anatomical folder, or the file itself) is
  missing.

  This function is essential for robust preprocessing pipelines, ensuring
  that the anatomical data for each subject is in the expected location
  before processing begins.

  Input Arguments:
  Subj_list_1      - A single subject structure, which must contain
                     `anat_folder` and `anat_name` fields.
  comm_sess_name   - The common session folder name (e.g., 'ses-01').
  anat_folder_name - The name of the anatomical data subfolder (e.g., 'anat').

  Output Arguments:
  now_anat_path - A `dir` structure if the file is found, otherwise empty.
  report        - A string containing an error message if the file is not
                  found, otherwise an empty string.

  Author: Pratik Jain
  See also DIR, FULLFILE, ISEMPTY, ISFOLDER, STRCHR.
