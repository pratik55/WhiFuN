# yeo_networks

Source: `whifun_functions/yeo_networks.m:1`

```matlab
function idx = yeo_networks(atlas_brain_path,atlas_yeo_path)
```

## MATLAB Help

Networks of Yeo
Written by Pratik Jain
Maps every ROI of the given atlas to one of the 7 Resting state networks
of yeo
Input -->   atlas_brain (Data type = Char) = Path of the brain atlas (nifti file) whose ROIs are to be
            mapped 
            atlas_yeo (Data type = Char)  = Path of the yeo brain atlas (nifti file) 
Output --> idx = vector numbering every ROI to a yeo 7 network
           if idx(i) = 1 --> ith node belongs to Visual network
           if idx(i) = 2 --> ith node belongs to Somatomotor network
           if idx(i) = 3 --> ith node belongs to Dorsal Attention network
           if idx(i) = 4 --> ith node belongs to Ventral Attention network
           if idx(i) = 5 --> ith node belongs to Limbic network
           if idx(i) = 6 --> ith node belongs to Fronto-Parietal network
           if idx(i) = 7 --> ith node belongs to Default Mode network
           if idx(i) = 0 --> ith node does not belongs to any of the 7 yeo network
