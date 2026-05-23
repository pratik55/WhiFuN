# whifun_select_confound_vars

Source: `whifun_functions/whifun_select_confound_vars.m:1`

```matlab
function idx_all = whifun_select_confound_vars(confound_vars, Reg_params)
```

## MATLAB Help

WHIFUN_SELECT_CONFOUND_VARS
Select confound variables using wildcard patterns (*)

INPUTS
  confound_vars : cell array of char or string
  Reg_params    : cell array of patterns (e.g., {'csf','aroma*','*motion*'})

OUTPUT
  selected_vars : cell array of matched confound variable names
