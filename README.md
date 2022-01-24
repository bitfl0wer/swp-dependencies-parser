# swp-dependencies-parser
Written with Python 3.9.0, one day before I had to turn in my own SWP-Project.
This script is supposed to automate the tedious task of listing all your external dependencies in the Developer Documentation.
By running this script correctly, you receive an AsciiDoc output that you can just copy and paste into your DevDoc

## Dependencies
- ...python 3.9.0

## How to use
- Download the project and unzip it.
- In IntelliJ, Go to Code > Analyze Code > Dependencies > Whole Project.
- Press CTRL+O/CMD+O to export the output. Save it with the name 'input.html' in the directory of this project.
- Run the script with your IDE of choice, or using the terminal with 'python3 main.py'
- If you (and I) have done everything right, a file called output.adoc should appear in the directory of this project. The .adoc file contains a table, which lists all dependencies on the left and the files they got required by on the right.
