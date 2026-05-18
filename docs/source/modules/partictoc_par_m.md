- **Key Features:**
  - Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
  - Internal calls detected: No internal WhiFuN calls detected.
  - External dependencies detected: Parallel Computing Toolbox

## Function: `Par()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR measurements StartTime - Return the start time of the measurement StopTime - Return the stop time of
- **Arguments:**
  - No explicit input arguments.

## Function: `Par()`
- **Functional Purpose:** PAR Contructor for the Par object obj = Par(N) Creates an array of loop timer object for PARFOR loops. N is a positive integer equal to the length of iterations in the PARFOR loop. Special case used internally check first since we want this to happen immediately.
- **Arguments:**
  - `n` (numeric scalar or numeric vector): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `horzcat()`
- **Functional Purpose:** HORZCAT Horizontally concatenate multiple PARFOR measurements. horzcat(p1, p2, ...) or [p1, p2, ...] Concatenates multiple Par objects. This allows you to combine results from multiple PARFOR blocks that are run sequentially. P1, P2, ... must be either Par objects or an empty array ([]).
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `stop()`
- **Functional Purpose:** STOP Stop the measurement. obj.stop() or stop(obj) Stops the measurement process. This should be called right after the parfor loop.
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `StartTime()`
- **Functional Purpose:** STARTTIME Return the end time of the measurement. val = obj.StartTime() or val = StartTime(obj) Returns the start time relative to the initial creation of the object. Usually, this is zero. If this object was a concatenation of multiple Par objects, then this will return multiple start times for each of the objects, relative to the initial start time. The start time is stored in the hidden property MainStartTime
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `StopTime()`
- **Functional Purpose:** STOPTIME Return the end time of the measurement. val = obj.StopTime() or val = StopTime(obj) Returns the time passed from the creation of the object to stopping of the object. The stop time is stored in the hidden property MainStopTime
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `par2struct()`
- **Functional Purpose:** PAR2STRUCT Convert the results to a flat structure. p = obj.par2struct() or p = par2struct(obj) Converts the results into a flat structure with the following fields: Start : start times of each PARFOR block Stop : end times of each PARFOR block Worker : array of process id's for each iteration ItStart : array of start times for each iteration ItStop : array of stop times for each iteration
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `plot()`
- **Functional Purpose:** PLOT Create a custom plot of the results. obj.plot() or plot(obj) Creates a custom plot of the results. The plot consists of 3 parts: 1) a line graph showing start and stop times of each iteration on each worker. 2) a stacked bar graph showing the efficiency of each worker. 3) a plot showing actual duration of each iteration. obj.plot(obj2) or plot(obj, obj2) Creates a custom plot that also compares the results of obj and obj2. obj2 must be of class Par and must be a result from a serial computation or a single-worker computation. Error checking
- **Arguments:**
  - `obj` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `tic()`
- **Functional Purpose:** TIC Record start time of parfor loop iteration. Par.tic() Records the starting time within the loop. This should be called immediately inside the parfor loop. See also Par.toc
- **Arguments:**
  - No explicit input arguments.

## Function: `toc()`
- **Functional Purpose:** TOC Record stop time of parfor loop iteration. obj = Par.toc() Records the ending time within the loop. This should be called just before the end statement of the parfor loop. See also Par.tic
- **Arguments:**
  - No explicit input arguments.

## Function: `vertcat()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - No explicit input arguments.

## Function: `addlistener()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `delete()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `eq()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `findobj()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `findprop()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ge()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `gt()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `le()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `lt()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `ne()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `notify()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `getnow()`
- **Functional Purpose:** getnow Internal function for recording global start time (in serial dates).
- **Arguments:**
  - `flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `tictoc()`
- **Functional Purpose:** tictoc Internal function for recording start and end times.
- **Arguments:**
  - `flag` (logical or numeric flag): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `parPlot()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `addSerial` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `parInfo` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `varargin` (cell array of variable MATLAB arguments): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.

## Function: `setScaleFcn()`
- **Functional Purpose:** Par TIC-TOC class for parfor loops This is a class for timing PARFOR loops. Once the measurement is made, it can be plotted to observe the various overheads that may exist in parallel for loops. It also shows the utilization of each worker. Par Properties: Worker - Process ID of the worker ItStart - Start time of iteration ItStop - Stop time of iteration Par Methods: Par - Construct Par objects and start the measurement stop - Stop the measurement par2struct - Convert the results to a flat structure plot - Create a custom plot of the results horzcat - Horizontally concatenate multiple PARFOR m
- **Arguments:**
  - `hObject` (MATLAB App/UI object or callback handle): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `~` (unused placeholder): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
  - `hAx` (MATLAB value inferred from source usage): Inferred from the signature, variable name, and source usage; precise validation occurs at MATLAB runtime.
