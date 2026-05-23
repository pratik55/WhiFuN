# y_Write

Source: `whifun_functions/y_Write.m:1`

```matlab
function y_Write(Data,Header,OutName)
```

## MATLAB Help

Write NIfTI file (3D or 4D) Based on SPM's nifti or Write GIfTI file (1D or 2D) Based on SPM's gifti or Write DPABINet Matrix files
%------------------------------------------------------------------------
1. For NIfTI
Write data (Data) with a specified header (Header) into a image file with format
of Nifti 1.1. The data (Data) should be 3D or 4D matrix, the header (Header) should
be a structure the same as SPM. If the filename (OutName) is with
extra name as '.img', then it will generate two files (header and
data seperately), or else, '.nii', it will generate single file with
header and data together.

Usage: y_Write(Data,Header,OutName)

Input:
1) Data -  Data of 4D matrix to write
2) Header - a structure containing image volume information, the structure
   is the same with a structure have read
   The elements in the structure are:
      Header.fname - the filename of the image. If the filename is not set,
                   just use the parameter.
      Header.dt    - A 1x2 array.  First element is datatype (see spm_type).
                The second is 1 or 0 depending on the endian-ness.
      Header.mat   - a 4x4 affine transformation matrix mapping from
                voxel coordinates to real world coordinates.
      Header.pinfo - plane info for each plane of the volume.
             Header.pinfo(1,:) - scale for each plane
             Header.pinfo(2,:) - offset for each plane
                The true voxel intensities of the jth image are given
                by: val*Header.pinfo(1,j) + Header.pinfo(2,j)
             Header.pinfo(3,:) - offset into image (in bytes).
                If the size of pinfo is 3x1, then the volume is assumed
                to be contiguous and each plane has the same scalefactor
                and offset.
             The scale and intercept will be changed according to the
             data to write
3) OutName - the path and filename of image file to output [path\*.img or *.nii]

2. For GIfTI
Write data (Data) with a specified header (Header) into a image file with format of GIfTI.
1) Data -  Data of 1D or 2D matrix to write
2) Header - a structure containing image GIfTI information, the structure
            is the same with a structure have read.
            It must have a subfield .cdata!!!

3. For DPABINet Matrix
Write data (Data) with a specified header (Header) into a .mat file with format defined in Header.
1) Data -  Data of 1D or 2D matrix to write
2) Header - a structure containing DPABINet Matrix information: Header.MatrixNames and Header.MatrixSize, the structure is the same with a structure have read.
      Header.MatrixNames  - the matrix names. Must have!
      Header.MatrixSize   - the size of the matrices.
