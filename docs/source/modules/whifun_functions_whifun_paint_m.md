- **Key Features:**
  - Method to display slice overlay FORMAT obj = paint(obj, params) Inputs obj - slice overlay object params - optional structure containing extra display parameters - refreshf - overrides refreshf in object - clf - overrides clf in object - userdata - if 0, does not add object to userdata field (see below) Outputs obj - which may have been filled with defaults paint attaches the object used for painting to the 'UserData' field of the figure handle, unless instructed not to with 0 in userdata flag __________________________________________________________________________ Matthew Brett $Id: paint.m
  - Internal calls detected: `findobj`, `mars_struct`, `pr_scaletocmap`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_paint()`
- **Functional Purpose:** Method to display slice overlay FORMAT obj = paint(obj, params) Inputs obj - slice overlay object params - optional structure containing extra display parameters - refreshf - overrides refreshf in object - clf - overrides clf in object - userdata - if 0, does not add object to userdata field (see below) Outputs obj - which may have been filled with defaults paint attaches the object used for painting to the 'UserData' field of the figure handle, unless instructed not to with 0 in userdata flag __________________________________________________________________________ Matthew Brett $Id: paint.m 6623 2015-12-03 18:38:08Z guillaume $
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `params` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `sf_slice2panel()`
- **Functional Purpose:** to voxel space of image
- **Arguments:**
  - `img` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `xyzmm` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `transform` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vdims` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
