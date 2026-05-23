# whifun_unzip_all_in_folder

**Source:** `whifun_functions/whifun_unzip_all_in_folder.m:1`

## Signature

```matlab
function whifun_unzip_all_in_folder(folder_)
```

## Summary

WHIFUN_UNZIP_ALL_IN_FOLDER Unzips all .nii.gz files located directly within a specified folder.

## Syntax

```matlab
WHIFUN_UNZIP_ALL_IN_FOLDER(FOLDER_)
```

## Description

This utility function is commonly used in neuroimaging pipelines to decompress gzipped NIfTI files (.nii.gz) into standard NIfTI files (.nii) before processing steps that require the uncompressed format.

## Input Arguments

### `FOLDER_`
A character array or string specifying the path to the folder containing the .nii.gz files to be unzipped.

## Requirements

MATLAB's built-in `gunzip` and `dir` functions.

## Author

Author: Pratik Jain
