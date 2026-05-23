# whifun_clean_up_folder

**Source:** `whifun_functions/whifun_clean_up_folder.m:1`

## Signature

```matlab
function whifun_clean_up_folder(folder_,log_file_id)
```

## Summary

WHIFUN_CLEAN_UP_FOLDER Compresses all NIfTI (.nii) files in a specified folder

## Syntax

```matlab
WHIFUN_CLEAN_UP_FOLDER(FOLDER_, LOG_FILE_ID)
```

## Description

into gzipped format (.nii.gz) and removes redundant uncompressed copies.

This utility function performs two main tasks:

1. **Removes Duplicates:** It identifies and deletes any uncompressed
NIfTI files (`.nii`) that already have a compressed counterpart (`.<file>.nii.gz`) present in the same folder.

2. **Compresses Remaining Files:** It then compresses all remaining
uncompressed `.nii` files into `.nii.gz` format and deletes the original uncompressed `.nii` files. All actions are logged to the specified file handle and the command window.

## Input Arguments

### `FOLDER_`
The full path to the directory to be cleaned up.

### `LOG_FILE_ID`
A file ID handle (obtained via `fopen`) for the log file where operations will be recorded.

## Requirements

`gzip` (MATLAB built-in function).

## Author

Author: Pratik Jain
