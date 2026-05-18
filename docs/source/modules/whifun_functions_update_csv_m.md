- **Key Features:**
  - UPDATE_CSV Updates Subj_list structure with new information for a specific subject and saves the entire list to a CSV file. SUBJ_LIST_ALL = UPDATE_CSV(SUBJ_LIST_SUBJI, SUBJ_LIST_ALL, OUTPUT_FOLDER) This utility function is typically used in a processing pipeline to record the status and results (e.g., motion metrics, processing time, error flags) for one subject into the complete subject list. Input Arguments: SUBJ_LIST_SUBJI - A structure representing a single subject, containing the updated fields to be transferred (e.g., `motion_ex`, `error`, `nt_dis`, `time_preprocess_min`). Must have a `n
  - Internal calls detected: `my_writetable`
  - External dependencies detected: MATLAB table/file I/O

## Function: `update_csv()`
- **Functional Purpose:** UPDATE_CSV Updates Subj_list structure with new information for a specific subject and saves the entire list to a CSV file. SUBJ_LIST_ALL = UPDATE_CSV(SUBJ_LIST_SUBJI, SUBJ_LIST_ALL, OUTPUT_FOLDER) This utility function is typically used in a processing pipeline to record the status and results (e.g., motion metrics, processing time, error flags) for one subject into the complete subject list. Input Arguments: SUBJ_LIST_SUBJI - A structure representing a single subject, containing the updated fields to be transferred (e.g., `motion_ex`, `error`, `nt_dis`, `time_preprocess_min`). Must have a `name` field for matching. SUBJ_LIST_ALL - The master structure array containing data for all subjects
- **Arguments:**
  - `Subj_list_subji` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_all` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `output_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
