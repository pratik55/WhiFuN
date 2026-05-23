# whifun_show_slices_multioverlay

Source: `whifun_functions/whifun_show_slices_multioverlay.m:1`

```matlab
function whifun_show_slices_multioverlay(volumes, overlay_types, cmaps, slices, orientation)
```

## MATLAB Help

WHIFUN_SHOW_SLICES_MULTIOVERLAY
Display multiple slices (one per image) in a montage with overlay support.

Inputs:
  volumes        - cell array of file paths or 3D matrices
  overlay_types  - cell array: {'structure','contour',...}
  cmaps          - cell array of colormaps for each image
  slices         - array of slice indices (one per image)
  orientation    - 'axial' | 'sagittal' | 'coronal'

Example:
  vols = {'sub1.nii','sub2.nii','sub3.nii'};
  types = {'structure','contour','structure'};
  cmaps = {hot, lines, gray};
  slices = [40 45 50];
  whifun_show_slices_multioverlay(vols, types, cmaps, slices, 'axial');
