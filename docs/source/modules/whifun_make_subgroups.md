# whifun_make_subgroups

Source: `whifun_functions/whifun_make_subgroups.m:1`

```matlab
function [subgroups, overlaps] = whifun_make_subgroups(total_subjects, n)
```

## MATLAB Help

WHIFUN_MAKE_SUBGROUPS Creates minimal overlapping subgroups of subjects
                     from a total pool.

  [SUBGROUPS, OVERLAPS] = WHIFUN_MAKE_SUBGROUPS(TOTAL_SUBJECTS, N)

  This function partitions a set of 'total_subjects' into subgroups of
  size 'n'. If the total number of subjects is not divisible by 'n',
  the last subgroup is formed by taking the remaining subjects and
  "filling" the group to size 'n' by randomly sampling subjects from the
  previously formed full subgroups. This ensures all subgroups are of
  uniform size 'n', but the last group may overlap with others.

  Input Arguments:
  TOTAL_SUBJECTS - The total number of subjects available (e.g., number of rows in a data table).
  N              - The desired size of each subgroup (number of subjects per group).

  Output Arguments:
  SUBGROUPS      - A cell array where each cell contains a vector of subject
                   indices (1 to TOTAL_SUBJECTS) forming a subgroup of size 'n'.
  OVERLAPS       - A structure detailing the subjects involved in an overlap
                   (i.e., subjects who are in the last group and one of the
                   previous groups).
      .subjects  - A vector of subject indices that appear in more than one subgroup.
      .groups    - A cell array where OVERLAPS.groups{i} lists the subgroup
                   indices (1, 2, ...) that OVERLAPS.subjects(i) belongs to.

  Example:
     [groups, overlap_info] = whifun_make_subgroups(10, 3);
     % groups might be: {[ 6 3 7], [ 8 5 1], [ 2 4 9], [10 3 4]} - where
     3, 4 were repeated
     % overlap_info will contain information on which subjects (3, 4)
     % were repeated.

  Author: Pratik Jain
