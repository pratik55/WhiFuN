- **Key Features:**
  - COMPLETE_FILEPATH Resolves a full file path from segments or wildcards. OUT_PATH = COMPLETE_FILEPATH(DIR, SUBDIR, FILENAME) joins the input segments using the system's file separator and attempts to resolve the final path. If wildcards are used, it returns the first match. INPUTS: varargin - Any number of string or character array segments representing a path (e.g., 'C:', 'Data', 'sub-*_T1w.nii'). OUTPUTS: out_path - A single string of the resolved path. Returns an empty string if the path cannot be found. NOTES: - If multiple files match a wildcard, the function currently returns the folder p
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `complete_filepath()`
- **Functional Purpose:** COMPLETE_FILEPATH Resolves a full file path from segments or wildcards. OUT_PATH = COMPLETE_FILEPATH(DIR, SUBDIR, FILENAME) joins the input segments using the system's file separator and attempts to resolve the final path. If wildcards are used, it returns the first match. INPUTS: varargin - Any number of string or character array segments representing a path (e.g., 'C:', 'Data', 'sub-*_T1w.nii'). OUTPUTS: out_path - A single string of the resolved path. Returns an empty string if the path cannot be found. NOTES: - If multiple files match a wildcard, the function currently returns the folder path if multiple matches exist, or the full filename if only one match exists. - If the path is not f
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
