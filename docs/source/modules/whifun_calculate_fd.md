# whifun_calculate_fd

Source: `whifun_functions/whifun_calculate_fd.m:1`

```matlab
function fd = whifun_calculate_fd(motion)
```

## MATLAB Help

WHIFUN_CALCULATE_FD Calculates framewise displacement (FD).

  fd = WHIFUN_CALCULATE_FD(motion) computes the framewise displacement (FD)
  from motion parameters. FD is a measure of head motion between
  consecutive time points in an fMRI scan.

  This function takes either the path to a motion parameter text file
  (as a string or `dir` structure) or the motion parameters directly (as
  a numeric matrix). It then calculates the vector difference between each
  time point. The rotational parameters are converted to millimeters by
  assuming a brain radius of 50mm, and the absolute sum of all six
  derivative parameters is returned as the FD time series.

  This function is a core part of quality control for fMRI data, as high
  FD values indicate excessive motion that may require subject exclusion
  or data scrubbing.

  Input Arguments:
  motion - The path to the motion parameter `.txt` file (string or `dir`
           structure), or a numeric matrix of motion parameters.

  Output Arguments:
  fd - A vector of framewise displacement values, where each element
       corresponds to a time point (starting from the second time point).

  Example:
     % Assuming 'rp_file.txt' is the motion parameter file
     % fd_values = whifun_calculate_fd('path_to_rp_file.txt');

     % Or, pass the matrix directly
     % motion_matrix = load('path_to_rp_file.txt');
     % fd_values = whifun_calculate_fd(motion_matrix);

  Author: Pratik Jain
  See also DIR, LOAD, DIFF.
