# whifun_build_net

Source: `whifun_functions/whifun_build_net.m:1`

```matlab
function [build_net,K] = whifun_build_net(cluster_folder,out_pattern,over_write)
```

## MATLAB Help

WHIFUN_BUILD_NET Manages the decision process for building Functional Networks (FNs).

  [BUILD_NET, K] = WHIFUN_BUILD_NET(CLUSTER_FOLDER, OUT_PATTERN, OVER_WRITE)

  This function checks if previously clustered FN files exist in the
  specified folder. If files are found, it prompts the user to either
  rebuild the networks or select an existing cluster solution (K value)
  to proceed with.

  Input Arguments:
  CLUSTER_FOLDER - Full path to the directory where FN cluster results are stored.
  OUT_PATTERN    - The filename pattern used for the clustered NIfTI files
                   (e.g., 'WM_FN_K*.nii', where * is the K value).
  OVER_WRITE     - (Optional, default 0) Flag to bypass prompts if set to 1.

  Output Arguments:
  BUILD_NET      - Flag indicating whether the networks should be built now:
                   BUILD_NET = 1: Proceed with network building.
                   BUILD_NET = 0: Skip building, proceed with existing K.
  K              - The number of networks (clusters) to proceed with:
                   K = 0: If BUILD_NET = 1 (K will be determined later).
                   K = K_old: If BUILD_NET = 0 (using a previously computed K).

  Dependencies: 'whifun_create_file', 'questdlg', 'inputdlg' functions.

  Author: Pratik Jain
