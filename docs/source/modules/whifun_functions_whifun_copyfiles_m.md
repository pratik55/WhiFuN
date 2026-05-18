- **Key Features:**
  - whifun_copyfiles(Subj_list, field_name, dest_folder) Copies files listed in a specified field of a struct array to a destination folder, preserving their directory structure relative to their source locations. Example: whifun_copyfiles(Subj_list, 'func_path', 'D:\All_Func_Files') Inputs: Subj_list : Struct array (e.g., Subj_list(i).func_path = '/data/sub1/func.nii') field_name : Name of the field containing file paths dest_folder : Destination root folder for copied files Notes: - Creates subfolders as needed to mirror the source directory structure. - Keeps original filenames. - Assumes all f
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_copyfiles()`
- **Functional Purpose:** whifun_copyfiles(Subj_list, field_name, dest_folder) Copies files listed in a specified field of a struct array to a destination folder, preserving their directory structure relative to their source locations. Example: whifun_copyfiles(Subj_list, 'func_path', 'D:\All_Func_Files') Inputs: Subj_list : Struct array (e.g., Subj_list(i).func_path = '/data/sub1/func.nii') field_name : Name of the field containing file paths dest_folder : Destination root folder for copied files Notes: - Creates subfolders as needed to mirror the source directory structure. - Keeps original filenames. - Assumes all files share a common root (e.g., '/data'). You can customize the 'common_root' detection below if nee
- **Arguments:**
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `field_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `dest_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
