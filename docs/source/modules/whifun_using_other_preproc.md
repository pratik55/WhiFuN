# whifun_using_other_preproc

Source: `whifun_functions/whifun_using_other_preproc.m:1`

```matlab
function whifun_using_other_preproc(output_folder,only_data_check)
```

## MATLAB Help

WHIFUN_USING_OTHER_PREPROC Runs QC on data preprocessed by other software.

  WHIFUN_USING_OTHER_PREPROC(output_folder) provides a streamlined workflow
  for performing quality control checks on fMRI data that has been not
  been preprocessed using WhiFuN.

  This function guides the user through the process of creating a subject
  list and then generating a series of quality control plots. It is
  designed to be a flexible entry point for users who want to leverage
  the QC capabilities of this toolbox without running the entire
  preprocessing pipeline.

  The function performs the following steps:
  1. **Create Subject List**: It calls `whifun_create_Subj_list` to
     interactively generate a structured subject list. This list links
     each subject to their preprocessed functional and anatomical files.
  2. **Data Check**: It validates the existence of the specified files
     and extracts key metadata like the number of volumes (n_image) and
     voxel dimensions. It then generates a summary report and plots.
  3. **Run QC**: It iterates through each subject in the list and calls
     the `whifun_qc` function to generate a full suite of quality control
     plots. These plots cover various aspects of the data, such as motion,
     normalization, and functional connectivity sanity checks.

  This workflow is ideal for users who want to verify the quality of their
  preprocessed data before proceeding with advanced analysis.

  Input Arguments:
  output_folder   - (Optional) The directory to save all output. If not
                    provided, a dialog box prompts the user to select one.
  only_data_check - (Optional) A flag to only run the initial data check
                    without generating all the QC plots. Defaults to 1.

  Author: Pratik Jain
  See also WHIFUN_CREATE_SUBJ_LIST, WHIFUN_CHECK_DATA, WHIFUN_PLOT_DATA_CHECK_FIGURES, WHIFUN_QC.
