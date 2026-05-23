# whifun_convert_nifti_3d_to_4d

Source: `whifun_functions/whifun_convert_nifti_3d_to_4d.m:1`

```matlab
function a = whifun_convert_nifti_3d_to_4d(folder,filter,TR,out_filename,atlas)
```

## MATLAB Help

WHIFUN_CONVERT_NIFTI_3D_TO_4D Combines a series of 3D NIfTI volumes into a
  single 4D NIfTI file (e.g., creating a functional time series from
  individual 3D volumes).

  A = WHIFUN_CONVERT_NIFTI_3D_TO_4D(FOLDER, FILTER, TR, OUT_FILENAME, ATLAS)

  This function is useful for aggregating individual 3D image acquisitions
  (e.g., single time points from a scanner) into the standard 4D time series format.

  Input Arguments:
  FOLDER      - The directory path containing the 3D NIfTI files.
  FILTER      - The common filename pattern (wildcard) to match the 3D NIfTI files (e.g., 'f*.nii').
  TR          - The Temporal Resolution (Repetition Time) in seconds. This
                value is written to the 4th dimension of the NIfTI header's
                PixelDimensions (voxel size).
  OUT_FILENAME- (Optional) The full path and filename for the resulting 4D NIfTI file.
                Default: `<basename>_4d.nii` in the FOLDER.
  ATLAS       - (Optional, default 0) A flag to indicate a special conversion mode:
                ATLAS = 0: Standard mode. Reads the raw image data (e.g., BOLD signal).
                ATLAS = 1: Atlas mode. Reads the binary mask (assumed to be 1s and 0s)
                           and replaces the 1s with the index 'i' of the file being read.
                           This can be used to combine multiple binary masks into a
                           4D volume where each 3D volume is a uniquely labeled mask.

  Output Arguments:
  A           - The resulting 4D matrix [X x Y x Z x T] containing the combined image data.

  Dependencies: `niftiinfo`, `niftiread`, `niftiwrite` (MATLAB built-in or custom wrappers).

  Author: Pratik Jain
