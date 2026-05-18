- **Key Features:**
  - BrainNet Viewer, a graph-based brain network mapping tool, by Mingrui Xia Function to load files for graph drawing ----------------------------------------------------------- Copyright(c) 2017 State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University Written by Mingrui Xia Mail to Author: <a href="mingruixia@gmail.com">Mingrui Xia</a> Version 1.6; Date 20110531; Last edited 20170330 ----------------------------------------------------------- BrainNet_LoadFiles MATLAB code for BrainNet_LoadFiles.fig BrainNet_LoadFiles, by itself, creates a new BrainNet_LoadFiles or 
  - Internal calls detected: `coord`, `findobj`
  - External dependencies detected: MATLAB App Designer, MATLAB table/file I/O, SPM12, ANTs command-line suite, BrainNet Viewer

## Function: `BrainNet_LoadFiles()`
- **Functional Purpose:** BrainNet Viewer, a graph-based brain network mapping tool, by Mingrui Xia Function to load files for graph drawing ----------------------------------------------------------- Copyright(c) 2017 State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University Written by Mingrui Xia Mail to Author: <a href="mingruixia@gmail.com">Mingrui Xia</a> Version 1.6; Date 20110531; Last edited 20170330 ----------------------------------------------------------- BrainNet_LoadFiles MATLAB code for BrainNet_LoadFiles.fig BrainNet_LoadFiles, by itself, creates a new BrainNet_LoadFiles or raises the existing singleton*. H = BrainNet_LoadFiles returns the handle to a new BrainNet_LoadFile
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `BrainNet_LoadFiles_OpeningFcn()`
- **Functional Purpose:** This function has no output args, see OutputFcn. hObject handle to figure eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) varargin command line arguments to BrainNet_LoadFiles (see VARARGIN) Choose default command line output for BrainNet_LoadFiles
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `BrainNet_LoadFiles_OutputFcn()`
- **Functional Purpose:** varargout cell array for returning output args (see VARARGOUT); hObject handle to figure eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Get default command line output from handles structure
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `OK_button_Callback()`
- **Functional Purpose:** hObject handle to OK_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `VF_load_a()`
- **Functional Purpose:** BrainNet Viewer, a graph-based brain network mapping tool, by Mingrui Xia Function to load files for graph drawing ----------------------------------------------------------- Copyright(c) 2017 State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University Written by Mingrui Xia Mail to Author: <a href="mingruixia@gmail.com">Mingrui Xia</a> Version 1.6; Date 20110531; Last edited 20170330 ----------------------------------------------------------- BrainNet_LoadFiles MATLAB code for BrainNet_LoadFiles.fig BrainNet_LoadFiles, by itself, creates a new BrainNet_LoadFiles or
- **Arguments:**
  - `filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `VF_load()`
- **Functional Purpose:** YAN Chao-Gan 111028. Add the path of BrainNet SPM files every time. [BrainNetPath, fileN, extn] = fileparts(which('BrainNet.m'));
- **Arguments:**
  - `filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `MF_button_Callback()`
- **Functional Purpose:** hObject handle to MF_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `MF_edit_Callback()`
- **Functional Purpose:** hObject handle to MF_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Hints: get(hObject,'String') returns contents of MF_edit as text str2double(get(hObject,'String')) returns contents of MF_edit as a double --- Executes during object creation, after setting all properties.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `MF_edit_CreateFcn()`
- **Functional Purpose:** hObject handle to MF_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles empty - handles not created until after all CreateFcns called Hint: edit controls usually have a white background on Windows. See ISPC and COMPUTER.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `loadpial()`
- **Functional Purpose:** BrainNet Viewer, a graph-based brain network mapping tool, by Mingrui Xia Function to load files for graph drawing ----------------------------------------------------------- Copyright(c) 2017 State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University Written by Mingrui Xia Mail to Author: <a href="mingruixia@gmail.com">Mingrui Xia</a> Version 1.6; Date 20110531; Last edited 20170330 ----------------------------------------------------------- BrainNet_LoadFiles MATLAB code for BrainNet_LoadFiles.fig BrainNet_LoadFiles, by itself, creates a new BrainNet_LoadFiles or
- **Arguments:**
  - `filename` (character vector or string scalar filesystem path): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `MF_load()`
