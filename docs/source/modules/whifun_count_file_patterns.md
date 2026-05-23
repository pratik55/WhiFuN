# whifun_count_file_patterns

Source: `whifun_functions/whifun_count_file_patterns.m:1`

```matlab
function pattern_table = whifun_count_file_patterns(dataset_path)
```

## MATLAB Help

WHIFUN_COUNT_FILE_PATTERNS Audits dataset structure by counting file naming patterns.

  Author: Pratik Jain

  This function recursively scans a directory and identifies unique file 
  naming patterns by abstracting subject-specific IDs (sub-XXXX) into 
  wildcards (sub*). It is designed to validate BIDS-compliant datasets.

  INPUTS:
      dataset_path - String. The root directory of your fMRI dataset.

  OUTPUTS:
      pattern_table - A table containing:
          * Name: The abstracted file path and pattern.
          * Value: The total count of files matching that pattern.

  EXAMPLE:
      % Check if all 20 subjects have their MNI-space bold files
      audit = whifun_count_file_patterns('/data/project/derivatives/fmriprep');

  See also DIR, REGEXPREP, CONTAINERS.MAP.
  Author: Pratik Jain
