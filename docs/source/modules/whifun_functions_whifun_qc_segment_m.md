- **Key Features:**
  - WHIFUN_QC_SEGMENT Generates quality control images for anatomical segmentation. WHIFUN_QC_SEGMENT(...) creates a visual report to assess the quality of the anatomical image segmentation. The function can generate two types of reports, one in the subject's native space and one in MNI space, depending on the input paths. The function performs the following steps: 1. **SPM Orthoslice Plot**: It creates a plot showing a reference image (`ref`) with overlaid contours of the segmented Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF). This provides a visual check of how well the seg
  - Internal calls detected: `whifun_create_file`, `whifun_create_seg_overlaps`, `whifun_slover`
  - External dependencies detected: SPM12, SLover/MarsBaR-style visualization helpers

## Function: `whifun_qc_segment()`
- **Functional Purpose:** WHIFUN_QC_SEGMENT Generates quality control images for anatomical segmentation. WHIFUN_QC_SEGMENT(...) creates a visual report to assess the quality of the anatomical image segmentation. The function can generate two types of reports, one in the subject's native space and one in MNI space, depending on the input paths. The function performs the following steps: 1. **SPM Orthoslice Plot**: It creates a plot showing a reference image (`ref`) with overlaid contours of the segmented Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF). This provides a visual check of how well the segmentation process worked. 2. **SLover Plot**: It uses `whifun_slover` to display the segmented tissu
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ref` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_slices` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_contour_range` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `slover_view` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `space_name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