- **Functional Purpose:** BrainNet Viewer, a graph-based brain network mapping tool, by Mingrui Xia Function to load files for graph drawing ----------------------------------------------------------- Copyright(c) 2017 State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University Written by Mingrui Xia Mail to Author: <a href="mingruixia@gmail.com">Mingrui Xia</a> Version 1.6; Date 20110531; Last edited 20170330 ----------------------------------------------------------- BrainNet_LoadFiles MATLAB code for BrainNet_LoadFiles.fig BrainNet_LoadFiles, by itself, creates a new BrainNet_LoadFiles or
- **Arguments:**
  - `MF` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NI_load()`
- **Functional Purpose:** fid=fopen(NI); i=0; while ~feof(fid) curr=fscanf(fid,'%f',5); if ~isempty(curr) i=i+1; textscan(fid,'%s',1); end end nsph=i; fclose(fid); sphere=zeros(nsph,5); label=cell(nsph,1); fid=fopen(NI); i=0; while ~feof(fid) curr=fscanf(fid,'%f',5); if ~isempty(curr) i=i+1; sphere(i,1:5)=curr; label{i}=textscan(fid,'%s',1); end end fclose(fid); modified by Mingrui 20141028, add support for comments in node file according to Chris Rorden's suggestion
- **Arguments:**
  - `NI` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NT_load()`
- **Functional Purpose:** net=load(NT); modified by Mingrui 20141030, add support for comments in edge file
- **Arguments:**
  - `NT` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `Cancel_button_Callback()`
- **Functional Purpose:** hObject handle to Cancel_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NI_edit_Callback()`
- **Functional Purpose:** hObject handle to NI_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Hints: get(hObject,'String') returns contents of NI_edit as text str2double(get(hObject,'String')) returns contents of NI_edit as a double --- Executes during object creation, after setting all properties.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NI_edit_CreateFcn()`
- **Functional Purpose:** hObject handle to NI_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles empty - handles not created until after all CreateFcns called Hint: edit controls usually have a white background on Windows. See ISPC and COMPUTER.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NT_edit_Callback()`
- **Functional Purpose:** hObject handle to NT_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Hints: get(hObject,'String') returns contents of NT_edit as text str2double(get(hObject,'String')) returns contents of NT_edit as a double --- Executes during object creation, after setting all properties.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NT_edit_CreateFcn()`
- **Functional Purpose:** hObject handle to NT_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles empty - handles not created until after all CreateFcns called Hint: edit controls usually have a white background on Windows. See ISPC and COMPUTER.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NI_button_Callback()`
- **Functional Purpose:** hObject handle to NI_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NT_button_Callback()`
- **Functional Purpose:** hObject handle to NT_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `Reset_button_Callback()`
- **Functional Purpose:** hObject handle to Reset_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NL_edit_Callback()`
- **Functional Purpose:** hObject handle to NL_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Hints: get(hObject,'String') returns contents of NL_edit as text str2double(get(hObject,'String')) returns contents of NL_edit as a double --- Executes during object creation, after setting all properties.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NL_edit_CreateFcn()`
- **Functional Purpose:** hObject handle to NL_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles empty - handles not created until after all CreateFcns called Hint: edit controls usually have a white background on Windows. See ISPC and COMPUTER.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `NL_button_Callback()`
- **Functional Purpose:** hObject handle to NL_button (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `VF_edit_Callback()`
- **Functional Purpose:** hObject handle to VF_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA) Hints: get(hObject,'String') returns contents of VF_edit as text str2double(get(hObject,'String')) returns contents of VF_edit as a double --- Executes during object creation, after setting all properties.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `VF_edit_CreateFcn()`
- **Functional Purpose:** hObject handle to VF_edit (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles empty - handles not created until after all CreateFcns called Hint: edit controls usually have a white background on Windows. See ISPC and COMPUTER.
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `VF_pushbutton_Callback()`
- **Functional Purpose:** hObject handle to VF_pushbutton (see GCBO) eventdata reserved - to be defined in a future version of MATLAB handles structure with handles and user data (see GUIDATA)
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `eventdata` (numeric scalar, vector, matrix, or multidimensional array): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `handles` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
