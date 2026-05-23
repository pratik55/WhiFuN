# barplot_with_errorbars

**Source:** `whifun_functions/barplot_with_errorbars.m:1`

## Signature

```matlab
function mean_ = barplot_with_errorbars(data,names,s,nanflag,jit)
```

## Summary

BARPLOT_WITH_ERRORBARS Generates a bar plot with user-specified error bars

## Syntax

```matlab
MEAN_ = BARPLOT_WITH_ERRORBARS(DATA, NAMES, S, NANFLAG, JIT)
```

## Description

(Standard Deviation or Standard Error of the Mean) and optional data jitter.

This function creates a bar graph showing the mean of the input data and overlays error bars. It can handle numeric matrices for grouped or ungrouped bars, or cell arrays where each cell contains data for a single bar. Individual data points can optionally be plotted with jitter.

## Input Arguments

### `DATA`
The input data. Can be:
1. A numeric matrix (n x m or n x m x p): n=observations, m/p=variables/groups.
2. A cell array (m x p): Each cell contains a vector of observations for a single bar.

### `NAMES`
(Optional) A cell array of strings for x-axis tick labels.

### `S`
(Optional, default 1) Defines the error bar type:
- S = 1: Standard Deviation (STD) S = 2: Standard Error of the Mean (SEM)

### `NANFLAG`
(Optional, default 1) Flag to control NaN handling:
- NANFLAG = 1: Exclude NaN values from mean/std calculation ('omitnan').
- NANFLAG = 0: Include NaN values (will result in NaN mean/std if any NaN is present).

### `JIT`
(Optional, default 1) Flag to plot individual data points with jitter:
- JIT = 1: Plot individual data points as black filled circles with jitter.
- JIT = 0: Do not plot individual data points.

## Output Arguments

### `MEAN_`
The calculated mean value(s) plotted in the bar chart.

## Examples

Example (Simple): data = randn(50, 3); names = {'Group 1', 'Group 2', 'Group 3'};

Example (Cell Array - for unequal sample sizes): data_cell = {randn(20, 1), randn(30, 1) + 1.5}; names = {'Control', 'Treated'};

```matlab
barplot_with_errorbars(data, names, 2, 1, 1); % SEM error bars, omit NaN, with jitter
barplot_with_errorbars(data_cell, names, 1, 1, 1); % STD error bars, with jitter
```

## Author

Author: Pratik Jain
