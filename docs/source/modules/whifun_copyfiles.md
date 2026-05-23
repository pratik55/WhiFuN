# whifun_copyfiles

**Source:** `whifun_functions/whifun_copyfiles.m:1`

## Signature

```matlab
function whifun_copyfiles(Subj_list, field_name, dest_folder)
```

## Summary

whifun_copyfiles(Subj_list, field_name, dest_folder)

## Description

Copies files listed in a specified field of a struct array to a destination folder, preserving their directory structure relative to their source locations.

## Input Arguments

Subj_list   : Struct array (e.g., Subj_list(i).func_path = '/data/sub1/func.nii') field_name  : Name of the field containing file paths dest_folder : Destination root folder for copied files Notes: - Creates subfolders as needed to mirror the source directory structure. - Keeps original filenames. - Assumes all files share a common root (e.g., '/data'). You can customize the 'common_root' detection below if needed.

## Examples

Example:

```matlab
whifun_copyfiles(Subj_list, 'func_path', 'D:\All_Func_Files')
```

## Author

Author: Pratik Jain
