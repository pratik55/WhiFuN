# whifun_calc

Source: `whifun_functions/whifun_calc.m:1`

```matlab
function whifun_calc(output_path, expression, varargin)
```

## MATLAB Help

whifun_calc(output_path, expression, nifti1, nifti2, ...)

Calculates a mathematical expression using multiple NIfTI images.

Example:
  whifun_calc('out.nii', 'i1 + i2 + i3', 'sub1.nii', 'sub2.nii', 'sub3.nii')

Inputs:
  output_path : path to save the output NIfTI file
  expression  : expression to evaluate (e.g., 'i1 + i2 - i3')
  varargin    : list of NIfTI image file paths (all in same grid/space)

The variables in the expression must be named i1, i2, i3, ... corresponding
to the order of NIfTI inputs.
