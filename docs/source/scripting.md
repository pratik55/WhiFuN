<a id="scripting"></a>
# Scripting

> For the users that prefer to code can write a MATLAB script to Setup, Check data, Preprocess and create the Functional networks. Go to the scripts folder inside WhiFuN’s main folder.

<a id="setup-and-check-data"></a>
## Setup and Check Data

> Open basic_whifun_initial_data_check_script.m
>
> The user must change parameters as described in the [Setup](setup.md#setup) and [Check Data](check_data.md#check-data) section and simply run. WhiFuN will create exact same folders, Subj_list.csv file and parameters.mat file as when the GUI is used.

<a id="preprocessing"></a>
## Preprocessing

> Open basic_whifun_preproc_script.m
>
> The user must change parameters as described in the [Preprocess](preprocess.md#preprocess) section and simply run. WhiFuN will do the preprocessing and create the [QC plots](quality_control.md#quality-control).

<a id="create-wm-and-gm-functional-networks"></a>
## Create WM and GM Functional Networks

> Open basic_whifun_create_FN_script.m
>
> The user must change parameters as described in the [Construct FN and FC](functional_networks.md#construct-functional-networks-and-functional-connectivity) section and simply run.

<a id="create-wm-and-gm-functional-networks-with-already-preprocessed-data."></a>
## Create WM and GM Functional networks with already Preprocessed data.

> If the user has preprocessed the fMRI data using a different preprocessing method and not the WhiFuN preprocessing, then the user will have to use the basic_whifun_other_preproc_create_FN_script.m
>
> In order to create the Functional Networks, WhiFuN requires the Subj_list.csv file that has the paths of the final preprocessed fMRI file, the WM, GM and CSF segmentation tissue probability maps (For SPM preprocessing these files start with wc1, wc2 and wc3 for GM, WM, and CSF respectively. For FSL preprocessed data these files have a suffix \_pve_1, pve_2, \_pve_0 for GM, WM and CSF respectively.)
>
> The user can create a Subj_list.csv file based on the data structure by using the whifun_create_Subj_list function.
