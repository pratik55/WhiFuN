- **Key Features:**
  - function rest_CallBrainNetViewer(BrainVolume,NMin,PMin,ClusterSize,ConnectivityCriterion,SurfFileName,viewtype,ColorMap,NMax,PMax,BrainHeader) Function to call BrainNet Viewer (by Mingrui Xia) by REST Slice Viewer. Also can be used to scripting call BrainNet Viewer. Input: BrainVolume - 1) The 3D Brain Volume (could be thresholded), parameter 'BrainHeader' needed. or 2) the File Name of a Brain Image, e.g. '/home/T.img' NMin - The negative minimum (minimum in absolute value). Could be the negative threshold - default: calculate from BrainVolume PMin - The positive minimum. Could be the positiv
  - Internal calls detected: `BrainNet`
  - External dependencies detected: SPM12, BrainNet Viewer

## Function: `BrainNet_MapVolume()`
- **Functional Purpose:** function rest_CallBrainNetViewer(BrainVolume,NMin,PMin,ClusterSize,ConnectivityCriterion,SurfFileName,viewtype,ColorMap,NMax,PMax,BrainHeader) Function to call BrainNet Viewer (by Mingrui Xia) by REST Slice Viewer. Also can be used to scripting call BrainNet Viewer. Input: BrainVolume - 1) The 3D Brain Volume (could be thresholded), parameter 'BrainHeader' needed. or 2) the File Name of a Brain Image, e.g. '/home/T.img' NMin - The negative minimum (minimum in absolute value). Could be the negative threshold - default: calculate from BrainVolume PMin - The positive minimum. Could be the positive threshold - default: calculate from BrainVolume ClusterSize - Set a cluster (voxel number) must be
- **Arguments:**
  - `BrainVolume` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `NMin` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `PMin` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ClusterSize` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ConnectivityCriterion` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `SurfFileName` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `viewtype` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ColorMap` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `NMax` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `PMax` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `BrainHeader` (numeric image/header data, commonly X x Y x Z or X x Y x Z x T): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `AdjustColorMap()`
- **Functional Purpose:** Adjust the colormap to leave blank to values under threshold, the orginal color map with be set into [NMax NMin] and [PMin PMax]. Written by YAN Chao-Gan, 111023 Input: OriginalColorMap - the original color map NullColor - The values between NMin and PMin will be set to this color (leave blank) NMax, NMin, PMin, PMax - set the axis of colorbar (the orginal color map with be set into [NMax NMin] and [PMin PMax]) Output: NewColorMap - the generated color map, a 1000 by 3 matrix.
- **Arguments:**
  - `OriginalColorMap` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `NullColor` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `NMax` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `NMin` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `PMin` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `PMax` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `AFNI_ColorMap()`
- **Functional Purpose:** Generate the color map like AFNI. Written by YAN Chao-Gan, 090601 Input: SegmentNum - the number of segments. it should be 2,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20 or 256 Output: ColorMap - the generated color map, an x by 3 matrix.
- **Arguments:**
  - `SegmentNum` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
