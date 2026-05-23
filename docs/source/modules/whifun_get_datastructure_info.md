# whifun_get_datastructure_info

Source: `whifun_functions/whifun_get_datastructure_info.m:1`

```matlab
function summary = whifun_get_datastructure_info(dataDir, funcPattern, anatPattern, varargin)
```

## MATLAB Help

WHIFUN_GET_DATASTRUCTURE_INFO Audits data directory to check for functional and anatomical files.

  summary = WHIFUN_GET_DATASTRUCTURE_INFO(dataDir, funcPattern, anatPattern)
  scans a study root directory, loops through individual subject folders, and 
  looks into intermediate session directories (e.g., BAS1, BAS2). It recursively 
  checks for the existence of files matching the functional and anatomical 
  string patterns.

  The function prints a neatly formatted console breakdown grouped by 
  intermediate folder types, showing:
      - Total directories scanned per session type
      - "Complete" count (both functional and anatomical files exist)
      - "Missing Part" count (either functional, anatomical, or both are missing)

  Inputs:
      dataDir     - String or char array of the root directory containing 
                    subject folders (e.g., 'C:\MyStudy\Data').
      funcPattern - String/char wildcard pattern for functional images 
                    (e.g., 'f*.nii' or 'func.nii').
      anatPattern - String/char wildcard pattern for anatomical images 
                    (e.g., 'co*.nii' or 'T1.nii').
      varargin    - Optional arguments (reserved for pipeline expansion).

  Outputs:
      summary     - A MATLAB table containing columns: 
                    {'Subject', 'FolderType', 'Has_Func', 'Has_Anat'} 
                    providing a row-by-row audit trail for every session.

  Example:
      % Scan data directory for raw NIfTI files across sessions
      auditTable = whifun_get_datastructure_info('D:\MRI_Data', 'bold*.nii', 'T1*.nii');
  Author: Pratik Jain
