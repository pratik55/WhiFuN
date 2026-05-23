# whifun_gunzip_preproc

Source: `whifun_functions/whifun_gunzip_preproc.m:1`

```matlab
function [Subj_list_1,out_path] = whifun_gunzip_preproc(now_file_path,Subj_list_1,anat_func)
```

## MATLAB Help

WHIFUN_GUNZIP_PREPROC Unzips .nii.gz files for preprocessing.

  [Subj_list_1, out_path] = WHIFUN_GUNZIP_PREPROC(now_file_path, Subj_list_1, anat_func)
  unzips a compressed neuroimaging file (e.g., `file.nii.gz`) to a standard
  NIfTI file (`file.nii`). The function handles both anatomical and
  functional data, updating the subject structure with the path to the
  unzipped file.

  The function first checks for the existence of multiple files and, if
  found, selects the oldest one. It then checks if the unzipped `.nii` file
  already exists to avoid redundant processing. If the `.nii.gz` file is
  present and the `.nii` file is not, it performs the unzipping operation.

  Input Arguments:
  now_file_path - A `dir` structure pointing to the file to be unzipped.
  Subj_list_1   - A single subject structure that will be updated.
  anat_func     - A string, either 'anatomical' or 'functional', to
                  specify the type of data being processed.

  Output Arguments:
  Subj_list_1 - The updated subject structure, which now includes a new
                field (`nii_anat` or `nii_func`) with the path to the
                unzipped file.
  out_path    - The full path to the unzipped `.nii` file.

  Author: Pratik Jain
  See also GUNZIP, DIR, FULLFILE, ISEMPTY, ISFILE, SPLIT.
