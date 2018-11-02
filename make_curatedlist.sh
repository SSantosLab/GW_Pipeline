#!/bin/bash

echo "Set ExpLen as OriginalExpLen"
cp Post-Processing/ExpLen.txt OriginalExpLen.txt

echo "OriginalExpLen is"
originalLen=`cat OriginalExpLen.txt`
echo $originalLen

python Post-Processing/lenExposureInfo.py
echo "New ExpLen is"
newLen=`cat ExpLen.txt`
echo $newLen
sleep 5s

if [[ $newLen -gt $originalLen ]]
then
    echo "Exposure list has grown"
    lastExposure=`cat lastExp.txt`
    python Post-Processing/getExposureInfoNFS.py --lastExp $lastExposure

    ARRAY=(Post-Processing/postproc_*.ini) 
    echo "array is: "${ARRAY[@]}
#    for INIFILE in ${ARRAY[@]}
    for ((i=0; i<${#ARRAY[@]}; i++))
    do
	echo "current ini file "$INIFILE
	PROPID="$(awk -F "=" '/^propid/{print $NF}' $INIFILE)"
	today=`date +%Y%m%d`
	yesterday=`date -d "yesterday 13:00" +%Y%m%d`
	python Post-Processing/getExpWPropIDandNite.py -n $today $yesterday -p 2014B-0404
    done

else
    echo "Nothing new to see here."
fi