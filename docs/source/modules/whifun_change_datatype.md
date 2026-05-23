# whifun_change_datatype

Source: `whifun_functions/whifun_change_datatype.m:1`

```matlab
function whifun_change_datatype(Subj_list,data_type,field)
```

## MATLAB Help

WHIFUN_CHANGE_DATATYPE Converts NIfTI image data to a new datatype and overwrites.

  WHIFUN_CHANGE_DATATYPE(Subj_list, data_type) takes a single NIfTI file path 
  (string or char) and casts its internal image data to the specified 
  data_type. It calculates the Mean Squared Error (MSE) introduced by the 
  conversion, displays the memory footprint before and after, and saves 
  the newly typed image back to disk.

  WHIFUN_CHANGE_DATATYPE(Subj_list, data_type, field) processes a batch 
  of files. If Subj_list is a structure array, you must provide the 'field' 
  argument as a string/char indicating which field contains the file paths.

  Important Note: This function overwrites the original file in place and 
  applies the AdditiveOffset and MultiplicativeScaling from the NIfTI header 
  prior to saving.

  Dependencies: 
      Requires 'whifun_niftiread' to read the image data and info.

  Inputs:
      Subj_list - String/char array for a single file path, OR a struct 
                  array containing multiple file paths.
      data_type - String or char array of the target MATLAB datatype 
                  (e.g., 'single', 'int16', 'uint8').
      field     - (Optional) String or char array specifying the fieldname 
                  in Subj_list that holds the file paths. Required if 
                  Subj_list is a struct.

  Example 1: Single File
      whifun_change_datatype('C:\Data\T1.nii', 'single');

  Example 2: Structure Array
      files = dir('C:\Data\*\T1.nii');
      whifun_change_datatype(files, 'single', 'name');

  Author: Pratik Jain
