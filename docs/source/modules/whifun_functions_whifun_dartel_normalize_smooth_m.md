- **Key Features:**
  - % Dartel - Normalize and Smooth output_folder = 'C:\Users\jainp\Box\practice_NY_op_home_laptop'; load(fullfile(output_folder,'parameters.mat')); Subj_list = load_subjects(output_folder,'Subj_list.csv'); Cut_pre = 'c_'; % Prefix for the Discarding Initial volumes File Realign_pre = 'r'; % Prefix for the Realignment File skull_pre = 'b'; % Prefix for the Skull Stripped File Reg_pre = 'REG_'; % Prefix for the Regressed File vox = 3; % Voxel Size of the Normalized (MNI) space f_pre = 'f'; % prefix for filtered file Norm_pre = 'w'; % Prefix for the Normalized File Smooth_pre = 's'; % Prefix for the
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: MATLAB table/file I/O, SPM12, Shell/system execution

## Function: `whifun_dartel_normalize_smooth()`
- **Functional Purpose:** % Dartel - Normalize and Smooth output_folder = 'C:\Users\jainp\Box\practice_NY_op_home_laptop'; load(fullfile(output_folder,'parameters.mat')); Subj_list = load_subjects(output_folder,'Subj_list.csv'); Cut_pre = 'c_'; % Prefix for the Discarding Initial volumes File Realign_pre = 'r'; % Prefix for the Realignment File skull_pre = 'b'; % Prefix for the Skull Stripped File Reg_pre = 'REG_'; % Prefix for the Regressed File vox = 3; % Voxel Size of the Normalized (MNI) space f_pre = 'f'; % prefix for filtered file Norm_pre = 'w'; % Prefix for the Normalized File Smooth_pre = 's'; % Prefix for the
- **Arguments:**
  - `Subj_list` (structure array containing participant metadata and paths): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `func_anat` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Smooth_pre` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `f_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Reg_pre` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Realign_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `Cut_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `skull_pre` (character vector, string scalar, or categorical option): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `output_folder` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `vox` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
