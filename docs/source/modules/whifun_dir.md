# whifun_dir

**Source:** `whifun_functions/whifun_dir.m:1`

## Signature

```matlab
function out = whifun_dir(path_)
```

## Summary

WHIFUN_DIR Safely retrieves directory information.

## Description

This function wraps the standard MATLAB dir command in a try-catch block. It is particularly useful for robustly handling missing directories or path-string errors without interrupting the execution of a larger preprocessing loop.

## Input Arguments

### `path_`
String or Character array. The path or file pattern to be listed (e.g., '/data/sub-*/func/').

## Output Arguments

### `out`
A structure array containing directory information. Returns an empty array [] if the path is invalid or an error occurs.

## Examples

EXAMPLE: % Safely check for the presence of a specific session contents = whifun_dir(fullfile(subj_dir, 'ses-02')); if isempty(contents) fprintf('Session 02 not found for this subject.\n'); end

See also DIR, WHIFUN_COMPLETE_FILEPATH, WHIFUN_DELETE.

## Author

Author: Pratik Jain
