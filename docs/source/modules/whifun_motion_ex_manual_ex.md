# whifun_motion_ex_manual_ex

**Source:** `whifun_functions/whifun_motion_ex_manual_ex.m:1`

## Signature

```matlab
function Subj_list_1 = whifun_motion_ex_manual_ex(Subj_list_1)
```

## Summary

WHIFUN_MOTION_EX_MANUAL_EX Initializes or validates subject exclusion flags

## Syntax

```matlab
SUBJ_LIST_1 = WHIFUN_MOTION_EX_MANUAL_EX(SUBJ_LIST_1)
```

## Description

for motion-based or manual exclusion.

This utility function ensures that the `motion_ex` (motion exclusion) and `manual_ex` (manual exclusion) fields exist in the subject structure and are initialized to 0 (meaning the subject is *included*) if they are either missing or empty. It also initializes an `error` flag to 0.

## Input Arguments

### `SUBJ_LIST_1`
A scalar structure containing a single subject's information. Must contain the field 'name'.

## Output Arguments

### `SUBJ_LIST_1`
The updated structure with the following fields ensured:
- .error: Initialized to
0.
- .motion_ex: Initialized to 0 if missing or empty.
- .manual_ex: Initialized to 0 if missing or empty.

## Author

Author: Pratik Jain
