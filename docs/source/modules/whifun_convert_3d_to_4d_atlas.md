# whifun_convert_3d_to_4d_atlas

Source: `whifun_functions/whifun_convert_3d_to_4d_atlas.m:1`

```matlab
function whifun_convert_3d_to_4d_atlas(input_atlas_path, output_path)
```

## MATLAB Help

whifun_convert_3d_to_4d_atlas(input_atlas_path, [output_path])

Converts a 3D labeled atlas into a 4D NIfTI file, where each label
(level) becomes a separate 3D volume in the 4th dimension.

Example:
  whifun_convert_3d_to_4d_atlas('atlas_3d.nii');
  whifun_convert_3d_to_4d_atlas('atlas_3d.nii', 'atlas_4d.nii');

Inputs:
  input_atlas_path : Path to the input 3D atlas NIfTI file.
  output_path      : (Optional) Output 4D NIfTI file path.
                     If not provided, saved as <input_name>_4d.nii

Notes:
  - Each volume in the 4D output corresponds to one unique label in the atlas.
  - Background (0) is ignored.

Requires:
  SPM toolbox (for spm_vol, spm_read_vols, spm_write_vol)
Author: Pratik Jain
