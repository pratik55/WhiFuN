# whifun_parse_bids_filename

**Source:** `whifun_functions/whifun_parse_bids_filename.m:1`

## Signature

```matlab
function info = whifun_parse_bids_filename(fname)
```

## Summary

WHIFUN_PARSE_BIDS_FILENAME

## Description

Extract BIDS/fMRIPrep entities from a filename

INPUT fname : string or char

OUTPUT info : struct with fields: sub, ses, task, run, space, desc, suffix, extension
