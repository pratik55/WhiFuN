- **Key Features:**
  - WHIFUN_WANAT_MASK Creates a brain mask from segmented anatomical images in MNI space using SPM. output = WHIFUN_ANAT_MASK(m_file, now_anat_path, norm) creates a binary brain mask by combining the segmented Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF) images. This function configures and runs the `imcalc` module in SPM to perform a simple logical operation. It sums the segmented GM, WM, and CSF images and creates a binary mask where any voxel with a combined probability greater than 0.5 is set to 1 (brain tissue), and all other voxels are set to 0. The function can create 
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: SPM12, Shell/system execution

## Function: `whifun_anat_mask()`
- **Functional Purpose:** WHIFUN_WANAT_MASK Creates a brain mask from segmented anatomical images in MNI space using SPM. output = WHIFUN_ANAT_MASK(m_file, now_anat_path, norm) creates a binary brain mask by combining the segmented Gray Matter (GM), White Matter (WM), and Cerebrospinal Fluid (CSF) images. This function configures and runs the `imcalc` module in SPM to perform a simple logical operation. It sums the segmented GM, WM, and CSF images and creates a binary mask where any voxel with a combined probability greater than 0.5 is set to 1 (brain tissue), and all other voxels are set to 0. The function can create the mask in either native or MNI space, based on the `norm` input argument. This is a crucial step f
- **Arguments:**
  - `out_mask_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `anat_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `GM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `WM_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `CSF_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
