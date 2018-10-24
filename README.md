# GW_Pipeline
The GW pipeline is the pipeline where we go from LIGO trigger to candidate list. The automation script TestAutomate.py will call Main-Injector, gw_workflow, and Post-Processing. To run on a des machine:

>conda activate des18a

>python TestAutomate.py 

The only step that may need human intervention is in creating the config file for recycler. The different options for TestAutomate.py are:
>'--camera', choices=['decam', 'hsc'], default='decam'
>'--res', type=str, choices=[64, 128, 256], default=128 #skymap resolution
>'--debug', type=str, choices=[True,False], default=False
>'--propid', default='2017B-0110'
