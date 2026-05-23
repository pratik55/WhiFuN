# complete_filepath

**Source:** `whifun_functions/complete_filepath.m:1`

## Signature

```matlab
function out_path = complete_filepath(varargin)
```

## Summary

COMPLETE_FILEPATH Resolves a full file path from segments or wildcards.

## Syntax

```matlab
OUT_PATH = COMPLETE_FILEPATH(DIR, SUBDIR, FILENAME) joins the input
```

## Description

segments using the system's file separator and attempts to resolve the final path. If wildcards are used, it returns the first match.

## Input Arguments

### `varargin`
Any number of string or character array segments representing a path (e.g., 'C:', 'Data', 'sub-*_T1w.nii').

## Output Arguments

### `out_path`
A single string of the resolved path. Returns an empty string if the path cannot be found. NOTES:
- If multiple files match a wildcard, the function currently returns the folder path if multiple matches exist, or the full filename if only one match exists.
- If the path is not found, a warning is displayed in the console.

## Examples

EXAMPLE: % Find a specific BIDS file using a wildcard path = complete_filepath('/data/project', 'sub-01', 'ses-*', '*_bold.nii.gz');

See also FULLFILE, DIR, STRING.
