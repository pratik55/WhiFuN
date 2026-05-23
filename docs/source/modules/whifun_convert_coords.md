# whifun_convert_coords

Source: `whifun_functions/whifun_convert_coords.m:1`

```matlab
function coord_out = whifun_convert_coords(M, coord_in, mode,mat_py)
```

## MATLAB Help

WHIFUN_CONVERT_COORDS Converts coordinates between MNI and voxel space.

  coord_out = WHIFUN_CONVERT_COORDS(M, coord_in, mode, mat_py) converts
  a set of 3D coordinates from one coordinate system to another using a
  4x4 affine transformation matrix.

  This function is a fundamental utility for neuroimaging analysis, as it
  allows for precise mapping of locations between the standard MNI space
  and a subject voxel space. It can handle both `mni2vox` and
  `vox2mni` conversions. The function also includes a parameter to handle
  the difference between 0-based indexing (Python) and 1-based indexing
  (MATLAB), ensuring correct conversion.

  Input Arguments:
  M        - A 4x4 affine transformation matrix (e.g., from a NIfTI header).
  coord_in - A matrix of input coordinates (Nx3), where N is the number of
             points and the columns are x, y, and z.
  mode     - A string specifying the direction of conversion:
             - `'mni2vox'` converts from MNI coordinates to voxel coordinates.
             - `'vox2mni'` converts from voxel coordinates to MNI coordinates.
  mat_py   - (Optional) A logical value (0 or 1). If 1, it assumes the
             input and output are based on MATLAB's 1-based indexing
             for voxel coordinates. If 0, it assumes 0-based indexing.
             Defaults to 1.

  Output Arguments:
  coord_out - A matrix of the converted coordinates (Nx3). For `mni2vox`,
              the output is rounded to the nearest integer.

  Author: Pratik Jain
  See also ROUND.
