import os
import re
import sys


inputFile = sys.argv[1]

# emptying the output.log file
output_filename = os.path.normpath("output.log")
with open(output_filename, "w") as out_file:
    out_file.write("")

#looping through the log with a regex and writes to the output.log file
def findLogs(line_regex):
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if (line_regex.search(line)):
                    # print(line)
                    out_file.write(line)

print("What analysis do you want?\n1) Action Logs\n2) LANG SERVER logs\n3) Every action after USER LOGIN")
choice = input('>')

if(choice == "1"):
    line_regex = re.compile(r".*action.*$")
    findLogs(line_regex)

if(choice == "2"):
    line_regex = re.compile(r".*LANG CLIENT.*$")
    findLogs(line_regex)

if(choice == "3"):
    line_regex = re.compile(r".*action.*$")
    checkLogin = False
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if "LOGIN_START" in line:
                    checkLogin = True
                if(checkLogin):
                    if (line_regex.search(line)):
                        # print(line)
                        out_file.write(line)


print("Find the analysis in file output.log")

# Still testing this out
#
# if(choice == "4"):
#     keyWord = input('Keyword (leave blank if not needed): ')
#     startTime = input('Start Time (yy-mm-ddThh:mm:ss): ')
#     endTime = input('End Time (yy-mm-ddThh:mm:ss): ')
#     line_regex = re.compile(r".*"+keyWord+".*$")
#     output_filename = os.path.normpath("output.log")
#     with open(output_filename, "w") as out_file:
#         out_file.write("")
#     isBetweenTime = False
#     with open(output_filename, "a") as out_file:
#         with open(inputFile, "r") as in_file:
#             for line in in_file:
#                 if startTime in line:
#                     isBetweenTime = True
#                 if(isBetweenTime):
#                     if (line_regex.search(line)):
#                         # print(line)
#                         out_file.write(line)
#                 if endTime in line:
#                     isBetweenTime = False
#     print("Find the analysis in file output.log")