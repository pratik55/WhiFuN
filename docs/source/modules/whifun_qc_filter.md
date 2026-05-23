# whifun_qc_filter

Source: `whifun_functions/whifun_qc_filter.m:1`

```matlab
function whifun_qc_filter(out_folder,Subj_list_1,over_write,filter_freq_response_flag,filter_lp,filter_hp)
```

## MATLAB Help

WHIFUN_QC_FILTER Generates quality control figures for the filtering step.

  WHIFUN_QC_FILTER(out_folder, Subj_list_1, over_write, filter_freq_response_flag, filter_lp, filter_hp)
  creates visual quality control reports to assess the effectiveness of
  the bandpass filtering applied to functional data.

  The function performs the following steps:
  1.  **Check Existence**: It checks if the output plots already exist and,
      based on the `over_write` flag, either skips or generates new ones.
      The output includes up to two figures.
  2.  **Global Time Series Plot**: It plots the mean global time series of
      the functional data *before* and *after* filtering. The global mean
      is calculated across all voxels at each time point. The plot, with
      the mean subtracted, visually demonstrates the removal of
      low-frequency drift and high-frequency noise.
  3.  **Frequency Response Plot**: If `filter_freq_response_flag` is true,
      it calculates the frequency response of the Butterworth filter that was
      used. This plot provides a technical verification of the filter's design.
      It uses an assumed helper function `whifun_plot_freqz` for this purpose.
  4.  **Export**: All generated plots are saved as PNG files in a dedicated
      quality control directory.

  Input Arguments:
  out_folder                 - The root directory for saving all QC output.
  Subj_list_1                - A single subject structure with `nuisance_regressed`
                               and `filtered` file paths, and `TR`.
  over_write                 - A logical value (0 or 1) to force overwriting existing
                               QC images.
  filter_freq_response_flag  - A logical flag (0 or 1) to generate the
                               frequency response plot.
  filter_lp                  - (Optional) The low-pass cutoff frequency of the filter in Hz.
  filter_hp                  - (Optional) The high-pass cutoff frequency of the filter in Hz.

  Author: Pratik Jain
  See also WHIFUN_CREATE_FILE, NIFTIREAD, FIGURE, PLOT, LEGEND, EXPORTGRAPHICS.
