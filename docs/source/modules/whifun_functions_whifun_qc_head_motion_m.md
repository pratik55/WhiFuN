- **Key Features:**
  - WHIFUN_QC_HEAD_MOTION Generates a quality control figure for head motion. WHIFUN_QC_HEAD_MOTION(out_folder, realigned_func_native, ..., motion_txt) creates a comprehensive quality control report for head motion for a single subject. The report consists of four plots combined into a single figure. The function performs the following steps: 1. **Check Existence**: It checks if a head motion QC image already exists and, based on the `over_write` flag, either skips or generates a new one. 2. **Calculate Metrics**: It reads the realigned functional data and the motion parameter file. It then calcul
  - Internal calls detected: `whifun_create_file`
  - External dependencies detected: MATLAB NIfTI I/O, MATLAB table/file I/O

## Function: `whifun_qc_head_motion()`
- **Functional Purpose:** WHIFUN_QC_HEAD_MOTION Generates a quality control figure for head motion. WHIFUN_QC_HEAD_MOTION(out_folder, realigned_func_native, ..., motion_txt) creates a comprehensive quality control report for head motion for a single subject. The report consists of four plots combined into a single figure. The function performs the following steps: 1. **Check Existence**: It checks if a head motion QC image already exists and, based on the `over_write` flag, either skips or generates a new one. 2. **Calculate Metrics**: It reads the realigned functional data and the motion parameter file. It then calculates: - **Global Mean**: The scaled global signal mean over time. - **Pairwise Variance**: A measure
- **Arguments:**
  - `out_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `realigned_func_native` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `name` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `max_fd` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mean_fd` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `greater_than_20` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `over_write` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `motion_txt` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
