# whifun_get_func_TR

Source: `whifun_functions/whifun_get_func_TR.m:1`

```matlab
function [Subj_list_1,tr,report] = whifun_get_func_TR(now_func_path,Subj_list_1)
```

## MATLAB Help

WHIFUN_GET_FUNC_TR Extracts the TR (Repetition Time) from a functional NIfTI file.

  [Subj_list_1, tr, report] = WHIFUN_GET_FUNC_TR(now_func_path, Subj_list_1)
  attempts to read the TR from the header of a functional NIfTI file.
  The TR is a critical parameter for fMRI data analysis.

  The function uses `niftiinfo` to access the file's metadata. If the TR
  is successfully retrieved, it is returned and stored in the subject's
  structure. In case the TR value is not available, the
  function sets the TR to `NaN` and generates a report message, which is
  useful for downstream error handling.

  Input Arguments:
  now_func_path - A `dir` structure (from a call to `dir`) pointing to
                  the functional NIfTI file.
  Subj_list_1   - A single subject structure, which will be updated
                  with the TR value.

  Output Arguments:
  Subj_list_1 - The updated subject structure, now containing the `TR` field.
  tr          - The repetition time (TR) in seconds, or `NaN` if not found.
  report      - A string containing a warning message if the TR could not
                be found, otherwise an empty string.

  Example:
     % Assume 'func_file' is a valid dir structure for a NIfTI file
     % and 'subject_struct' is a subject structure.
     % [subject_struct, tr, msg] = whifun_get_func_TR(func_file, subject_struct);

  Author: Pratik Jain
  See also NIFTIINFO, WARNING.
