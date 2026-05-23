# whifun_get_common_subjects

Source: `whifun_functions/whifun_get_common_subjects.m:1`

```matlab
function [S_common,idx1,idx2] = whifun_get_common_subjects(S1, S2)
```

## MATLAB Help

WHIFUN_GET_COMMON_SUBJECTS Finds the intersection of two subject cohorts based on name.

  S_common = WHIFUN_GET_COMMON_SUBJECTS(S1, S2) compares the '.name' fields 
  of two subject sets and returns a subset of S1 containing only the subjects 
  present in both sets. The structure array format of S1 is completely preserved.

  [S_common, idx1, idx2] = WHIFUN_GET_COMMON_SUBJECTS(S1, S2) additionally 
  returns the indices of the common subjects such that S_common = S1(idx1) 
  and the corresponding matching elements in S2 are found at S2(idx2).

  Input Flexibility:
      Inputs can be provided directly as structure arrays containing a '.name' 
      field, OR as string/char file paths. If a path is provided, the function 
      automatically extracts the folder/file details and loads the dataset 
      using 'load_subjects_all'.

  Dependencies:
      Requires 'load_subjects_all' if paths are passed as inputs.

  Inputs:
      S1       - Structure array of subjects, or string/char path to a subject file.
      S2       - Structure array of subjects, or string/char path to a subject file.

  Outputs:
      S_common - Subset of the S1 structure array containing only intersecting subjects.
      idx1     - Vector of indices mapping S_common back to the original S1 array.
      idx2     - Vector of indices mapping the common elements back to the original S2 array.

  Example:
      % Using paths to files
      path1 = 'C:\Study\CohortA\sub_list.mat';
      path2 = 'C:\Study\CohortB\sub_list.mat';
      [common_struct, idxA, idxB] = whifun_get_common_subjects(path1, path2);
  Author: Pratik Jain
