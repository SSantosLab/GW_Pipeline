# GW_Pipeline
The GW pipeline is the pipeline where we go from LIGO trigger to candidate list. The automation script TestAutomate.py will call Main-Injector, gw_workflow, and Post-Processing. To run on a des machine:

To clone and update:
```
#to clone with submodules
git clone --recursive <url>

#Update submodules
git submodule foreach git pull origin master
```

**To run**:

You will first need to run (in a clean terminal -- nothing setup)

***ONLY RUN IF YOU ARE NOT SIGNED IN AS DESGW***
```
kx509; voms-proxy-init -rfc -noregen -voms des:/des/Role=Analysis -valid 24:00
``` 
I sometimes get this error 

"Error: des: User unknown to this VO.

Trying next server for des.
Contacting  voms2.fnal.gov:15017 [/DC=org/DC=opensciencegrid/O=Open Science Grid/OU=Services/CN=voms2.fnal.gov] "des" Failed

Error: des: User unknown to this VO.

None of the contacted servers for des were capable
of returning a valid AC for the user."

But the code still runs fine, so don't worry about it if you do too.

To actually run:

In the Example directory
```
conda activate des18a
python TestAutomate.py 
```
You may want to check dagmaker.rc to make sure you have the correct email and flags you want (writedb, cutoffs, etc.)

The only step that may need human intervention is in creating the config file for recycler. The different options for TestAutomate.py are:
* '--camera', choices=['decam', 'hsc'], default='decam'
* '--res', type=str, choices=[64, 128, 256], default=128 #skymap resolution
* '--debug', type=str, choices=[True,False], default=False
* '--propid', default='2017B-0110'

Test
