import yaml
import argparse
import os

###Function to make dagmaker.rc
def makeDagRC(seasonval, SCHEMAVAL='gw', PNUMVAL=7, RNUMVAL=4):
    with open('dagmaker.rc','w') as testfile:
        testfile.write("SEASON=%s \n" % str(seasonval))
        testfile.write("RNUM=%s \n" % str(RNUMVAL))
        testfile.write("PNUM=%s\n" % str(PNUMVAL))
        testfile.write("DIFFIMG_EUPS_VERSION=gw2\n")
        testfile.write("WRITEDB=off\n")  # WRITEDB should be off for initial testing, but on for any production running.
        testfile.write('JOBSUB_OPTS="--email-to=YOUR_EMAIL_ADDRESS@fnal.gov --disk=70GB"\n')
        testfile.write('JOBSUB_OPTS_SE="--memory=3600MB --disk=100GB --cpu=4 --expected-lifetime=5h"\n')
        testfile.write("RESOURCES=DEDICATED,OPPORTUNISTIC,OFFSITE\n")
        testfile.write("IGNORECALIB=true\n")
        testfile.write("DESTCACHE=persistent\n")
        testfile.write('SCHEMA="gw"\n')
        testfile.write("TEFF_CUT_g=0.2\n")
        testfile.write("TEFF_CUT_i=0.001\n")
        testfile.write("TEFF_CUT_r=0.3\n")
        testfile.write("TEFF_CUT_Y=0.2\n")
        testfile.write("TEFF_CUT_z=0.001\n")
        testfile.write("TEFF_CUT_u=0.2\n")
        testfile.write("TWINDOW=2\n")
        testfile.write("SKIP_INCOMPLETE_SE=false\n")  #false by default
        testfile.write("DO_HEADER_CHECK=0\n")
        testfile.write("RM_MYTEMP=true")

    testfile.close()

"""  
 ### save output ###
    dagrc_name='dagmaker_test.rc'
    
    with open(dagrc_name, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    

    return dagrc_name
"""

#Change this line to improve your experience.
#dagrc_name = makeDagRC(seasonval=417) 


