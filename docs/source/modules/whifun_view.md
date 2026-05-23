# whifun_view

**Source:** `whifun_functions/whifun_view.m:1`

## Signature

```matlab
function whifun_view(vol, M)
```

## Summary

WHIFUN_VIEW Interactive multi-planar visualizer for 3D and 4D neuroimaging volumes.

## Syntax

```matlab
WHIFUN_VIEW(vol) launches an interactive orthoview UI featuring a 2x2
WHIFUN_VIEW(vol, M) attaches a 4x4 affine transformation matrix (M). This
```

## Description

tiled layout showing Coronal (XZ), Sagittal (YZ), and Axial (XY) planes. If the input is a 3D volume, the 4th panel displays the current voxel value. If the input is a 4D volume (e.g., fMRI), the 4th panel plots the entire BOLD time series for the selected voxel with a real-time frame indicator.

activates additional interactive UI edit boxes displaying real-time MNI coordinates. Users can input target MNI coordinates directly to jump the crosshairs to that anatomical location.

Input Flexibility: If 'vol' is passed as a string or char file path to a NIfTI image, the function automatically reads the volume and extracts its spatial transformation matrix (M) from the header information.

Interactive Features:

- Crosshairs: Click anywhere inside the Axial, Coronal, or Sagittal
plots to instantly reposition the crosshairs and update all views.

- Voxel/MNI Input Boxes: Type explicit coordinates to update positions.
- 4D Time Slider: Use the slider or step text box at the bottom left
to scroll through different time frames of 4D datasets.

## Input Arguments

### `vol`
A 3D matrix (X x Y x Z), 4D matrix (X x Y x Z x T), or a string/char specifying the file path to a valid NIfTI file.

### `M`
(Optional) 4x4 affine transformation matrix mapping voxels to MNI space. Automatically extracted if 'vol' is a file path. Examples: % Example 1: View a NIfTI file directly (auto-loads MNI space) % Example 2: View a raw 3D matrix without MNI space mapping imgData = rand(91, 109, 91);

## Requirements

'whifun_convert_coords' if an affine matrix is supplied or automatically loaded from a NIfTI path.

## Author

Author: Pratik Jain

## Examples

```matlab
whifun_view('C:\Data\wfunc.nii');
whifun_view(imgData);
```
