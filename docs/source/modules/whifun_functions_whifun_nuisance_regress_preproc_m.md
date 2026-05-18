- **Key Features:**
  - WHIFUN_NUISANCE_REGRESS_PREPROC Orchestrates nuisance regression. [Subj_list_1, out_func_path] = WHIFUN_NUISANCE_REGRESS_PREPROC(...) is a high-level function that manages the nuisance regression step of a neuroimaging preprocessing pipeline. It automates the process of removing unwanted signals from the functional data, such as head motion artifacts and physiological noise. The function first checks if a pre-regressed file already exists. Based on the `over_write` flag, it either skips the process or calls the `whifun_regress` function to perform the actual regression. This utility function e
  - Internal calls detected: `whifun_create_file`, `whifun_regress`, `write_error`
  - External dependencies detected: Shell/system execution

## Function: `whifun_nuisance_regress_preproc()`
- **Functional Purpose:** WHIFUN_NUISANCE_REGRESS_PREPROC Orchestrates nuisance regression. [Subj_list_1, out_func_path] = WHIFUN_NUISANCE_REGRESS_PREPROC(...) is a high-level function that manages the nuisance regression step of a neuroimaging preprocessing pipeline. It automates the process of removing unwanted signals from the functional data, such as head motion artifacts and physiological noise. The function first checks if a pre-regressed file already exists. Based on the `over_write` flag, it either skips the process or calls the `whifun_regress` function to perform the actual regression. This utility function ensures that the regression is performed only when needed. The function updates the subject structure
- **Arguments:**
  - No explicit input arguments.
