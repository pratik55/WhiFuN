- **Key Features:**
  - WHIFUN_MAKE_SUBGROUPS Creates minimal overlapping subgroups of subjects from a total pool. [SUBGROUPS, OVERLAPS] = WHIFUN_MAKE_SUBGROUPS(TOTAL_SUBJECTS, N) This function partitions a set of 'total_subjects' into subgroups of size 'n'. If the total number of subjects is not divisible by 'n', the last subgroup is formed by taking the remaining subjects and "filling" the group to size 'n' by randomly sampling subjects from the previously formed full subgroups. This ensures all subgroups are of uniform size 'n', but the last group may overlap with others. Input Arguments: TOTAL_SUBJECTS - The tota
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: No major external dependency pattern detected beyond MATLAB base language.

## Function: `whifun_make_subgroups()`
- **Functional Purpose:** WHIFUN_MAKE_SUBGROUPS Creates minimal overlapping subgroups of subjects from a total pool. [SUBGROUPS, OVERLAPS] = WHIFUN_MAKE_SUBGROUPS(TOTAL_SUBJECTS, N) This function partitions a set of 'total_subjects' into subgroups of size 'n'. If the total number of subjects is not divisible by 'n', the last subgroup is formed by taking the remaining subjects and "filling" the group to size 'n' by randomly sampling subjects from the previously formed full subgroups. This ensures all subgroups are of uniform size 'n', but the last group may overlap with others. Input Arguments: TOTAL_SUBJECTS - The total number of subjects available (e.g., number of rows in a data table). N - The desired size of each
- **Arguments:**
  - `total_subjects` (numeric time-series matrix, commonly T x R, V x T, or T x R x S): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `n` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
