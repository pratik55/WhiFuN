- **Key Features:**
  - Scale image data to colormap, returning colormap indices FORMAT [img, badvals]=pr_scaletocmap(inpimg,mn,mx,cmap,lrn) Inputs inpimg - matrix containing image to scale mn - image value that maps to first value of colormap mx - image value that maps to last value of colormap cmap - 3xN colormap lrn - 1x3 vector, giving colormap indices that should fill: - lrn(1) (L=Left) - values less than mn - lrn(2) (R=Right) - values greater than mx - lrn(3) (N=NaN) - NaN values If lrn value is 0, then colormap values are set to 1, and indices to these values are returned in badvals (below) Output img - inpimg
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `pr_scaletocmap()`
- **Functional Purpose:** Scale image data to colormap, returning colormap indices FORMAT [img, badvals]=pr_scaletocmap(inpimg,mn,mx,cmap,lrn) Inputs inpimg - matrix containing image to scale mn - image value that maps to first value of colormap mx - image value that maps to last value of colormap cmap - 3xN colormap lrn - 1x3 vector, giving colormap indices that should fill: - lrn(1) (L=Left) - values less than mn - lrn(2) (R=Right) - values greater than mx - lrn(3) (N=NaN) - NaN values If lrn value is 0, then colormap values are set to 1, and indices to these values are returned in badvals (below) Output img - inpimg scaled between 1 and (size(cmap, 1)) badvals - indices into inpimg containing values out of range,
- **Arguments:**
  - `inpimg` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mn` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mx` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `cmap` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `lrn` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
