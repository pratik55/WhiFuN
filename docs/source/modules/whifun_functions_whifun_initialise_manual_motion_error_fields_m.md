- **Key Features:**
  - WHIFUN_INITIALISE_MANUAL_MOTION_ERROR_FIELDS Initializes exclusion fields for a subject. Subj_list_1 = WHIFUN_INITIALISE_MANUAL_MOTION_ERROR_FIELDS(Subj_list_1) initializes the `error`, `motion_ex`, and `manual_ex` fields of a single subject structure `Subj_list_1`. This function is a utility to ensure that these tracking fields are properly set to a default value (0) before a subject is processed. It prevents potential errors that could arise from trying to access or modify a field that is empty, non-existent, or contains a `NaN` value. The function performs the following actions: 1. Sets the
  - Internal calls detected: `whifun_isnan_or_empty`
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_initialise_manual_motion_error_fields()`
- **Functional Purpose:** WHIFUN_INITIALISE_MANUAL_MOTION_ERROR_FIELDS Initializes exclusion fields for a subject. Subj_list_1 = WHIFUN_INITIALISE_MANUAL_MOTION_ERROR_FIELDS(Subj_list_1) initializes the `error`, `motion_ex`, and `manual_ex` fields of a single subject structure `Subj_list_1`. This function is a utility to ensure that these tracking fields are properly set to a default value (0) before a subject is processed. It prevents potential errors that could arise from trying to access or modify a field that is empty, non-existent, or contains a `NaN` value. The function performs the following actions: 1. Sets the `error` field to 0. This flag is used to track processing errors for the subject. 2. Checks if the
- **Arguments:**
  - `Subj_list_1` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
