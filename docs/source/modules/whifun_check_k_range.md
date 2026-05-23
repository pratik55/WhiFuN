# whifun_check_k_range

Source: `whifun_functions/whifun_check_k_range.m:1`

```matlab
function whifun_check_k_range(K_range_l,K_range_h)
```

## MATLAB Help

Written by Pratik Jain
WHIFUN_CHECK_K_RANGE Checks the validity of a K-range.

  WHIFUN_CHECK_K_RANGE(K_range_l, K_range_h) verifies that the lower bound
  of a K-range (`K_range_l`) is less than or equal to the upper bound
  (`K_range_h`).

  If the condition `K_range_l > K_range_h` is met, the function generates
  an error and stops the script's execution. This is a crucial check to
  ensure that range-based parameters are specified in the correct order.

  Input Arguments:
  K_range_l - The lower bound of the K-range.
  K_range_h - The upper bound of the K-range.

  Example:
     % This will pass without error
     whifun_check_k_range(2, 10);

     % This will throw an error
     % whifun_check_k_range(10, 2);

  See also SPRINTF, ERROR.
  Author: Pratik Jain
