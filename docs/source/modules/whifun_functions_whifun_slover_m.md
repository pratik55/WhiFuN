- **Key Features:**
  - WHIFUN_SLOVER A wrapper function around the core 'slover' visualization engine, customized for WhiFuN's needs, particularly for image overlays and segmentation QC displays. OBJ = WHIFUN_SLOVER(IMGS, ITYPE, CMAP, SLICES, CNT_RANGE, IMG_VIEW, WT, FG, CBAR_) This function initializes and configures a 'slover' object to display multiple NIfTI images with custom colormaps, slices, and views, and then calls a drawing function (whifun_paint) to render the output. Input Arguments: IMGS - Cell array of full paths to NIfTI files to be displayed. ITYPE - Cell array of strings defining the image type for 
  - Internal calls detected: `whifun_paint`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_slover()`
- **Functional Purpose:** WHIFUN_SLOVER A wrapper function around the core 'slover' visualization engine, customized for WhiFuN's needs, particularly for image overlays and segmentation QC displays. OBJ = WHIFUN_SLOVER(IMGS, ITYPE, CMAP, SLICES, CNT_RANGE, IMG_VIEW, WT, FG, CBAR_) This function initializes and configures a 'slover' object to display multiple NIfTI images with custom colormaps, slices, and views, and then calls a drawing function (whifun_paint) to render the output. Input Arguments: IMGS - Cell array of full paths to NIfTI files to be displayed. ITYPE - Cell array of strings defining the image type for each image (e.g., 'Structural', 'Blobs', 'Truecolour', 'Contours', and related items.). CMAP - Cell array of color
- **Arguments:**
  - `imgs` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `itype` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `cmap` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `cnt_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `img_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `wt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `fg` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `cbar_` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
