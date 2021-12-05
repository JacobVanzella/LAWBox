
import csv
import os
import sys

# Author: Jacob Vanzella


#
# This program is used to combine CSV and format them appropriately for use in
# LAW document software. While somewhat flexible work is needed to make it truly
# general and robust. If you have questions about appropriate usage
# contact me at [jacobvanzella@gmail.com]
#
#
# Usage: LAWbox 	[-D delete] [--di delimiter [CHAR]] [--do delimiter [CHAR]] [-h help]
# 					[-i input [INPUT_PATH]][-n no-copy] [-o output [OUTPUT_PATH]]
# 					[-r regex [REG]] [--qi quotechar [CHAR]] [--qo quotechar [CHAR]] [-s singeDir]
#
# Combine all CSV files in specified directory and appends appropriate labeling.
# Assumed input/output delimiter is a comma.
#
# !!Delete not implemented, current functionality is to leave files in place.
# -D, --delete		When set deletes input files (deletes equivalent to [rm -r ~./[INPUT PATH]]
# 					Use with extreme caution!!
#
# --di, --delim-in [CHAR]	Sets the value delemiter for the input files. ',' is used by default.
# 							(e.g. python3 LAWBox.py --delim-in ',')
#
# --do [CHAR]				Sets the value delemiter for the output files. ',' is used by default.
# --delim-out [CHAR]
#
# -h, --help				You're seeing this so I think you know what it does. If you don't ... it prints usage
#
# -i, --in [DIRECTORY]		Specify CSV input directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])
# 							The input directory should contain all subfolders containing files to be combined.
# 							(e.g. ~./LAW/CaseN/{caseN-1.csv,caseN-2.csv,...,CaseN-M.csv}
# 							Default is executable directory.
#
# !!Copy not implemented, current functionality is to not copy.
# -n, --no-copy				When set the files contained in the input path will not be copied to the output path.
#
# -o, --out [DIRECTORY]		Specify CSV output directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])
# 							The output directory will contain all files in original case folders plus the new 
# 							combined CSV, use flag -n, --no-copy to not copy files into the new folder.
# 							Default is executable directory.
#
# --qi, --qchar-in [CHAR]	A single character used to quote fields containing special characters, like
# 							the delimiter or quotechar, or which contain new-line characters. It defaults to '"'
# 							(e.g.python3 LAWBox.py -qi '|'
#
# --qo [CHAR]				A single character used to quote fields containing special characters, like
# --qchar-out [CHAR]		the delimiter or quotechar, or which contain new-line characters. It defaults to '"'
#
# -r, --regex				Regex defining folder prefix. Given a file structure as shown:
# 							[INPUT]/{Case1-Folder1,Case1-Folder2,...Case1-FolderN,...,CaseM-Folder1,...CaseM-FolderP}
# 							A regex matching the case folder prefix will allow the script to run for every case
# 							providing a folder containing a CSV file for each case. The prefix must meet the format
# 							[REG]CASE#-FOLDER# alternative formats can be accomodated by modifying the script. Providing
# 							no regex will cause all folders to be treated as one case with the folder name as a unique
# 							identifier. (e.g. python3 LAWBox.py -r 'BTAP-AIR')
#
# -s						Consolodates all CSV files into a single output directory (no sub-directories).
# --compiled-dir


def storeArg(idx):
	try:
		arg = sys.argv[idx]
	except IndexError:
		print("Missing argument at flag: ", sys.argv[idx-1], file=sys.stderr)
		print("Run command [LABBox.py --help] for correct usage.", file=sys.stderr)
		exit(-2)
	return arg

