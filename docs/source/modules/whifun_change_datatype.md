# whifun_change_datatype

**Source:** `whifun_functions/whifun_change_datatype.m:1`

## Signature

```matlab
function whifun_change_datatype(Subj_list,data_type,field)
```

## Summary

WHIFUN_CHANGE_DATATYPE Converts NIfTI image data to a new datatype and overwrites.

## Syntax

```matlab
WHIFUN_CHANGE_DATATYPE(Subj_list, data_type) takes a single NIfTI file path
WHIFUN_CHANGE_DATATYPE(Subj_list, data_type, field) processes a batch
```

## Description

(string or char) and casts its internal image data to the specified data_type. It calculates the Mean Squared Error (MSE) introduced by the conversion, displays the memory footprint before and after, and saves the newly typed image back to disk.

of files. If Subj_list is a structure array, you must provide the 'field' argument as a string/char indicating which field contains the file paths.

Important Note: This function overwrites the original file in place and applies the AdditiveOffset and MultiplicativeScaling from the NIfTI header prior to saving.

## Input Arguments

### `Subj_list`
String/char array for a single file path, OR a struct array containing multiple file paths.

### `data_type`
String or char array of the target MATLAB datatype (e.g., 'single', 'int16', 'uint8').

### `field`
(Optional) String or char array specifying the fieldname in Subj_list that holds the file paths. Required if Subj_list is a struct.

## Examples

Example 1: Single File

Example 2: Structure Array files = dir('C:\Data\*\T1.nii');

```matlab
whifun_change_datatype('C:\Data\T1.nii', 'single');
whifun_change_datatype(files, 'single', 'name');
```

## Requirements

'whifun_niftiread' to read the image data and info.

## Author

Author: Pratik Jain
