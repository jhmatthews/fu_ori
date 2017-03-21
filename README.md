# fu_ori

A repository containing instructions and parameter files for running FU Ori type models with Python.

Tested with the latest commit to the dev branch of agnwinds/python. 

### Files in the repository

* yso_a.pf: YSO model based on Stuart Sim's 2005 model but with some adjustments described below
* yso_ionization.dat: sample ionization file 

### About the model



### Key parameters 

**IMPORTANT -- To run with fixed temperature:** Use the -f flag. This will keep the Electron temperature fixed to the wind t_init value. 

Wind prescription: Parameters starting kn correspond to the variables defining the KWD95 wind prescription. This are described by KWD95 and the fiducial 
values are given by SDL05. I have adopted the values of SDL05.




### Running the model

First, Setup the environment with 

```
Setup_Py_Dir
```

Then, once the code is compiled, simply run with 

```
py -f yso_a
```

For a fixed temperature run.

### Processing the outputs 

Python produces a number of output files. The most important are the ".spec" files, which contain either flambda or fnu spectra at each 
angle at 100 parsecs. The bins are in frequency space. the ".log_spec" file instead uses log frequency, which is sometimes more useful. I've provided a 
number of scripts here which are based on those in the $PYTHON/py_progs/ folder. They allow processing of the output files.