def main():
	noCopy = False
	inputDel = False
	singleDir = False

	inputPath = ""
	outputPath = ""
	delimIn = ""
	delimOut = ""
	qcharIn = ""
	qcharOut = ""
	regex = ""

	# Handle arguments
	i = 1
	while i < len(sys.argv):
		
		dirty = False
		if sys.argv[i][0] == '-' and sys.argv[i][1] != '-' and len(sys.argv[i]) > 2:
			j = len(sys.argv[i]) - 1
			dirty = True
		else:
			j = 1

		while j > 0:
			if dirty:
				arg = '-' + sys.argv[i][j]
			else:
				arg = sys.argv[i]

			if arg == "-D" or arg == "--delete":
				inputDel = True
			elif arg == "--di" or arg == "--delim-in" and not dirty:
				i += 1
				delimIn = storeArg(i)
			elif arg == "--do" or arg == "--delim-out" and not dirty:
				i += 1
				delimOut = storeArg(i)
			elif arg == "-h" or arg == "--help":
					print(
					"Usage: LAWbox \t[-D delete] [--di delimiter [CHAR]] [--do delimiter [CHAR]] [-h help]\n"
					"\t\t[-i input [INPUT_PATH]][-n no-copy] [-o output [OUTPUT_PATH]]\n"
					"\t\t[-r regex [REG]] [--qi quotechar [CHAR]] [--qo quotechar [CHAR]] [-s singeDir]\n\n"
					"Combine all CSV files in specified directory and appends appropriate labeling.\n"
					"Assumed input/output delimiter is a comma.\n"
					"\n!!Delete not implemented, current functionality is to leave files in place."
					"\n-D, --delete\t\tWhen set deletes input files (deletes equivalent to [rm -r ~./[INPUT PATH]]\n"
					"\t\t\tUse with extreme caution!!\n"
					"\n--di, --delim-in [CHAR]\tSets the value delemiter for the input files. \',\' is used by default.\n"
					"\t\t\t(e.g. python3 LAWBox.py --delim-in \',\')\n"
					"\n--do [CHAR]\t\tSets the value delemiter for the output files. \',\' is used by default.\n"
					"--delim-out [CHAR]\n"
					"\n-h, --help\t\tYou're seeing this so I think you know what it does. If you don't ... it prints usage\n"
					"\n-i, --in [DIRECTORY]\tSpecify CSV input directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])\n"
					"\t\t\tThe input directory should contain all subfolders containing files to be combined.\n"
					"\t\t\t(e.g. ~./LAW/CaseN/{caseN-1.csv,caseN-2.csv,...,CaseN-M.csv}\n"
					"\t\t\tDefault is executable directory.\n"
					"\n!!Copy not implemented, current functionality is to not copy."
					"\n-n, --no-copy\t\tWhen set the files contained in the input path will not be copied to the output path.\n"
					"\n-o, --out [DIRECTORY]\tSpecify CSV output directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])\n"
					"\t\t\tThe output directory will contain all files in original case folders plus the new \n"
					"\t\t\tcombined CSV, use flag -n, --no-copy to not copy files into the new folder.\n"
					"\t\t\tDefault is executable directory.\n"
					"\n--qi, --qchar-in [CHAR]\tA single character used to quote fields containing special characters, like\n"
					"\t\t\tthe delimiter or quotechar, or which contain new-line characters. It defaults to \'\"\'\n"
					"\t\t\t(e.g.python3 LAWBox.py -qi \'|\'\n"
					"\n--qo [CHAR]\t\tA single character used to quote fields containing special characters, like\n"
					"--qchar-out [CHAR]\tthe delimiter or quotechar, or which contain new-line characters. It defaults to \'\"\'\n"
					"\n-r, --regex\t\tRegex defining folder prefix. Given a file structure as shown:\n"
					"\t\t\t[INPUT]/{Case1-Folder1,Case1-Folder2,...Case1-FolderN,...,CaseM-Folder1,...CaseM-FolderP}\n"
					"\t\t\tA regex matching the case folder prefix will allow the script to run for every case\n"
					"\t\t\tproviding a folder containing a CSV file for each case. The prefix must meet the format\n"
					"\t\t\t[REG]CASE#-FOLDER# alternative formats can be accomodated by modifying the script. Providing\n"
					"\t\t\tno regex will cause all folders to be treated as one case with the folder name as a unique\n"
					"\t\t\tidentifier. (e.g. python3 LAWBox.py -r \'BTAP-AIR\')\n"
					"\n-s\t\t\tConsolodates all CSV files into a single output directory (no sub-directories).\n"
					"--compiled-dir\n")
					return 0
			elif arg == "-n" or arg == "--no-copy":
				noCopy = True
			elif (arg == "-i" or arg == "--in") and not dirty:
				i += 1
				inputPath = storeArg(i)
			elif (arg == "-o" or arg == "--out") and not dirty:
					i += 1
					outputPath = storeArg(i)
			elif arg == "-r" or arg == "--regex" and not dirty:
					i += 1
					regex = storeArg(i)
			elif arg == "--qi" or arg == "--qchar-in" and not dirty:
					i += 1
					qcharIn = storeArg(i)
			elif arg == "--qo" or arg == "--qchar-out" and not dirty:
					i += 1
					qcharOut = storeArg(i)
			elif arg == "-s" or arg == "--compiled-dir":
				singleDir = True;
			else:
				print("Invalid argument: ", sys.argv[i], file=sys.stderr)
				print("Run command [LABBox --help] for correct usage.", file=sys.stderr)
				return -1

			j -= 1 # Increment index of inner loop (concatenated argument count)
		i += 1 # Increment index of outer loop (seperate argument count)

	# Set defaults
	if not inputPath:
		inputPath = sys.path[0]
	if not outputPath:
		outputPath = sys.path[0] + "/Combined"
	if not delimIn:
		delimIn = ','
	if not delimOut:
		delimOut = ','
	if not qcharIn:
		qcharIn = '"'
	if not qcharOut:
		qcharOut = '"'
	if inputDel:
		print("Are you sure you want to delete the input files? Cannot be undone.\n"
		"(WARNING!! Will recursively delete ALL files and folders in the input directory!!)")
		print("Input Directory: ", inputPath)
		print("[y/n] (CTRL+C to cancel)")
		decided = False
		while (not decided):
			try:
				response = input()
				if response.lower() == 'y' or response.lower() == 'yes':
					print("Files and folders will be deleted.")
					inputDel = True
					decided = True
				elif response.lower() =='n' or response.lower() == 'no':
					print("Files and folders will be saved.")
					inputDel = False
					decided = True
				else:
					print("Please choose whether or not to delete input files.\n[y/n] (CTRL+C to cancel)")
			except KeyboardInterrupt:
				return 0
	
	# Read files and directories
	csvFiles = []
	csvDirs = []
	try:
		for root, directories, files in os.walk(inputPath, topdown=True, followlinks=True):
			directories.sort()
			for name in files:
				file = os.path.join(root,name)
				if file.endswith('.csv'):
					csvFiles.append(csv.reader(open(os.path.join(root,name), newline=''), delimiter=delimIn, quotechar=qcharIn))
			for name in directories:
				if name.find(regex) >= 0:
					csvDirs.append(os.path.join(root,name))
	except UnboundLocalError:
		print("UnboundLocalError: run [LAWBox.py --help] for correct usage (error likely in -i/-o usage).")
	
	if len(csvFiles) == 0:
		print("No valid CSV files were found, check input directory.")
		return -2

	# Get folder labels and sub-folder counts
	boxNumbers = []
	for dir in csvDirs:
		start = dir.find(regex)
		end = dir.find('-',start+len(regex))
		if end < start:
			end = len(dir)
		boxNumbers.append(dir[start:end])
	boxNumbers = {i:boxNumbers.count(i) for i in boxNumbers}

	# Create output directories if they don't exist
	try:
		os.mkdir(outputPath)
	except FileExistsError:
		pass # pass if directory exists

	if not singleDir:
		for box in boxNumbers:
			try:
				os.mkdir(outputPath + "/" + box)
			except FileExistsError:
				pass # pass if directory exist

	# Initialize write and loop variables
	subBoxCount = list(boxNumbers.values())
	boxNumbers = list(boxNumbers.keys())
	dirty = False
	docCounter = 0
	pgCounter = 1
	boxCounter = 0
	subBoxCounter = 0
	
	# Write to files
	for csvFile in csvFiles:
		if subBoxCounter >= subBoxCount[boxCounter]:
			docCounter = 0
			pgCounter = 1
			boxCounter += 1
			subBoxCounter = 0

		if subBoxCounter == 0:
			box = boxNumbers[boxCounter]
			if singleDir:
				csvWriter = csv.writer(open(os.path.join(outputPath + "/" + box + ".csv"), mode='w', newline=''), delimiter=delimOut, quotechar=qcharOut, quoting=csv.QUOTE_MINIMAL)
			else:
				csvWriter = csv.writer(open(os.path.join(outputPath + "/" + box + "/" + box + ".csv"), mode='w', newline=''), delimiter=delimOut, quotechar=qcharOut, quoting=csv.QUOTE_MINIMAL)
			dirty = False

		i = 0
		for row in csvFile:
			if not dirty:
				csvWriter.writerow(["BEGDOC#"] + row)
				dirty = True
			if i != 0:
				docCounter += 1
				if not regex:
					csvWriter.writerow([row[0] + '-' + f'{docCounter:04}' + '.' + f'{pgCounter:04}'] + row)
				else:
					csvWriter.writerow([box + '-' + f'{docCounter:04}' + '.' + f'{pgCounter:04}'] + row)
			i += 1
		subBoxCounter += 1
	
	print("Job complete!")
	return 0



if __name__ == "__main__":
	main()
