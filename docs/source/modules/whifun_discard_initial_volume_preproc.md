# whifun_discard_initial_volume_preproc

**Source:** `whifun_functions/whifun_discard_initial_volume_preproc.m:1`

## Signature

```matlab
function Subj_list_1 = whifun_discard_initial_volume_preproc(quality_control_path,Subj_list_1,in_func_path,out_func_path,n_vol_dis,over_write)
```

## Summary

WHIFUN_DISCARD_INITIAL_VOLUME Removes initial volumes from a functional scan.

## Description

discards a specified number of initial volumes (`n_vol_dis`) from a functional NIfTI file. This is a common step in fMRI preprocessing to allow for signal to stabilize.

The function first checks if the output file already exists and, based on the `over_write` flag, either uses the existing file or deletes it and creates a new one. It then reads the functional data, discards the initial volumes, and saves the new file. The subject structure is updated with the path to the new file and the new number of time points.

In case of an error during this process, the function catches the exception, sets the subject's `error` flag to 1, and logs the error to a file.

## Input Arguments

### `quality_control_path`
Path to the quality control directory for saving logs.

### `Subj_list_1`
A single subject structure to be updated.

### `in_func_path`
The path to the input functional NIfTI file.

### `out_func_path`
The desired path for the output file.

### `n_vol_dis`
The number of initial volumes to discard.

### `over_write`
(Optional) A logical value (0 or 1) to force overwriting the output file. Defaults to 0.

## Output Arguments

### `Subj_list_1`
The updated subject structure with the new `initial_vol_cut` file path and the updated `nt_dis` (number of time points after discarding).

## Examples

Example: % Discard 4 initial volumes from a functional scan % updated_subj = whifun_discard_initial_volume(qc_path, subj, in_path, out_path, 4);

See also WHIFUN_CREATE_FILE, NIFTIINFO, NIFTIREAD, NIFTISAVE, TRY, CATCH.

```matlab
Subj_list_1 = WHIFUN_DISCARD_INITIAL_VOLUME(quality_control_path, Subj_list_1, ..., over_write)
```

## Author

Author: Pratik Jain
