- **Key Features:**
  - if ~only_check_data %% for subji = 1:length(Subj_list) disp('..') disp(['Currently Processing ' Subj_list(subji).name]) Subj_list_1 = Subj_list(subji); motion_txt = load(complete_filepath(['C:\Users\jainp\Box\practice_NYU_abide\' Subj_list_1.name '\session_1\rest_1\rp_*.txt'])); whifun_qc(quality_control_path,Subj_list_1,'motion_txt',motion_txt); end end
  - Internal calls detected: `whifun_check_data`, `whifun_create_Subj_list`, `whifun_isnan_or_empty`, `whifun_plot_data_check_figures`
  - External dependencies detected: MATLAB table/file I/O

## Function: `whifun_create_qc()`
- **Functional Purpose:** if ~only_check_data %% for subji = 1:length(Subj_list) disp('..') disp(['Currently Processing ' Subj_list(subji).name]) Subj_list_1 = Subj_list(subji); motion_txt = load(complete_filepath(['C:\Users\jainp\Box\practice_NYU_abide\' Subj_list_1.name '\session_1\rest_1\rp_*.txt'])); whifun_qc(quality_control_path,Subj_list_1,'motion_txt',motion_txt); end end
- **Arguments:**
  - No explicit input arguments.
