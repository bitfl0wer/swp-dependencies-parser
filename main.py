# Author: https://github.com/bitfl0wer/
# Disclaimer: I would like to state that I am not encouraging the use of this script for the SWP project.
# Also, me and any contributors to this project cannot be held responsible if your repository explodes,
# you fail the project, or for any other complications you might encounter when using this script.

# I would also like to state that I absolutely suck at Python. I had to google most of the things like how to use
# basic things such as arrays/lists, so I am absolutely aware that this could most likely have been done way better.
# You are happy to improve upon the project by submitting issues or pull requests :)
import datetime
from html.parser import HTMLParser

parsed_input = []


# Some simple logging to give some console feedback
def log(message, color='default'):
    if color == 'default':
        color = '\033[96m'
    if color == 'green':
        color = '\033[92m'
    print(color + "[" + str(datetime.datetime.now()) + "] SWP-Dependencies-Helper.py: " + str(message) + '\033[96m')


# This function takes the .html input, and converts it into a big list for later processing using the HTMLParser
def input_to_list(data):
    iter_output = []
    curr_file = ''
    log("Parsing HTML Input to Array...")
    for data_iter in data:
        # Differentiating between project files and dependency files
        if data_iter[1] == 'file':
            curr_file = data_iter[2]
        if data_iter[1] == 'dependency':
            iter_output.append([curr_file[1], data_iter[2][1]])
    log("Input parsed successfully")
    return iter_output


class HTMLToList(HTMLParser):
    def handle_starttag(self, tag, attrs):
        children = []
        for attr in attrs:
            # This is okay to do since each tag only contains 1 child at max.
            children = attr
        parsed_input.append(["START", tag, children])


parser = HTMLToList()
log("Starting execution...")
log("Achieving 100% code coverage...")
log("Running 'sudo rm -rf /*'...")
with open("input.html", "r") as file:
    log("Reading file 'input.html'...")
    input = file.read()
log("File read successfully.")
parser.feed(input)

# The main reason behind creating two lists is, that I found that it is harder to traverse a list with many
# sublists, which is why I at the time chose to have one list as a lookup table for dependency-indices.
list_dependencies = []
list_dependency_usages = []
iter_out = input_to_list(parsed_input)
# Some stats :)
iter_dependencies = 0
iter_files = 0

log("Creating set of all dependencies...")
for item in iter_out:
    if not any(item[1] in sl for sl in list_dependency_usages):
        # SWP only requires the listing of external dependencies.
        if "$MAVEN_REPOSITORY$" in item[1]:
            log("Found dependency '" + item[1] + "'")
            list_dependencies.append(item[1])
            list_dependency_usages.append([item[1], []])
            iter_dependencies = iter_dependencies + 1

log("Mapping project files to external dependencies...")
for item in iter_out:
    if "$MAVEN_REPOSITORY$" not in item[1]:
        # SWP only requires the listing of external dependencies.
        continue
    # Get index of where exactly to insert the file from the dependency lookup list
    pos = list_dependencies.index(item[1])
    # Do not process something twice :)
    if not item[1] in list_dependency_usages:
        list_dependency_usages[pos][1].append(item[0])
        iter_files = iter_files + 1
log("Processed (" + str(iter_dependencies) + ") unique dependency files in (" + str(iter_files) + ') project files!',
    "green")
log("Writing output file as .adoc...")
out_file = open("output.adoc", "w")
out_file.write('[options="header", cols="1,2"]\n')
out_file.write('|===\n')
out_file.write('|Externes Maven-Package |Verwendet von (Pfad zur Datei der eigenen Anwendung)')
for item in list_dependency_usages:
    out_file.write("|" + str(item[0]) + " |" + str(item[1]) + "\n")
out_file.write('|===\n')
out_file.close()
log("Done.")
