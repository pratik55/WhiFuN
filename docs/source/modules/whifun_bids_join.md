# whifun_bids_join

**Source:** `whifun_functions/whifun_bids_join.m:1`

## Signature

```matlab
function out = whifun_bids_join(varargin)
```

## Summary

WHIFUN_BIDS_JOIN Joins multiple strings into an underscore-separated BIDS name.

## Syntax

```matlab
OUT = WHIFUN_BIDS_JOIN(STR1, STR2, ...) takes a variable number of
```

## Description

input strings or character arrays and concatenates them using an underscore ('_') delimiter. Empty inputs are automatically ignored.

## Input Arguments

### `varargin`
Any number of string or character array inputs (e.g., 'sub-01', 'ses-pre', 'T1w').

## Output Arguments

### `out`
A single character array of joined elements.

## Examples

EXAMPLE: name = whifun_bids_join('sub-01', 'ses-01', '', 'T1w'); % returns: 'sub-01_ses-01_T1w'

See also JOIN, STRING, CHAR.
