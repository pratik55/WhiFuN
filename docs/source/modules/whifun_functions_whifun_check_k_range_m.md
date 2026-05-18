- **Key Features:**
  - Written by Pratik Jain WHIFUN_CHECK_K_RANGE Checks the validity of a K-range. WHIFUN_CHECK_K_RANGE(K_range_l, K_range_h) verifies that the lower bound of a K-range (`K_range_l`) is less than or equal to the upper bound (`K_range_h`). If the condition `K_range_l > K_range_h` is met, the function generates an error and stops the script's execution. This is a crucial check to ensure that range-based parameters are specified in the correct order. Input Arguments: K_range_l - The lower bound of the K-range. K_range_h - The upper bound of the K-range. Example: % This will pass without error whifun_c
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_check_k_range()`
- **Functional Purpose:** Written by Pratik Jain WHIFUN_CHECK_K_RANGE Checks the validity of a K-range. WHIFUN_CHECK_K_RANGE(K_range_l, K_range_h) verifies that the lower bound of a K-range (`K_range_l`) is less than or equal to the upper bound (`K_range_h`). If the condition `K_range_l > K_range_h` is met, the function generates an error and stops the script's execution. This is a crucial check to ensure that range-based parameters are specified in the correct order. Input Arguments: K_range_l - The lower bound of the K-range. K_range_h - The upper bound of the K-range. Example: % This will pass without error whifun_check_k_range(2, 10); % This will throw an error % whifun_check_k_range(10, 2); See also SPRINTF, ERR
- **Arguments:**
  - `K_range_l` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `K_range_h` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
