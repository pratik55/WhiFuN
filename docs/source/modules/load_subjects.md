# load_subjects

**Source:** `whifun_functions/load_subjects.m:1`

## Signature

```matlab
function [Subj_list,rm] = load_subjects(folder,name,first)
```

## Summary

LOAD_SUBJECTS Loads a list of subjects from a CSV file.

## Syntax

```matlab
[Subj_list, rm] = LOAD_SUBJECTS(folder, name) loads a CSV file
[Subj_list, rm] = LOAD_SUBJECTS(folder, name, first) allows for
```

## Description

named 'name' from the specified 'folder'. It returns a structure array 'Subj_list' containing the subject data and a logical array 'rm' indicating which rows were removed. The function automatically removes subjects marked with 'error', 'motion_ex', or 'manual_ex'.

different behavior on the first run. If 'first' is true (1), the function initializes new 'error' and 'motion_ex' columns with zeros and only removes subjects marked with 'manual_ex'. This is useful for initial data processing runs.

## Input Arguments

### `folder`
The folder path where the CSV file is located (char or string).

### `name`
The name of the CSV file (char or string).

### `first`
(Optional) A logical value. If true, it performs a "first run" initialization. Defaults to false if not provided.

## Output Arguments

### `Subj_list`
A structure array containing the subject data after filtering. Each row of the CSV becomes a structure in the array.

### `rm`
A logical array indicating which rows were removed based on the exclusion criteria.

## Examples

Example: % Load subjects from 'subject_data.csv' in the current folder [subjects, removed] = load_subjects(pwd, 'subject_data.csv');

See also READTABLE, TABLE2STRUCT, DETECTIMPORTOPTIONS.

## Author

Author: Pratik Jain
