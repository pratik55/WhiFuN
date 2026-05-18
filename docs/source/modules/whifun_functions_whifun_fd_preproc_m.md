- **Key Features:**
  - WHIFUN_FD_PREPROC Performs quality control based on framewise displacement. Subj_list_1 = WHIFUN_FD_PREPROC(quality_control_path, Subj_list_1, ..., greater_than_20) calculates the framewise displacement (FD) and assesses whether a subject's head motion exceeds predefined quality control thresholds. The function first computes the FD using the motion parameters. It then applies three checks: 1. **Maximum FD**: Is the maximum FD value greater than `max_fd`? 2. **Mean FD**: Is the mean FD value greater than `mean_fd`? 3. **Percentage of high-motion volumes**: Is the percentage of volumes with FD 
  - Internal calls detected: `whifun_calculate_fd`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_fd_preproc()`
- **Functional Purpose:** WHIFUN_FD_PREPROC Performs quality control based on framewise displacement. Subj_list_1 = WHIFUN_FD_PREPROC(quality_control_path, Subj_list_1, ..., greater_than_20) calculates the framewise displacement (FD) and assesses whether a subject's head motion exceeds predefined quality control thresholds. The function first computes the FD using the motion parameters. It then applies three checks: 1. **Maximum FD**: Is the maximum FD value greater than `max_fd`? 2. **Mean FD**: Is the mean FD value greater than `mean_fd`? 3. **Percentage of high-motion volumes**: Is the percentage of volumes with FD greater than `greater_than_20` more than 20%? If any of these conditions are met, the subject is fla
- **Arguments:**
  - `quality_control_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `in_motion_txt_path` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `max_fd` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `mean_fd` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `greater_than_20` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
