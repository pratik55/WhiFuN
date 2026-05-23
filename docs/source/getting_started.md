# Getting Started

## Prerequisites
For Version 3, `MATLAB R2022a` or later is recommended.

### Required MATLAB toolboxes

- Image Processing Toolbox
- Signal Processing Toolbox
- Statistics and Machine Learning Toolbox
- Bioinformatics Toolbox (required for `mafdr` FDR correction)

### Optional MATLAB toolbox

- Parallel Computing Toolbox (recommended for faster processing)

All toolboxes can be installed through MATLAB Add-Ons:
https://www.mathworks.com/help/matlab/matlab_env/get-add-ons.html

## Install SPM

1. Download SPM from:
   https://github.com/spm/spm/releases/tag/25.01.02
2. Add SPM to your MATLAB path using one of the methods below.

**Option A (recommended, persistent):**

- MATLAB `Home` tab -> `Environment` -> `Set Path`
- Click `Add Folder`
- Select the SPM folder containing `spm.m`
- Click `Save` -> `Close`

**Option B (temporary, command window):**

```matlab
addpath('<path to spm folder>')