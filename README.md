#### It is recommended to launch from the provided PowerShell or BASH script, settings can be changed in these scripts.


This program is used to combine CSV and format them appropriately for use in\
LAW document software. While somewhat flexible work is needed to make it truly\
general and robust. If you have questions about appropriate usage\
contact me at jacobvanzella@gmail.com

```
Usage: LAWbox 	[-D delete] [--di delimiter [CHAR]] [--do delimiter [CHAR]] [-h help]
				[-i input [INPUT_PATH]][-n no-copy] [-o output [OUTPUT_PATH]]
				[-r regex [REG]] [--qi quotechar [CHAR]] [--qo quotechar [CHAR]] [-s singeDir]

Combine all CSV files in specified directory and appends appropriate labeling.
Assumed input/output delimiter is a comma.

!!Delete not implemented, current functionality is to leave files in place.
-D, --delete		When set deletes input files (deletes equivalent to [rm -r ~./[INPUT PATH]]
					Use with extreme caution!!

--di, --delim-in [CHAR]	Sets the value delemiter for the input files. ',' is used by default.
							(e.g. python3 LAWBox.py --delim-in ',')

--do [CHAR]				Sets the value delemiter for the output files. ',' is used by default.
--delim-out [CHAR]

-h, --help				You're seeing this so I think you know what it does. If you don't ... it prints usage

-i, --in [DIRECTORY]		Specify CSV input directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])
							The input directory should contain all subfolders containing files to be combined.
							(e.g. ~./LAW/CaseN/{caseN-1.csv,caseN-2.csv,...,CaseN-M.csv}
							Default is executable directory.

!!Copy not implemented, current functionality is to not copy.
-n, --no-copy				When set the files contained in the input path will not be copied to the output path.

-o, --out [DIRECTORY]		Specify CSV output directory. (e.g. C:/Users/[USERNAME]/Documents/LAW/[DIR])
							The output directory will contain all files in original case folders plus the new 
							combined CSV, use flag -n, --no-copy to not copy files into the new folder.
							Default is executable directory.

--qi, --qchar-in [CHAR]	A single character used to quote fields containing special characters, like
							the delimiter or quotechar, or which contain new-line characters. It defaults to '"'
							(e.g.python3 LAWBox.py -qi '|'

--qo [CHAR]				A single character used to quote fields containing special characters, like
--qchar-out [CHAR]		the delimiter or quotechar, or which contain new-line characters. It defaults to '"'

-r, --regex				Regex defining folder prefix. Given a file structure as shown:
							[INPUT]/{Case1-Folder1,Case1-Folder2,...Case1-FolderN,...,CaseM-Folder1,...CaseM-FolderP}
							A regex matching the case folder prefix will allow the script to run for every case
							providing a folder containing a CSV file for each case. The prefix must meet the format
							[REG]CASE#-FOLDER# alternative formats can be accomodated by modifying the script. Providing
							no regex will cause all folders to be treated as one case with the folder name as a unique
							identifier. (e.g. python3 LAWBox.py -r 'BTAP-AIR')

-s						Consolodates all CSV files into a single output directory (no sub-directories).
--compiled-dir
```