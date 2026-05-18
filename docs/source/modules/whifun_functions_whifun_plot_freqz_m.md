- **Key Features:**
  - WHIFUN_PLOT_FREQZ Plots the frequency response of a digital filter. WHIFUN_PLOT_FREQZ(b, a, Fs) generates a two-part plot showing the magnitude and phase response of a digital filter. This function is a utility for visualizing the characteristics of a filter, such as a Butterworth bandpass filter used in fMRI preprocessing. The function uses MATLAB's `freqz` function to calculate the frequency response and then plots the magnitude (how much the filter amplifies or attenuates a given frequency) and phase (the phase shift applied to a frequency). The frequency axis is displayed in Hz. Input Argu
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: Signal Processing Toolbox

## Function: `whifun_plot_freqz()`
- **Functional Purpose:** WHIFUN_PLOT_FREQZ Plots the frequency response of a digital filter. WHIFUN_PLOT_FREQZ(b, a, Fs) generates a two-part plot showing the magnitude and phase response of a digital filter. This function is a utility for visualizing the characteristics of a filter, such as a Butterworth bandpass filter used in fMRI preprocessing. The function uses MATLAB's `freqz` function to calculate the frequency response and then plots the magnitude (how much the filter amplifies or attenuates a given frequency) and phase (the phase shift applied to a frequency). The frequency axis is displayed in Hz. Input Arguments: b - The numerator coefficients of the filter transfer function. a - The denominator coefficie
- **Arguments:**
  - `b` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `a` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Fs` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
