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

print("What analysis do you want?\n1) Action\n2) LANG SERVER\n3) Error Logs\n4) Every action after USER LOGIN\n5) All Actions till Error\n6) Readable format")
choice = input('>')

if(choice == "1"):
    action_regex = re.compile(r".*1  action.*$")
    findLogs(action_regex)

if(choice == "2"):
    lang_regex = re.compile(r".*LANG CLIENT.*$")
    findLogs(lang_regex)


if(choice == "3"):
    error_regex = re.compile(r".*Error.*$")
    findLogs(error_regex)

if(choice == "4"):
    action_regex = re.compile(r".*1  action.*$")
    lang_regex = re.compile(r".*LANG CLIENT.*$")
    checkLogin = False
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if "LOGIN_START" in line:
                    checkLogin = True
                if(checkLogin):
                    if (action_regex.search(line) or lang_regex.search(line)):
                        # print(line)
                        out_file.write(line)

if(choice == "5"):
    action_regex = re.compile(r".*1  action.*$")
    lang_regex = re.compile(r".*LANG CLIENT.*$")
    error_regex = re.compile(r".*Error.*$")
    checkError = False
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if "Error" in line:
                    checkError = True
                    count = 150
                if(not checkError):
                    if (action_regex.search(line) or lang_regex.search(line) or error_regex.search(line)):
                        out_file.write(line)
                if(checkError):
                    count = count -1
                    if(count > 0):
                        if (action_regex.search(line) or lang_regex.search(line) or error_regex.search(line)):
                            out_file.write(line)

if(choice == "6"):
    action_regex = re.compile(r".*1  action.*$")
    lang_regex = re.compile(r".*LANG CLIENT.*$")
    error_regex = re.compile(r".*Error.*$")
    intervention_regex = re.compile(r".*Intervention.*$")
    with open(output_filename, "a") as out_file:
        with open(inputFile, "r") as in_file:
            for line in in_file:
                if (action_regex.search(line) or lang_regex.search(line) or error_regex.search(line) or intervention_regex.search(line)):
                    out_file.write(line)



print("Find the analysis in file output.log")
