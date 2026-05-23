# whifun_realignment

Source: `whifun_functions/whifun_realignment.m:1`

```matlab
function output = whifun_realignment(now_func_path,Realign_pre,nt)
```

## MATLAB Help

WHIFUN_REALIGNMENT Performs motion correction (realignment) using SPM.

  output = WHIFUN_REALIGNMENT(now_func_path, Realign_pre, nt)
  configures and executes the SPM realignment job to correct for head motion
  in a time series of functional images.

  This function creates an SPM batch job to:
  - **Estimate and Write**: Estimates the motion parameters and applies
    the transformations to create a new, realigned image series.
  - **Quality Settings**: Uses a high-quality estimation (`quality = 0.9`),
    a default separation, and a FWHM smoothing kernel of 5mm.
  - **Reference Image**: Registers all images to the first image in the
    series (`rtm = 0`).
  - **Interpolation**: Uses 2nd-degree B-spline for estimation and
    4th-degree B-spline for writing the resliced images.
  - **Masking**: Applies a mask to set out-of-bounds voxels to zero
    to handle interpolation artifacts from motion.
  - **Prefix**: Adds a specified prefix (`Realign_pre`) to the output
    realigned files.

  The function suppresses the SPM GUI and returns the log output.

  Input Arguments:
  now_func_path - A `dir` structure pointing to the functional NIfTI file.
  Realign_pre   - The prefix to use for the output realigned file (e.g., 'r').
  nt            - The number of time points in the functional image series.

  Output Arguments:
  output - A string containing the log output from the SPM jobman.

  Author: Pratik Jain
  See also SPM_JOBMAN, EVALC, FULLFILE.
