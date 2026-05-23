# update_csv

Source: `whifun_functions/update_csv.m:1`

```matlab
function Subj_list_all = update_csv(Subj_list_subji,Subj_list_all,output_folder)
```

## MATLAB Help

UPDATE_CSV Updates Subj_list structure with new information for a
  specific subject and saves the entire list to a CSV file.

  SUBJ_LIST_ALL = UPDATE_CSV(SUBJ_LIST_SUBJI, SUBJ_LIST_ALL, OUTPUT_FOLDER)

  This utility function is typically used in a processing pipeline to
  record the status and results (e.g., motion metrics, processing time,
  error flags) for one subject into the complete subject list.

  Input Arguments:
  SUBJ_LIST_SUBJI - A structure representing a single subject, containing
                    the updated fields to be transferred (e.g., `motion_ex`,
                    `error`, `nt_dis`, `time_preprocess_min`). Must have a
                    `name` field for matching.
  SUBJ_LIST_ALL   - The master structure array containing data for all subjects.
  OUTPUT_FOLDER   - The path to the folder where the updated CSV file
                    ("Subj_list.csv") will be saved.

  Output Arguments:
  SUBJ_LIST_ALL   - The updated master structure array.

  Dependencies: 'my_writetable'

  Author: Pratik Jain
