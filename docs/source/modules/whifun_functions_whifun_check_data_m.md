- **Key Features:**
  - WHIFUN_CHECK_DATA Performs an initial, comprehensive check on fMRI and anatomical data files for all subjects in a list, recording key metadata and flagging missing files. [REPORT, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA, SUBJ_LIST_ALL] = ... WHIFUN_CHECK_DATA(OUTPUT_FOLDER, SUBJ_LIST_ALL, COMM_SESS_NAME, FUNC_FOLDER_NAME, FUNC_DATA_NAME, ANAT_FOLDER_NAME, ANAT_DATA_NAME, D) This is typically the first step in a neuroimaging pipeline, ensuring all required files exist and have consistent properties before processing begins. Input Arguments: OUTPUT_FOLDER - Path to the directory where the
  - Internal calls detected: `my_writetable`, `whifun_check_data_anat`, `whifun_check_data_func`, `whifun_create_fields`, `whifun_initialise_manual_motion_error_fields`, `whifun_isnan_or_empty`
  - External dependencies detected: MATLAB table/file I/O, ANTs command-line suite

## Function: `whifun_check_data()`
- **Functional Purpose:** WHIFUN_CHECK_DATA Performs an initial, comprehensive check on fMRI and anatomical data files for all subjects in a list, recording key metadata and flagging missing files. [REPORT, N_IMAGE, TR, VOXEL_FUNC, VOXEL_ANAT, MIS_DATA, SUBJ_LIST_ALL] = ... WHIFUN_CHECK_DATA(OUTPUT_FOLDER, SUBJ_LIST_ALL, COMM_SESS_NAME, FUNC_FOLDER_NAME, FUNC_DATA_NAME, ANAT_FOLDER_NAME, ANAT_DATA_NAME, D) This is typically the first step in a neuroimaging pipeline, ensuring all required files exist and have consistent properties before processing begins. Input Arguments: OUTPUT_FOLDER - Path to the directory where the updated subject list CSV will be saved. SUBJ_LIST_ALL - The master structure array containing subje
- **Arguments:**
  - `output_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_all` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `comm_sess_name` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_folder_name` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_data_name` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_folder_name` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_data_name` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `d` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
