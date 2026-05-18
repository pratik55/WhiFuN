- **Key Features:**
  - FD_CALC Calculates the Framewise Displacement (FD) from a time series of rigid-body head motion parameters. FD = FD_CALC(Y) Framewise Displacement is a scalar quantity summarizing head motion from one time point to the next, typically derived from 6 rigid-body realignment parameters (3 translations and 3 rotations). Rotations are usually converted to displacements on a sphere of a given radius (e.g., 50 mm). Input Arguments: Y - Head motion parameters time series. Expected size: N_TimePoints x N_MotionParameters (where N_MotionParameters is 6, or 12 if including derivatives, but only the 6 pri
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `fd_calc()`
- **Functional Purpose:** FD_CALC Calculates the Framewise Displacement (FD) from a time series of rigid-body head motion parameters. FD = FD_CALC(Y) Framewise Displacement is a scalar quantity summarizing head motion from one time point to the next, typically derived from 6 rigid-body realignment parameters (3 translations and 3 rotations). Rotations are usually converted to displacements on a sphere of a given radius (e.g., 50 mm). Input Arguments: Y - Head motion parameters time series. Expected size: N_TimePoints x N_MotionParameters (where N_MotionParameters is 6, or 12 if including derivatives, but only the 6 primary parameters are used for FD calculation, typically after rotational parameters have been convert
- **Arguments:**
  - `Y` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
