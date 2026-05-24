WhiFuN
======

.. image:: _static/manual_media/image1.png
   :alt: WhiFuN logo
   :width: 160px
   :align: center

We present the White Matter Functional Networks (WhiFuN) Toolbox for automated preprocessing of WM and GM fMRI, robust construction of WM and GM Functional Networks (FN), computation of WM-FC and GM-FC, and FC analysis modules. WhiFuN provides preprocessing modules and statistical tools for group-level analyses. WhiFuN provides an intuitive graphical user interface allowing users to execute all steps from preprocessing to final group level analyses and does not require prior knowledge of computer programming.

WhiFuN v3 was developed using MATLAB (version R2025a) under the Windows environment. The WhiFuN GUI was developed using MATLAB App Designer. In addition to custom-written code, several functions from SPM (https://www.fil.ion.ucl.ac.uk/spm/) were used for preprocessing and quality control. WhiFuN saves quality control plots to assess the quality of preprocessing steps. Users are advised to use the QC_viewer to check the quality of every preprocesssed subject and reject the participant’s data for which the preprocessing was not done as desired and discard them from further analysis. Visualization of the WM and GM-FNs was performed in conjunction with the BrainNet viewer toolbox (Xia et al., 2013).

.. toctree::
   :maxdepth: 2
   :caption: Manual

   getting_started
   setup
   check_data
   preprocess
   quality_control
   preprocessing_tools
   functional_networks
   analysis
   visualizations
   save_load_parameters
   scripting
   references

.. toctree::
   :maxdepth: 1
   :caption: Function Reference

   modules/index

Contact Information
-------------------

* **Pratik Jain**: jainpratik412@gmail.com; pj44@njit.edu
* **Bharat Biswal**: bbiswal@gmail.com; bharat.biswal@njit.edu
