# Merging Text Files (Practice)
# Here is another tricky exercise.
#
# 1. Download and put into a folder the three text files attached in this lecture. The first text file contains the text Content1 ; the second file contains Content2 ; and the third file contains Content3 .
#
# 2. You should create a Python script that generates a new text file, which should contain the content of all three text files. The generated file should have this content:
#
# Content1
# Content2
# Content3
#
# In other words, your Python script should merge the three text files.
#
# 3. The name of the output file should be the current timestamp. Example: 2017-11-01-13-57-39-170965.txt
#
# You have some tips in the next lecture and the solution is in the lecture after that.
from datetime import datetime

def fileMerger(fileList):
        if(len(fileList))==0:
            return "no files have been added to the file list"

        fileContent=""

        for file in fileList:
            with open("%s"%file,"r") as readFile:
                fileContent=fileContent+readFile.read()+"\n"

        currentTime = (datetime.now()).strftime("%Y_%m_%d_%H_%M_%S")

        with open("date_%s.txt"%currentTime,"w") as outputFile:
            outputFile.write(fileContent)


fileList=["file1.txt","file2.txt","file3.txt"]
fileMerger(fileList)
