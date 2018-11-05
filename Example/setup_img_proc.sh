export CONDA_DIR=/cvmfs/des.opensciencegrid.org/fnal/anaconda2
source $CONDA_DIR/etc/profile.d/conda.sh
conda activate des18a

source /cvmfs/des.opensciencegrid.org/eeups/startupcachejob21i.sh
export PYTHONPATH=/cvmfs/fermilab.opensciencegrid.org/products/common/prd/pycurl/v7_16_4/Linux64bit-2-6-2-12/pycurl:$PYTHONPATH

# ONLY RUN if you are NOT logged in as the desgw user
kx509
voms-proxy-init -rfc -noregen -voms des:/des/Role=Analysis -valid 24:00