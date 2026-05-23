# whifun_delete

Source: `whifun_functions/whifun_delete.m:1`

```matlab
function whifun_delete(path_)
```

## MATLAB Help

WHIFUN_DELETE Safely attempts to delete a file.

  This function wraps the standard MATLAB delete command in a 
  try-catch block. This prevents the pipeline from stopping if 
  a file is locked by the OS, missing, or if permissions are denied.

  INPUTS:
      path_ - String or Character array. The full path to the file 
              you wish to remove.

  EXAMPLE:
      % Clean up a temporary zipped file after extraction
      whifun_delete('C:\Data\temp_image.nii.gz');

  See also DELETE, TRY, CATCH.
  Author: Pratik Jain
