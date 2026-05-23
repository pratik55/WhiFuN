# load_subjects_bad

**Source:** `whifun_functions/load_subjects_bad.m:1`

## Signature

```matlab
function Subj_list = load_subjects_bad(folder,name)
```

## Summary

LOAD_SUBJECTS_BAD Loads the Subjects that wont be preprocessed or analysed due to error, Motion exclusion or Manual rejection list of subjects from a CSV file.

## Syntax

```matlab
[Subj_list, rm] = LOAD_SUBJECTS_BAD(folder, name) loads a CSV file
```

## Description

named 'name' from the specified 'folder'. It returns a structure array 'Subj_list' containing the subject data. The function loads subjects marked with 'error', 'motion_ex', or 'manual_ex'.

## Input Arguments

### `folder`
The folder path where the CSV file is located (char or string).

### `name`
The name of the CSV file (char or string).

## Output Arguments

### `Subj_list`
A structure array containing the subject data after filtering. Each row of the CSV becomes a structure in the array.

## Examples

Example: % Load bad subjects from 'subject_data.csv' in the current folder [subjects, removed] = load_subjects_bad(pwd, 'subject_data.csv');

See also READTABLE, TABLE2STRUCT, DETECTIMPORTOPTIONS.

## Author

Author: Pratik Jain
