- **Key Features:**
  - Written by Pratik Jain WHIFUN_CHECK_FILTER_PARAMETERS Checks if filter cutoffs are correctly ordered. WHIFUN_CHECK_FILTER_PARAMETERS(filter_lp, filter_hp) checks if the low-pass filter cutoff frequency (`filter_lp`) is less than or equal to the high-pass filter cutoff frequency (`filter_hp`). If the condition `filter_lp > filter_hp` is met, the function throws an error with a descriptive message, halting script execution. This is a useful utility function for validating user input in signal processing scripts. Input Arguments: filter_lp - The low-pass filter cutoff frequency (e.g., 0.1). filte
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_check_filter_parameters()`
- **Functional Purpose:** Written by Pratik Jain WHIFUN_CHECK_FILTER_PARAMETERS Checks if filter cutoffs are correctly ordered. WHIFUN_CHECK_FILTER_PARAMETERS(filter_lp, filter_hp) checks if the low-pass filter cutoff frequency (`filter_lp`) is less than or equal to the high-pass filter cutoff frequency (`filter_hp`). If the condition `filter_lp > filter_hp` is met, the function throws an error with a descriptive message, halting script execution. This is a useful utility function for validating user input in signal processing scripts. Input Arguments: filter_lp - The low-pass filter cutoff frequency (e.g., 0.1). filter_hp - The high-pass filter cutoff frequency (e.g., 0.01). Example: % This will pass without error w
- **Arguments:**
  - `filter_lp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `filter_hp` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
