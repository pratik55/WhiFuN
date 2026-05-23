# whifun_create_Subj_list_gui

Source: `whifun_functions/whifun_create_Subj_list_gui.m:1`

```matlab
function [Subj_list_all,output_folder] = whifun_create_Subj_list_gui(output_folder,dataFolder,choice,finalData)
```

## MATLAB Help

WHIFUN_CREATE_SUBJ_LIST_GUI Interactively creates a subject list structure.

  [Subj_list_all, output_folder] = WHIFUN_CREATE_SUBJ_LIST(output_folder)
  provides a user-friendly, GUI-based tool for setting up a subject list
  structure for a preprocessing pipeline. The function guides the user
  through selecting data, defining patterns for files, and validating the
  paths for each subject.

  The function performs the following steps:
  1.  **Select Folders**: It prompts the user to select an output folder
      and a main data folder containing all subject directories.
  2.  **Subject Selection**: It offers options to select subjects from the
      main data folder, either by selecting all, using a wildcard pattern,
      or manually picking from a list.
  3.  **Define Patterns**: A graphical user interface (GUI) is displayed,
      where the user can define patterns (relative to the subject folder)
      for various files generated or used during the preprocessing pipeline
      (e.g., segmented tissue files, masks, normalized data).
  4.  **Populate Structure**: It iterates through each subject, attempting
      to find files matching the defined patterns. It populates a structure
      array `Subj_list_all` with the full paths to these files.
  5.  **Error Handling**: If a pattern results in zero or multiple matches
      for a subject, it issues a warning. This helps the user identify and
      fix potential naming inconsistencies in their data.
  6.  **Save Output**: The final subject list structure is converted to a
      table and saved as a `Subj_list.csv` file in the specified output folder.

  This function streamlines the initial setup of a preprocessing pipeline,
  making it less prone to manual errors and more adaptable to different
  data organization schemes.

  Input Arguments:
  output_folder - (Optional) The path to the directory where the output
                  CSV file will be saved. If not provided, a dialog box
                  prompts the user to select one.
  data_folder   - (Optional) The path to the directory where the output
                  CSV file will be saved. If not provided, a dialog box
                  prompts the user to select one.
  choice        - (Optional) How do you want to select subject folders? Options:
                                          'All'    : Select All Subjects
                                          'Pattern': Wild Card pattern to select subjects
                                          'Manual' : Manully Select subjects
  finalData     - (Optional) A cell structure that has information about
                  the patterns corresponding to the different fields in Subj_list.csv
                  file. (Can be created using the whifun_create_preproc_files_cell
                  function)

  Output Arguments:
  Subj_list_all - A structure array where each element represents a subject
                  and contains the full file paths for the specified fields.
  output_folder - The path to the selected output directory.

  Author: Pratik Jain
  See also UIGETDIR, UITALBE, INPUTDLG, DIR, FULLFILE.
