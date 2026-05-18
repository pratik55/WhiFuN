- **Key Features:**
  - WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
  - Internal calls detected: `whifun_convert_coords`
  - External dependencies detected: MATLAB NIfTI I/O

## Function: `whifun_view()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transformation matrix (from NIfTI header) for converting Voxel coordinates to MNI/World coordinates. Depen
- **Arguments:**
  - `vol` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `M` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `clickXZ1()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `evt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `clickYZ()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `evt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `clickXY1()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `evt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `editBoxCallback()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `src` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `dim` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `type` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `changeVolume()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `src` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `sliderVolume()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `src` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `updateViews()`
- **Functional Purpose:** WHIFUN_VIEW Ortho viewer for 3D or 4D NIfTI volumes with interactive crosshairs, coordinate display (Voxel and optional MNI), volume navigation, and time series plotting. Usage: whifun_view(vol4d, M) % Pass 4D volume data and affine matrix M whifun_view(vol3d) % Pass 3D volume data whifun_view(nifti_path) % Pass NIfTI file path (reads data and header M) Input Arguments: VOL: Input data. Can be: - X x Y x Z x T numeric array (4D fMRI data). - X x Y x Z numeric array (3D anatomical/map data). - Character array or string specifying the path to a NIfTI file. M: (Optional) 4x4 numeric affine transf
- **Arguments:**
  - `h` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
