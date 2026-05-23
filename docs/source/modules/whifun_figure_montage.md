# whifun_figure_montage

**Source:** `whifun_functions/whifun_figure_montage.m:1`

## Signature

```matlab
function whifun_figure_montage(in,x,y)
```

## Summary

WHIFUN_FIGURE_MONTAGE Creates a 2D image montage from a 3D matrix (stack of images) and displays it.

## Syntax

```matlab
OUT = WHIFUN_FIGURE_MONTAGE(IN, X, Y)
```

## Description

Takes a stack of 2D images (N x M x K) and arranges them into a single montage image of size (N*Y) x (M*X), where X is the number of images per row and Y is the number of rows. It then displays the resulting montage using `imagesc`.

## Input Arguments

### `IN`
The 3D data array (stack of images). Expected dimensions: (Image_Height x Image_Width x Number_of_Images)

### `X`
The number of images to place horizontally (columns) in the montage.

### `Y`
The number of images to place vertically (rows) in the montage. Note: X * Y should equal the total number of images (size(IN, 3)).

## Output Arguments

### `OUT`
The final 2D montage matrix (Image_Height*Y x Image_Width*X).

## Examples

Example: % Assume 'brain_slices' is 91x109x10 (10 slices) % Create a 2x5 montage (2 rows, 5 columns)

```matlab
whifun_figure_montage(brain_slices, 5, 2);
```

## Author

Author: Pratik Jain
