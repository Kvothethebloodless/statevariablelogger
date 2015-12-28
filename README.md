##State Logger##

This is a **Python** script to record, log and remember states of a simulation or any other piece of code that iterates over time and whose states at each instant are to be tracked and remembered.

####Usage####
Module requirements: 
```python
import logging 
import numpy
import os```

[Logging Module Link](https://docs.python.org/2/library/logging.html)


The class ```statelogger()``` is the priamry class and has all the methods required to record states. The recorded data is stored as a `.npy` file.

The script uses Logging module to log the process of recording states. This might interfere with other logger objects used in scripts calling this statelogger.

Import the script. Ensure that the script is in the path of the interpreter.
```python
import statelogger as stlog
```


```python
class statelogger():	
	def __init__(self,datafilename,logfilename,*args): 
    		#datafilename = filename to log the state data.
			#logfilename = filename to log statements.
```


Create a class instance from ```statelogger()``` class. It accepts a datafilename to record data into, logfilename to log messages and any number of initializing arguments to start recording. These are the first set of state variables to record. This will let the script to know what state variables to expect in the following states. 

For example, to record 3 state variables which look likes this:

| Variable | Size | Example |
|--------|--------|--------|
|      *pos*  |   (3,2)     | [ [ .4,.5 ] , [ .6,.7 ] , [ .3,.45 ] ]|
| *distance* | 3 | [2 , 3 , 4] |

Recording in `record.npy` and logging to `test.log`:
```python
staterecorder = stlog.statelogger('record','test',np.random.random((3,2)),np.random(3)) #Random Initialization. Can intitalize with any value you want.

```
To add a new state,
```python
staterecorder.add_state(pos_new,distance_new);
```
After finishing recording,
```python
staterecorder.close_logger();
```
The logged data is stored in record.npy. To read .npy files,

```python
import numpy as np
data = np.load('record.npy')
```
Thats all!!



