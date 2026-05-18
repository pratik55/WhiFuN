- **Key Features:**
  - Properties that correspond to app components
  - Internal calls detected: `BrainNet_MapCfg_WhifuN`, `dice_iou`, `freq_per_band`, `load_subjects`, `load_subjects_all`, `motion_threshold_select`, `my_writetable`, `PCA_regression_parameters`, `rerunpreproc`, `Sub_info`, `Subject_data_folder_details`, `uigetfile_n_dir`, `update_csv`, `whifun_addpath_and_create_preproc_folders`, `whifun_check_data`, `whifun_create_avg_ts`, `whifun_create_fields_preproc`, `whifun_create_file`, `whifun_create_FN_Kmeans`, `whifun_create_FN_Kmeans_WM_GM`, `whifun_create_group_mask`, `whifun_create_Subj_list_all_from_Subj_folder_details`, `whifun_dartel`, `whifun_dartel_normalize_smooth`, `whifun_delete`, `whifun_dir`, `whifun_display_FC`, `whifun_niftiread`, `whifun_plot_data_check_figures`, `whifun_preproc` plus 7 more
  - External dependencies detected: MATLAB App Designer, MATLAB NIfTI I/O, MATLAB table/file I/O, Parallel Computing Toolbox, SPM12, ANTs command-line suite, BrainNet Viewer, SLover/MarsBaR-style visualization helpers

## Function: `main()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - No explicit input arguments.

## Function: `load_param()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `load_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `load_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `load_subjects_dropdown()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `select_by` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `load_subjects_dropdown2()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `save_param()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `save_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `save_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `get_symettry()`
- **Functional Purpose:** separating the left and right sides of the clustering solutions, and flipping the right side, for whifun_direct comparison to the left
- **Arguments:**
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `current_clustering_solution` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `get_symettry_indi()`
- **Functional Purpose:** separating the left and right sides of the clustering solutions, and flipping the right side, for whifun_direct comparison to the left
- **Arguments:**
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `current_clustering_solution` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `tooltip()`
- **Functional Purpose:** addpaths
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ParticipantDatafolderButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `OutputsfolderButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `SaveParametersButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `LoadParametersButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `RunPreprocessingButtonPushed()`
- **Functional Purpose:** % This code written by Pratik Jain. % This code was written with the help of different preprocessing scripts given by % Dr. Xin Di, Dr. Rakibul Hafeez, Dr. Wang Pan, Donna Chen and Wonbum Sohn % Under guidance of Dr Andrew Micheal and Dr. Bharat Biswal. % Defining Important paths and Creating Output whifun_directories
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `RunDataCheckButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `BIDSCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NuisanceRegressionDropDownValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DisplayFNButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DisplayFCButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CreateGroupMasksButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `WMGroupMaskButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `WMFNTabButtonDown()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CreateWMFNButtonPushed()`
- **Functional Purpose:** % Clustering WM Functional networks
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `GMFNTabButtonDown()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `GMGroupMaskButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CreateGMFNButtonPushed()`
- **Functional Purpose:** % Clustering GM Functional networks
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `StatisticsButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CompareFNButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `FilterCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `FrequenciesperbandButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ExtractROITImeseriesButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NetworksAtlasButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `SelectParticipantsButtonPushed()`
- **Functional Purpose:** if ~isempty(app.DataPathTextArea.Value) data_path = app.DataPathTextArea.Value; output_folder = end
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DataPathTextAreaValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `QCcheckdoneCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CheckFNSymettryButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `manuallycoregisterparticipantsButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DetermineFramewiseDisplacementthresholdsButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DeletePreprocessingfilesfromaparticularstepButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ParticipantsInfoButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `AllfoldersareParticipantsCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ManuallyexcludeparticipantsCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `DataPathTextArea_2ValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `OverwriteexistingfilesCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ParellelProcessingCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `QCviewerButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `frequencyspecificCheckBoxValueChanged()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CreateWMGMFNButtonPushed()`
- **Functional Purpose:** % Clustering GM Functional networks
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CheckMaskButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CheckMaskButton_2Pushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `CheckatlasButtonPushed()`
- **Functional Purpose:** Properties that correspond to app components
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `event` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `createComponents()`
- **Functional Purpose:** Get the file path for locating images
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `main()`
- **Functional Purpose:** Create UIFigure and components
- **Arguments:**
  - No explicit input arguments.

## Function: `delete()`
- **Functional Purpose:** Delete UIFigure when app is deleted
- **Arguments:**
  - `app` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
