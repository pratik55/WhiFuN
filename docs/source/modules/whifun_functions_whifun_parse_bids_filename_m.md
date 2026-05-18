- **Key Features:**
  - WHIFUN_PARSE_BIDS_FILENAME Extract BIDS/fMRIPrep entities from a filename INPUT fname : string or char OUTPUT info : struct with fields: sub, ses, task, run, space, desc, suffix, extension
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_parse_bids_filename()`
- **Functional Purpose:** WHIFUN_PARSE_BIDS_FILENAME Extract BIDS/fMRIPrep entities from a filename INPUT fname : string or char OUTPUT info : struct with fields: sub, ses, task, run, space, desc, suffix, extension
- **Arguments:**
  - `fname` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `extract_entity()`
- **Functional Purpose:** Extract BIDS entity value (e.g., sub-01 → 01)
- **Arguments:**
  - `str` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `key` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `extract_suffix()`
- **Functional Purpose:** Extract BIDS suffix (e.g., bold, T1w)
- **Arguments:**
  - `str` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
