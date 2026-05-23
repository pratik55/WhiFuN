# whifun_count_file_patterns

**Source:** `whifun_functions/whifun_count_file_patterns.m:1`

## Signature

```matlab
function pattern_table = whifun_count_file_patterns(dataset_path)
```

## Summary

WHIFUN_COUNT_FILE_PATTERNS Audits dataset structure by counting file naming patterns.

## Description

This function recursively scans a directory and identifies unique file naming patterns by abstracting subject-specific IDs (sub-XXXX) into wildcards (sub*). It is designed to validate BIDS-compliant datasets.

## Input Arguments

### `dataset_path`
String. The root directory of your fMRI dataset.

## Output Arguments

### `pattern_table`
A table containing: * Name: The abstracted file path and pattern. * Value: The total count of files matching that pattern.

## Examples

EXAMPLE: % Check if all 20 subjects have their MNI-space bold files audit = whifun_count_file_patterns('/data/project/derivatives/fmriprep');

See also DIR, REGEXPREP, CONTAINERS.MAP.

## Author

Author: Pratik Jain
Author: Pratik Jain
