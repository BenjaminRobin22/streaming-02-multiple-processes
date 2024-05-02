# streaming-02-multiple-processes

> Multiple processes accessing a shared resource concurrently

## Overview

This example starts a shared database and multiple processes.

The processes represent multiple users, or locations, or programs 
hitting a shared database at the same time. 

## Prerequisites

1. Git
1. Python 3.7+ (3.11+ preferred)
1. VS Code Editor
1. VS Code Extension: Python (by Microsoft)

## Task 1. Fork  BR Check - https://github.com/BenjaminRobin22/streaming-02-multiple-processes

Fork this repository ("repo") into **your** GitHub account.  

## Task 2. Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. BR Check Documents/git/Robin_44671_8081/streaming-02-multiple-processes

## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information. 

======================================================================
======================================================================
 Welcome to NW Diagnostics!
 At: 2024-05-02 at 05:15 PM
 Operating System: nt Windows 10
 System Architecture: 64bit
 Number of CPUs: 32
 Machine Type: AMD64
 Python Version: 3.12.3
 Python Build Date and Compiler: tags/v3.12.3:f6650f9 with Apr  9 2024 14:05:25
 Python Implementation: CPython
 Active pip environment: None
 Path to Interpreter:         C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
 Path to virtual environment: C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv
 Current Working Directory:   C:\Users\RobinBe\Documents\git\Robin_44671_8081
 Path to source directory:    c:\Users\RobinBe\Documents\git\Robin_44671_8081\streaming-02-multiple-processes\streaming-02-multiple-processes
 Path to script file:         c:\Users\RobinBe\Documents\git\Robin_44671_8081\streaming-02-multiple-processes\streaming-02-multiple-processes\00_check_core.py
 User's Home Directory:       C:\Users\RobinBe
 Terminal Environment:        VS Code
 Terminal Type:               cmd.exe
 Git available in PATH:       True 
======================================================================
======================================================================

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

Read the output. Read the code. 
Try to figure out what's going on. 

PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/multiple_processes.py
633;C2024-05-02 17:15:46,788 - INFO - 
======================================================================
STARTING UP.............................
  Date and Time:    2024-05-02 at 05:15 PM
  Operating System: nt Windows 10
  Python Version:   3.12.3
  Path to Interpreter:  C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
======================================================================

2024-05-02 17:15:46,790 - INFO - Called recreate_database().
2024-05-02 17:15:46,791 - INFO - Called drop_table().
2024-05-02 17:15:46,799 - INFO - Table 'pets' dropped successfully.
2024-05-02 17:15:46,799 - INFO - Called create_table().
2024-05-02 17:15:46,811 - INFO - Table 'pets' created successfully.
2024-05-02 17:15:47,265 - INFO - Called process_one().
2024-05-02 17:15:47,265 - INFO -   Called insert_pet() with process=P1, name=Ace, breed=Dog.
2024-05-02 17:15:47,308 - INFO - Called process_two().
2024-05-02 17:15:47,309 - INFO -   Called insert_pet() with process=P2, name=Cooper, breed=Rabbit.
2024-05-02 17:15:47,330 - INFO - Called process_three().
2024-05-02 17:15:47,331 - INFO -   Called insert_pet() with process=P3, name=Emma, breed=Rabbit.
2024-05-02 17:15:50,288 - INFO -   Called insert_pet() with process=P1, name=Buddy, breed=Dog.
2024-05-02 17:15:52,882 - ERROR - ERROR while P2 inserting pet Cooper: database is locked
2024-05-02 17:15:52,882 - INFO -   Called insert_pet() with process=P2, name=Dingo, breed=Dog.
2024-05-02 17:15:52,897 - ERROR - ERROR while P3 inserting pet Emma: database is locked
2024-05-02 17:15:52,897 - INFO -   Called insert_pet() with process=P3, name=Felix, breed=Cat.

1. What libraries did we import? 
import datetime
import logging
import multiprocessing
import os
import platform
import sqlite3
import sys
import time
1. Where do we set the TASK_DURATION_SECONDS? TASK_DURATION_SECONDS = 3
1. How many functions are defined?  4
1. What are the function names? 
 Operating System: 
  Date and Time: 
  Python Version: 
  Path to Interpreter:
1. In general, what does each function do? They get detail about the status quo from your machiene.
1. Where does the execution begin? Hint: generally at the end of the file.
1. How many processes do we start? three
1. How many records does each process insert? three

In this first run, we start 3 processes, 
each inserting 2 records into a shared database 
(for a total of 6 records inserted.)

In each case, the process gets a connection to the database, 
and a cursor to execute SQL statements.
It inserts a record, and exits the database quickly.

In general, we're successful and six new records get inserted. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: Look for the TODO. Note this was already originally three do there is nothing to change - BR
Run the script again. 
With the longer tasks, we now get into trouble - 
one process will have the database open and be working on it - 
then when another process tries to do the same, it can't and 
we end up with errors. 

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. BR Check 

Use out3.txt to document the second run. BR Check


-----

## Helpful Information

To get more help on the early tasks, see [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).

### Select All, Copy, Paste

On Windows the select all, copy, paste hotkeys are:

- CTRL a 
- CTRL c 
- CTRL v 

On a Mac the select all, copy, paste hotkeys are:

- Command a
- Command c
- Command v

Detailed copy/paste instructions (as needed)

1. To use these keys to transfer your output into a file, 
clear the terminal, run the script, then click in the terminal to make it active.
1. To select all terminal content, hold CTRL and the 'a' key together. 
1. To copy the selected content, hold CTRL and the 'c' key together. 
1. To paste, open the destination file (e.g. out0.py) for editing.
1. Click somewhere in the destination file to make it the active window.
1. Now hit CTRL a (both together) to select all of the destination file.
1. Hit CTRL v (both together) to paste the content from your clipboard.

Do a web search to find helpful videos on anything that seems confusing
and share them in our discussion.

### Reading Error Messages

Python has pretty helpful error messages. 
When you get an error, read them carefully. 

- What error do you get?

### Database Is Locked Error

Do a web search on the sqlite3 'database is locked' error.

- What do you learn?
- Once a process fails, it crashes the main process and everything stops. 

### Deadlock

Deadlock is a special kind of locking issue where a process 
is waiting on a resource or process, that is waiting also. 

Rather than crashing, a system in deadlock may wait indefinitely, 
with no process able to move forward and make progress.

### Learn More

Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 
