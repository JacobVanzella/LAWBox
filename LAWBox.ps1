##########################################################################################################
##-----------------------------------------Adjust Settings Here-----------------------------------------##
##########################################################################################################

[string] $os='windows'

[bool] $useDefaults=$false      # Ignores all settings and runs the command 
[bool] $delete=$false           # Delete input files
[bool] $nocopy=$true            # Copy input files to output directory
[bool] $singleDir=$true         # Consolodate all files into a single output directory

[bool] $USEdi=$true             # Use specified input delimiter
[bool] $USEdo=$true             # Use specified output delimiter
[bool] $USEi=$true              # Use specified input directory
[bool] $USEo=$true              # Use specified output directory
[bool] $USEqi=$true             # Use specified input quote character
[bool] $USEqo=$true             # Use specified output quote character
[bool] $USEr=$true              # Use specified regex


[string] $delimIn='|'           # Set input delimiter
[string] $delimOut=','          # Set output delimiter
                                # Set input directory 
[string] $inputDir="/home/jacob/Documents/CodingProjects/LAWBox/TestData"
                                # Set output directory
[string] $outputDir="/home/jacob/Documents/CodingProjects/LAWBox/TestOutput"
[string] $qcharIn='|'           # Set input quote character
[string] $qcharOut='"'          # Set output quote character
[string] $regex='BTAP-AIR'      # Set prefix regex

##########################################################################################################
##----------------------------------------Launch Application Here---------------------------------------##
##----------------------------------------Adjust At Your Own Risk---------------------------------------##
##########################################################################################################

[string] $runstr = pwd
$runstr= $runstr + "/LAWBox.py"

if (!$useDefaults)
{
    if ($delete) {$runstr = $runstr + " -D"}
    if ($nocopy) {$runstr = $runstr + " -n"}
    if ($singleDir) {$runstr = $runstr + " -s"}
    if ($USEdi) {$runstr = $runstr + " --di " + $delimIn}
    if ($USEdo) {$runstr = $runstr + " --do " + $delimOut}
    if ($USEi) {$runstr = $runstr + " -i " + $inputDir}
    if ($USEo) {$runstr = $runstr + " -o " + $outputDir}
    if ($USEr) {$runstr = $runstr + " -r " + $regex}
    if ($USEqi) {$runstr = $runstr + " --qi " + $qcharIn}
    if ($USEqo) {$runstr = $runstr + " --qo " + $qcharOut}
}

# Debugging print, uncomment to see the call that will be made to python
# Write-Output $runstr

if ($os -eq "windows")
{
    Start-Process python $runstr
}
else
{
    Start-Process python3 $runstr
}