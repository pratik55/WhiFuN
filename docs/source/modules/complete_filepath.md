# complete_filepath

Source: `whifun_functions/complete_filepath.m:1`

```matlab
function out_path = complete_filepath(varargin)
```

## MATLAB Help

COMPLETE_FILEPATH Resolves a full file path from segments or wildcards.

  OUT_PATH = COMPLETE_FILEPATH(DIR, SUBDIR, FILENAME) joins the input 
  segments using the system's file separator and attempts to resolve 
  the final path. If wildcards are used, it returns the first match.

  INPUTS:
      varargin - Any number of string or character array segments 
                 representing a path (e.g., 'C:', 'Data', 'sub-*_T1w.nii').

  OUTPUTS:
      out_path - A single string of the resolved path. Returns an empty 
                 string if the path cannot be found.

  NOTES:
      - If multiple files match a wildcard, the function currently returns 
        the folder path if multiple matches exist, or the full filename 
        if only one match exists.
      - If the path is not found, a warning is displayed in the console.

  EXAMPLE:
      % Find a specific BIDS file using a wildcard
      path = complete_filepath('/data/project', 'sub-01', 'ses-*', '*_bold.nii.gz');

  See also FULLFILE, DIR, STRING.
