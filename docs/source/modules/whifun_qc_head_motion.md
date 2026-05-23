# whifun_qc_head_motion

Source: `whifun_functions/whifun_qc_head_motion.m:1`

```matlab
function whifun_qc_head_motion(out_folder,realigned_func_native,name,max_fd,mean_fd,greater_than_20,over_write,motion_txt)
```

## MATLAB Help

WHIFUN_QC_HEAD_MOTION Generates a quality control figure for head motion.

  WHIFUN_QC_HEAD_MOTION(out_folder, realigned_func_native, ..., motion_txt)
  creates a comprehensive quality control report for head motion for a single
  subject. The report consists of four plots combined into a single figure.

  The function performs the following steps:
  1.  **Check Existence**: It checks if a head motion QC image already exists
      and, based on the `over_write` flag, either skips or generates a new
      one.
  2.  **Calculate Metrics**: It reads the realigned functional data and the
      motion parameter file. It then calculates:
      -   **Global Mean**: The scaled global signal mean over time.
      -   **Pairwise Variance**: A measure of voxel-wise signal change
          between consecutive time points.
      -   **Framewise Displacement (FD)**: A composite measure of motion
          combining translations and rotations.
  3.  **Plotting**: It creates a figure with four subplots:
      -   **Global Mean**: A plot of the scaled global mean over time.
      -   **Pairwise Variance**: A plot of the pairwise variance with a
          line indicating 3 standard deviations above the mean.
      -   **Rigid Body Motion**: A plot of the 6 rigid body motion parameters
          (3 translations and 3 rotations).
      -   **Framewise Displacement**: A plot of the FD with lines showing
          the thresholds used for quality control.
  4.  **Export**: The figure is saved as a `.png` file in the specified
      output folder.

  Input Arguments:
  out_folder             - The path to the quality control directory for saving the figure.
  realigned_func_native  - The full path to the realigned functional file.
  name                   - The subject's name.
  max_fd                 - The maximum FD threshold.
  mean_fd                - The mean FD threshold.
  greater_than_20        - The FD threshold for the percentage of excluded volumes.
  over_write             - (Optional) A logical value (0 or 1) to force overwriting.
  motion_txt             - (Optional) A matrix of motion parameters to plot instead
                           of reading from the `Subj_list_1.motion_txt` path.

  Author: Pratik Jain
  See also NIFTIREAD, RESHAPE, MEAN, PLOT, SUBPLOT, TITLE, LEGEND, EXPORTGRAPHICS.
