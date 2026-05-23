# whifun_delete

**Source:** `whifun_functions/whifun_delete.m:1`

## Signature

```matlab
function whifun_delete(path_)
```

## Summary

WHIFUN_DELETE Safely attempts to delete a file.

## Description

This function wraps the standard MATLAB delete command in a try-catch block. This prevents the pipeline from stopping if a file is locked by the OS, missing, or if permissions are denied.

## Input Arguments

### `path_`
String or Character array. The full path to the file you wish to remove.

## Examples

EXAMPLE: % Clean up a temporary zipped file after extraction

See also DELETE, TRY, CATCH.

```matlab
whifun_delete('C:\Data\temp_image.nii.gz');
```

## Author

Author: Pratik Jain
