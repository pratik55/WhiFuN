# whifun_create_sphere

Source: `whifun_functions/whifun_create_sphere.m:1`

```matlab
function vox_list = whifun_create_sphere(center_vox, radius_mm, vox_dim, vol_size)
```

## MATLAB Help

WHIFUN_CREATE_SPHERE Generates a list of voxel coordinates within a sphere.

  vox_list = WHIFUN_CREATE_SPHERE(center_vox, radius_mm, vox_dim, vol_size)
  creates a list of 1-based voxel coordinates that fall inside a sphere
  of a given radius. This function is a core utility for defining
  spherical regions of interest (ROIs) in neuroimaging analysis.

  The function first calculates a cubic grid of candidate voxels around the
  center point. It then filters this grid, keeping only the voxels whose
  Euclidean distance from the center (in millimeters) is less than or
  equal to the specified radius. Finally, it clips the list of voxels to
  ensure they are all within the bounds of the image volume.

  Input Arguments:
  center_vox - A 1x3 vector `[i j k]` representing the center voxel of the
               sphere in 1-based indices.
  radius_mm  - A scalar representing the radius of the sphere in millimeters.
  vox_dim    - A 1x3 vector `[dx dy dz]` of the voxel dimensions in millimeters.
  vol_size   - A 1x3 vector `[nx ny nz]` of the image dimensions.

  Output Arguments:
  vox_list   - An Nx3 array where each row contains the `[i j k]` 1-based
               coordinates of a voxel inside the sphere.

  Author: Pratik Jain
  See also NDGRID, BSXFUN.
