# whifun_paint

Source: `whifun_functions/whifun_paint.m:1`

```matlab
function obj = whifun_paint(obj, params)
```

## MATLAB Help

Method to display slice overlay
FORMAT obj = paint(obj, params)

Inputs
obj         - slice overlay object
params      - optional structure containing extra display parameters
              - refreshf - overrides refreshf in object
              - clf      - overrides clf in object
              - userdata - if 0, does not add object to userdata field
              (see below)

Outputs
obj         - which may have been filled with defaults

paint attaches the object used for painting to the 'UserData' field of
the figure handle, unless instructed not to with 0 in userdata flag
__________________________________________________________________________
