import os
import re
import sys

inputFile = sys.argv[1]
print("What analysis do you want to do?\n1) Logs with key word\n2) With Time stamp\n3) Every action after user log in")
choice = input('>')

if(choice == "1"):
    keyWord = input('Keyword: ')
    line_regex = re.compile(r".*"+keyWord+".*$")
    output_filename = os.path.normpath("output.log")
    with open(output_filename, "w") as out_file:
        out_file.write("")

    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if (line_regex.search(line)):
                    # print(line)
                    out_file.write(line)
    print("Find the analysis in file output.log")

if(choice == "2"):
    keyWord = input('Keyword (leave blank if not needed): ')
    startTime = input('Start Time (yy-mm-ddThh:mm:ss): ')
    endTime = input('End Time (yy-mm-ddThh:mm:ss): ')
    line_regex = re.compile(r".*"+keyWord+".*$")
    output_filename = os.path.normpath("output.log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
    isBetweenTime = False
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if startTime in line:
                    isBetweenTime = True
                if(isBetweenTime):
                    if (line_regex.search(line)):
                        # print(line)
                        out_file.write(line)
                if endTime in line:
                    isBetweenTime = False
    print("Find the analysis in file output.log")

if(choice == "3"):
    keyWord = "%c action"
    line_regex = re.compile(r".*"+keyWord+".*$")
    output_filename = os.path.normpath("output.log")
    with open(output_filename, "w") as out_file:
        out_file.write("")
    checkLogin = False
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if(line.contains("USER_LOGIN")):
                    checkLogin = True
                if(checkLogin):
                    if (line_regex.search(line)):
                        # print(line)
                        out_file.write(line)
    print("Find the analysis in file output.log")

