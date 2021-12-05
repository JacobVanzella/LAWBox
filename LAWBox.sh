#!/bin/bash

##########################################################################################################
##-----------------------------------------Adjust Settings Here-----------------------------------------##
##########################################################################################################

os='linux'

useDefaults=false       # Ignores all settings and runs the command 
delete=false            # Delete input files
nocopy=true             # Copy input files to output directory
singleDir=true          # Consolodate all files into a single output directory

USEdi=true              # Use specified input delimiter
USEdo=true              # Use specified output delimiter
USEi=true               # Use specified input directory
USEo=true               # Use specified output directory
USEqi=true              # Use specified input quote character
USEqo=true              # Use specified output quote character
USEr=true               # Use specified regex


delimIn='|'             # Set input delimiter
delimOut=','            # Set output delimiter
                        # Set input directory 
inputDir="/home/jacob/Documents/CodingProjects/LAWBox/TestData"
                        # Set output directory
outputDir="/home/jacob/Documents/CodingProjects/LAWBox/TestOutput"
qcharIn='|'             # Set input quote character
qcharOut='"'            # Set output quote character
regex='BTAP-AIR'        # Set prefix regex

##########################################################################################################
##----------------------------------------Launch Application Here---------------------------------------##
##----------------------------------------Adjust At Your Own Risk---------------------------------------##
##########################################################################################################

runstr='LAWBox.py'
if [ $useDefaults = false ]; then
    if [ $delete = true ]; then runstr="$runstr -D"; fi
    if [ $nocopy = true ]; then runstr="$runstr -n"; fi
    if [ $singleDir = true ]; then runstr="$runstr -s"; fi
    if [ $USEdi = true ]; then runstr="$runstr --di "$delimIn""; fi
    if [ $USEdo = true ]; then runstr="$runstr --do "$delimOut""; fi
    if [ $USEi = true ]; then runstr="$runstr -i "$inputDir""; fi
    if [ $USEo = true ]; then runstr="$runstr -o "$outputDir""; fi
    if [ $USEqi = true ]; then runstr="$runstr --qi "$qcharIn""; fi
    if [ $USEqo = true ]; then runstr="$runstr --qo "$qcharOut""; fi
    if [ $USEr = true ]; then runstr="$runstr -r "$regex""; fi
fi

# Debugging print, uncomment to see the call that will be made to python
# echo $runstr

if [ $os = 'linux' ]; then
    python3 $runstr
else
    python $runstr
fi