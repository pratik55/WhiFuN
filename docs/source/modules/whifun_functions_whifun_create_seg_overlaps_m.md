- **Key Features:**
  - WHIFUN_CREATE_SEG_OVERLAPS Visualizes the overlap of Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF) segmentation masks onto a reference image using SPM's `spm_orthviews`. WHIFUN_CREATE_SEG_OVERLAPS(GM_PATH, WM_PATH, CSF_PATH, REF, CAPTION_1, CAPTION_2) This function is used for quality control (QC) in neuroimaging pipelines, allowing a visual check of the accuracy of tissue segmentation (e.g., from SPM's 'New Segment' or 'Segment' tools) by overlaying the masks in distinct colors onto a T1-weighted or normalized reference image. Input Arguments: GM_PATH - Full path to the N
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SPM12, Shell/system execution

## Function: `whifun_create_seg_overlaps()`
- **Functional Purpose:** WHIFUN_CREATE_SEG_OVERLAPS Visualizes the overlap of Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF) segmentation masks onto a reference image using SPM's `spm_orthviews`. WHIFUN_CREATE_SEG_OVERLAPS(GM_PATH, WM_PATH, CSF_PATH, REF, CAPTION_1, CAPTION_2) This function is used for quality control (QC) in neuroimaging pipelines, allowing a visual check of the accuracy of tissue segmentation (e.g., from SPM's 'New Segment' or 'Segment' tools) by overlaying the masks in distinct colors onto a T1-weighted or normalized reference image. Input Arguments: GM_PATH - Full path to the NIfTI file containing the Gray Matter segmentation mask (e.g., c1T1.nii). WM_PATH - Full path to the
- **Arguments:**
  - `GM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `ref` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `caption_1` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `caption_2` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
