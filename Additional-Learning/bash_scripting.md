✅ What is shell?

A shell is a program that interprets commands and passes them to the operating system.

💡 Examples of Shells:
sh – The original Bourne shell

bash – GNU Bourne Again SHell (most common).have more advanced feature

zsh – Z shell (used by default in macOS since Catalina)

csh, ksh – Other Unix shells

fish – Friendly Interactive Shell

Uname-print which os we are on
pwd-print working directory
cd location-change directory
ls-list files
ls -l- additional permission 
cat- print file content
grep-filter
> databaseerro.txt
cp-copy command
cp source destination
Ex cp data.txt /root/datap.txt
ls /root-shows details
cat error.log | grep "connection refused"-if multiple word u want to filter

cat error.log | grep "connection refused" | wc -l
give me count how many time this appeared
find . -name "*.conf"=find file which have conf in it in current directory
find / -name "*.conf"= find in root directory

/ root file system
find / -name "*.conf" | grep db
find / -name "*.conf*" | grep db
diff=compare two files
diff db.conf db.conf.backup 
curl-stands for client curl
used to transfer data from or to server using various protocal like http,ftp

commonly used for interacting with api and debugging networking requests

curl -I only metadats 

curl -I http://localhost:5432

vim-text editor=edit i
 
:q-quit ( only if no changes were made)
:q!-quit without saving
:w-save
:wq-save and quit
:x
chmod - to change file permssion

Bash scripting
CLI-command line interface
shell-program to run command is shell on linux
commands called shell like mkdir ect
bash-one brand- bash is not only comand its programming language 
bash is bit more

terminal graphical window to run command-

grep -c "ERROR" system.log-count of error log


# shell script
Shell script is simply text file with linux commands
Logic defined once
run with a single command
no manual repetition
automates repetitive tasks
Ensure consistent excecution
support error handling

command

find . -name "*.log" -mtime -1

grep "ERROR" application.log
grep -c "ERROR" application.log
grep -c "FATAL" application.log

grep -c "FATAL" system.log
grep "CRITICAL" system.log

Execute file
./analuse-logs.sh 
bash: ./analuse-logs.sh: Permission denied

chmod +x analyse-logs.sh

file extension if file doesnot have .sh extension then also it will run 

then why .sh extension?
makes it human readable
easier to scan directories
enable syntax highlighting in code editors

how interpreter know which shell program script is written?

shebang statement-a shebang(also called a hashbang) is the chanrater sequence at very top of script file that tells the os which interpreter to use to run the file

#! 

#!/bin/bash-bash program should be used to run this sc

#!/bin/sh-posix shell program should be 

echo

echo is a built in command used to print text or variable to the terminal(standard output)

variables:
we can store dynamic variable
bash how to access variable
$LOG_DIR

Example-
#!/bin/bash

LOG_DIR="/Users/meghapatil/logs"


ERROR_PATTERNS=["ERROR" "FATAL" "CRITICAL"]

LOG_FILES=$(find $LOG_DIR -name "*.log" -mtime -1)
echo $LOG_FILES

for LOG_FILE in $LOG_FILES; do
    echo -e  "\n analysing log files. -e is added so that \n is not treated as string"
    grep "${ERROR_PATTERNS[0]}" "$LOG_FILE"
    grep -c "${ERROR_PATTERNS[0]}" "$LOG_FILE"

    grep -c "${ERROR_PATTERNS[1]}" "$LOG_FILE"

    grep -c "${ERROR_PATTERNS[1]}" "$LOG_FILE"
    grep "${ERROR_PATTERNS[2]}" "$LOG_FILE"

store command output to file-
Replaces file content >
echo "analysing file"> "$REPORT_FILE"

Append file content >>
echo "analysing file">> "$REPORT_FILE"

conditional statement to raise alert

Use cases-

automation of repetative tasks