- **Key Features:**
  - WHIFUN_COUNT_FILE_PATTERNS Audits dataset structure by counting file naming patterns. Author: Pratik Jain This function recursively scans a directory and identifies unique file naming patterns by abstracting subject-specific IDs (sub-XXXX) into wildcards (sub*). It is designed to validate BIDS-compliant datasets. INPUTS: dataset_path - String. The root directory of your fMRI dataset. OUTPUTS: pattern_table - A table containing: * Name: The abstracted file path and pattern. * Value: The total count of files matching that pattern. EXAMPLE: % Check if all 20 subjects have their MNI-space bold fil
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_count_file_patterns()`
- **Functional Purpose:** WHIFUN_COUNT_FILE_PATTERNS Audits dataset structure by counting file naming patterns. Author: Pratik Jain This function recursively scans a directory and identifies unique file naming patterns by abstracting subject-specific IDs (sub-XXXX) into wildcards (sub*). It is designed to validate BIDS-compliant datasets. INPUTS: dataset_path - String. The root directory of your fMRI dataset. OUTPUTS: pattern_table - A table containing: * Name: The abstracted file path and pattern. * Value: The total count of files matching that pattern. EXAMPLE: % Check if all 20 subjects have their MNI-space bold files audit = whifun_count_file_patterns('/data/project/derivatives/fmriprep'); See also DIR, REGEXPREP
- **Arguments:**
  - `dataset_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
