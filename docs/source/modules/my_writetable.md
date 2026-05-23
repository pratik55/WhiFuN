# my_writetable

Source: `whifun_functions/my_writetable.m:1`

```matlab
function my_writetable(Subj_list_all_table,path)
```

## MATLAB Help

MY_WRITETABLE Writes a WhiFuN Subj_list to a CSV, with robust
  error handling for common issues like open files.

  MY_WRITETABLE(SUBJ_LIST_ALL_TABLE, PATH)

  This function is a wrapper around MATLAB's built-in `writetable`
  that first attempts to remove common metadata fields (like those from a
  `dir` structure) from the table before writing. It also includes specific
  error handling for the case where the output file is currently open and
  locked by another application.

  Input Arguments:
  SUBJ_LIST_ALL_TABLE - The MATLAB table object to be written to disk.
  PATH                - The full file path and name where the table should be saved
                        (e.g., 'C:\data\Subj_list.csv').

  Error Handling:
  - Attempts to catch and handle the 'MATLAB:table:write:FileOpenError'
    which occurs when the file is locked (e.g., open in Excel). It prompts
    the user to close the file and retry.
  - Catches other errors, prints detailed error information to the command
    window (including identifier, message, and stack trace), and terminates
    execution with an error.

  Author: Pratik Jain
