# whifun_plot_freqz

**Source:** `whifun_functions/whifun_plot_freqz.m:1`

## Signature

```matlab
function whifun_plot_freqz(b,a,Fs)
```

## Summary

WHIFUN_PLOT_FREQZ Plots the frequency response of a digital filter.

## Syntax

```matlab
WHIFUN_PLOT_FREQZ(b, a, Fs) generates a two-part plot showing the
```

## Description

magnitude and phase response of a digital filter. This function is a utility for visualizing the characteristics of a filter, such as a Butterworth bandpass filter used in fMRI preprocessing.

The function uses MATLAB's `freqz` function to calculate the frequency response and then plots the magnitude (how much the filter amplifies or attenuates a given frequency) and phase (the phase shift applied to a frequency). The frequency axis is displayed in Hz.

## Input Arguments

### `b`
The numerator coefficients of the filter transfer function.

### `a`
The denominator coefficients of the filter transfer function.

### `Fs`
The sampling frequency in Hz (e.g., 1/TR for fMRI data). See also FREQZ, SUBPLOT, PLOT, GRID ON, XLABEL, YLABEL, TITLE.

## Author

Author: Pratik Jain
