# whifun_parse_bids_filename

Source: `whifun_functions/whifun_parse_bids_filename.m:1`

```matlab
function info = whifun_parse_bids_filename(fname)
```

## MATLAB Help

WHIFUN_PARSE_BIDS_FILENAME
Extract BIDS/fMRIPrep entities from a filename

INPUT
  fname : string or char

OUTPUT
  info : struct with fields:
         sub, ses, task, run, space, desc, suffix, extension
