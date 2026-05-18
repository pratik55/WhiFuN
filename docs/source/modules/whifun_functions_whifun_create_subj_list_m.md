- **Key Features:**
  - WHIFUN_CREATE_SUBJ_LIST Interactively creates a subject list structure. [Subj_list_all, output_folder] = WHIFUN_CREATE_SUBJ_LIST(output_folder) provides a user-friendly, GUI-based tool for setting up a subject list structure for a preprocessing pipeline. The function guides the user through selecting data, defining patterns for files, and validating the paths for each subject. The function performs the following steps: 1. **Select Folders**: It prompts the user to select an output folder and a main data folder containing all subject directories. 2. **Subject Selection**: It offers options to s
  - Internal calls detected: `my_writetable`, `whifun_create_fields`
  - External dependencies detected: MATLAB App Designer, MATLAB table/file I/O

## Function: `whifun_create_Subj_list()`
- **Functional Purpose:** WHIFUN_CREATE_SUBJ_LIST Interactively creates a subject list structure. [Subj_list_all, output_folder] = WHIFUN_CREATE_SUBJ_LIST(output_folder) provides a user-friendly, GUI-based tool for setting up a subject list structure for a preprocessing pipeline. The function guides the user through selecting data, defining patterns for files, and validating the paths for each subject. The function performs the following steps: 1. **Select Folders**: It prompts the user to select an output folder and a main data folder containing all subject directories. 2. **Subject Selection**: It offers options to select subjects from the main data folder, either by selecting all, using a wildcard pattern, or manu
- **Arguments:**
  - `output_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `dataFolder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `choice` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `finalData` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
