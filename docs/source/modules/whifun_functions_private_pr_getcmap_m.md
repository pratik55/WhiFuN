- **Key Features:**
  - Get colormap of name acmapname FORMAT [cmap, warnstr] = pr_getcmap(acmapname) Inputs acmapname - string. Can be (in order of precedence) - matrix name in base workspace - colour name; one of 'red','green','blue','cyan', 'magenta', 'yellow', 'black', 'white' - filename of .mat or .lut file. If filename has no extension, assumes '.mat' extension Outputs cmap - Nx3 colormap matrix or empty if fails warnstr - warning message if fails __________________________________________________________________________ Matthew Brett $Id: pr_getcmap.m 6623 2015-12-03 18:38:08Z guillaume $
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB table/file I/O, SLover/MarsBaR-style visualization helpers

## Function: `pr_getcmap()`
- **Functional Purpose:** Get colormap of name acmapname FORMAT [cmap, warnstr] = pr_getcmap(acmapname) Inputs acmapname - string. Can be (in order of precedence) - matrix name in base workspace - colour name; one of 'red','green','blue','cyan', 'magenta', 'yellow', 'black', 'white' - filename of .mat or .lut file. If filename has no extension, assumes '.mat' extension Outputs cmap - Nx3 colormap matrix or empty if fails warnstr - warning message if fails __________________________________________________________________________ Matthew Brett $Id: pr_getcmap.m 6623 2015-12-03 18:38:08Z guillaume $
- **Arguments:**
  - `acmapname` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
