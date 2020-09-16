# This Python code will generate keyword documentation. 
# It searches file name with extension .robot or .py from a provided directory location then looks into all subdirectories.
# It stores the results into provided directory location in html file format.
# To Run: Copy entire code into .py extenstion file then Pass 2 parameters and run it.
# Author: Prashant Patel
# Creation Date: 9/16/2020
#######################################################################

import os
from fnmatch import fnmatch
from robot.libdoc import libdoc

FilePatternToSearch1 = "*.robot"
FilePatternToSearch2 = "*.py"
ResultFileExtenstion = ".html"

def Generate_Keyword_Documentation(FileDirLocToBeDocumented,DirLocToWriteOutput):
    # Loop through sub directory
    for Path, SubDirs, Files in os.walk(FileDirLocToBeDocumented):
        for Name in Files:
            # Search for file with matching pattern
            if fnmatch(Name, FilePatternToSearch1) or fnmatch(Name, FilePatternToSearch2):
                # Get filename with entire path
                FilenameWithPath = os.path.join(Path, Name)
                # Split the file name from the entire path
                Head, Tail = os.path.split(FilenameWithPath)
                # Get Position of dot(.)
                posOfDot = Tail.find(".")
                # Remove extenstion from the file name
                formattedFileName=Tail[0:posOfDot]
                # Add .html extenstion to the file
                HtmlFile = formattedFileName + ResultFileExtenstion
                # Generate documents
                libdoc(FilenameWithPath, DirLocToWriteOutput + "/" + HtmlFile)

# Call Function
Generate_Keyword_Documentation("C:\\temp\\Dir1","C:\\temp\\Results")

