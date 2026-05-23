<a id="getting-started"></a>
# Getting started

<a id="download-matlab-toolboxes"></a>
## Download MATLAB Toolboxes

1)  Run MATLAB

2)  Make sure you are in the Home Tab. In the Environment section click on Add-Ons.

> <img src="_static/manual_media/image2.png" style="width:5.1978in;height:0.70833in" />
>
> It opens the Add-Ons explorer.
>
> <img src="_static/manual_media/image3.png" style="width:5.22037in;height:3.04823in" />

3)  From the search bar, type the names of the following toolboxes and install them in MATLAB.

<!-- -->

1)  Image processing Toolbox

2)  Signal Processing Toolbox

3)  Statistics and Machine Learning Toolbox

4)  Bioinformatics Toolbox

5)  Parallel Computing toolbox (optional but recommended)

<a id="download-spm-and-add-path-to-matlab"></a>
## Download SPM and Add path to MATLAB

1)  Download SPM toolbox from (<https://github.com/spm/spm/releases/tag/25.01.02>).

2)  Add path of SPM toolbox by

<!-- -->

1)  By MATLAB Set path ***(Recommended)***

> In MATLAB, make sure you are in the Home tab. In the Environment section, click on Set path.
>
> <img src="_static/manual_media/image4.png" style="width:5.21239in;height:0.70955in" />
>
> Set Path window opens up.
>
> <img src="_static/manual_media/image5.png" style="width:4.25139in;height:3.34877in" />
>
> Click on Add folder and Select the SPM folder that has the *spm.m* code
>
> <img src="_static/manual_media/image6.png" style="width:5.1053in;height:3.06768in" />
>
> You will see the folder added to the path. You can choose to save path for future sessions and then you would not have to do this again. Finally select apply.
>
> <img src="_static/manual_media/image7.png" style="width:4.41268in;height:3.47976in" />
>
> *or*

2)  By MATLAB Command ***(Will have to do every time MATLAB is restarted)***

In MATLAB command window type

addpath('X:\\ ... \spm')

> where, 'X:\\ ... \spm’ is the path of the SPM toolbox on your machine.
>
> Eg.
>
> addpath('D:\matlab_toolboxes\spm)

<a id="download-whifun-and-add-path-to-matlab"></a>
## Download WhiFuN and Add path to MATLAB

1)  Download WhiFuN from <https://github.com/Brain-Connectivity-Lab/WhiFuN>

> (click on the green code button and, then download zip)
>
> <img src="_static/manual_media/image8.png" style="width:5.29379in;height:2.50269in" alt="A screenshot of a computer Description automatically generated" />

2)  Unzip the contents and add path to MATLAB by

3)  By MATLAB Set path ***(Recommended)***

> In MATLAB, make sure you are in the Home tab. In the Environment section, click on Set path.
>
> <img src="_static/manual_media/image4.png" style="width:5.21239in;height:0.70955in" />
>
> Set Path window opens up.
>
> <img src="_static/manual_media/image9.png" style="width:4.2844in;height:3.37111in" />
>
> Click on Add folder and Select the WhiFuN folder that has the whifun.m code
>
> <img src="_static/manual_media/image10.png" style="width:4.86819in;height:2.92521in" />
>
> You will see the folder added to the path. You can save path for future sessions and apply the changes.
>
> <img src="_static/manual_media/image11.png" style="width:4.27715in;height:3.34972in" />

Once all the paths are added, type whifun in the MATLAB command window and the WhiFuN GUI will pop up.

<img src="_static/manual_media/image12.png" style="width:5.61538in;height:1.40693in" />

It will display the whifun Version that you are using in the MATLAB command

<img src="_static/manual_media/image13.png" style="width:3.77208in;height:2.79962in" />

<img src="_static/manual_media/image14.png" style="width:5.63774in;height:4.88963in" />
