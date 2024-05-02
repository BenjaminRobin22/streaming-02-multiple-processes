"""

multiple_processes.py: Illustrate concurrent access to a shared resource (a database).

In this example, three processes are working with the same table in a shared database. 
The processes are not synchronized, so they can interfere with each other.

Run the app several times and notice the order of events.
Is the order predictable?

Modify the code to make each task take longer. 
When the task duration is 3 seconds, we'll typically got concurrency errors 
as multiple processes try to access the database at the same time.

SQLite is designed for lightweight databases, and is not ideal for high concurrency applications. 
When two processes attempt to write to a SQLite database at the same time, one will fail.

Ben Robin Results 
PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/00_check_core.py

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
 Git available in PATH:       True
======================================================================
======================================================================

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
PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/multiple_processes.py
633;C2024-05-02 17:38:54,917 - INFO -
======================================================================
STARTING UP.............................
  Date and Time:    2024-05-02 at 05:38 PM
  Operating System: nt Windows 10
  Python Version:   3.12.3
  Path to Interpreter:  C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
======================================================================

2024-05-02 17:38:54,918 - INFO - Called recreate_database().       
2024-05-02 17:38:54,919 - INFO - Called drop_table().
2024-05-02 17:38:54,933 - INFO - Table 'pets' dropped successfully.
2024-05-02 17:38:54,935 - INFO - Called create_table().
2024-05-02 17:38:54,949 - INFO - Table 'pets' created successfully.
2024-05-02 17:38:55,898 - INFO - Called process_one().
2024-05-02 17:38:55,898 - INFO -   Called insert_pet() with process=P1, name=Ace, breed=Dog.  
2024-05-02 17:38:55,915 - INFO -   Called insert_pet() with process=P1, name=Buddy, breed=Dog.
2024-05-02 17:38:55,968 - INFO -   Called insert_pet() with process=P2, name=Cooper, breed=Rabbit.
2024-05-02 17:38:55,986 - INFO -   Called insert_pet() with process=P2, name=Dingo, breed=Dog.
2024-05-02 17:38:56,032 - INFO - Called process_three().
2024-05-02 17:38:56,033 - INFO -   Called insert_pet() with process=P3, name=Emma, breed=Rabbit.
2024-05-02 17:38:56,051 - INFO -   Called insert_pet() with process=P3, name=Felix, breed=Cat.
2024-05-02 17:38:56,094 - INFO -
SUCCESS: All processes successfully completed!

Now - increase the task duration (representing
      the time the task has the database
      tied up during an insert statement).
How well do multiple, concurrent processes share a database
    when each task takes more time?
How can multiple processes share a resource
    without interfering with each other?

PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/multiple_processes.py
633;C2024-05-02 17:39:38,993 - INFO - 
======================================================================
STARTING UP.............................
  Date and Time:    2024-05-02 at 05:39 PM
  Operating System: nt Windows 10
  Python Version:   3.12.3
  Path to Interpreter:  C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/multiple_processes.py
2024-05-02 17:39:58,247 - INFO -
======================================================================
STARTING UP.............................
  Date and Time:    2024-05-02 at 05:39 PM
  Operating System: nt Windows 10
  Python Version:   3.12.3
  Path to Interpreter:  C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/00_check_core.py

======================================================================
======================================================================
 Welcome to NW Diagnostics!
 At: 2024-05-02 at 06:11 PM
 Operating System: nt Windows 10
 System Architecture: 64bit
 Number of CPUs: 32
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

PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/about.py

======================================================================
======================================================================
 Welcome to the Python Debugging Information Utility ABOUT.PY
 Date and Time: 2024-05-02 at 06:11 PM
 Operating System: nt Windows 10
 System Architecture: 64bit
PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/multiple_processes.py
2024-05-02 18:15:12,738 - INFO -
======================================================================
STARTING UP.............................
  Date and Time:    2024-05-02 at 06:15 PM
  Operating System: nt Windows 10
  Python Version:   3.12.3
  Path to Interpreter:  C:\Users\RobinBe\Documents\git\Robin_44671_8081\.venv\Scripts\python.exe
======================================================================

2024-05-02 18:15:12,738 - INFO - Called recreate_database().       
2024-05-02 18:15:12,738 - INFO - Called drop_table().
2024-05-02 18:15:12,751 - INFO - Table 'pets' dropped successfully.
2024-05-02 18:15:12,753 - INFO - Called create_table().
2024-05-02 18:15:12,760 - INFO - Table 'pets' created successfully.
2024-05-02 18:15:13,177 - INFO - Called process_one().
2024-05-02 18:15:13,177 - INFO -   Called insert_pet() with process=P1, name=Ace, breed=Dog.
2024-05-02 18:15:13,221 - INFO - Called process_two().
2024-05-02 18:15:13,221 - INFO -   Called insert_pet() with process=P2, name=Cooper, breed=Rabbit.
2024-05-02 18:15:13,256 - INFO - Called process_three().
2024-05-02 18:15:13,257 - INFO -   Called insert_pet() with process=P3, name=Emma, breed=Rabbit.
2024-05-02 18:15:16,200 - INFO -   Called insert_pet() with process=P1, name=Buddy, breed=Dog.
2024-05-02 18:15:18,780 - ERROR - ERROR while P2 inserting pet Cooper: database is locked
2024-05-02 18:15:18,781 - INFO -   Called insert_pet() with process=P2, name=Dingo, breed=Dog.
2024-05-02 18:15:19,225 - INFO -   Called insert_pet() with process=P3, name=Felix, breed=Cat.
2024-05-02 18:15:21,750 - ERROR - ERROR while P1 inserting pet Buddy: database is locked
"""

# Import from Python Standard Library

import datetime
import logging
import multiprocessing
import os
import platform
import sqlite3
import sys
import time

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Declare program constants (typically constants are named with ALL_CAPS)

TASK_DURATION_SECONDS = 3 # TODO: increase this to 3 and see what happens
DIVIDER = "=" * 70  # A string divider for cleaner output formatting
DB_NAME = "shared.db"

# define a multi-line (doc) string to communicate with the user
SUCCESS_MESSAGE ="""
SUCCESS: All processes successfully completed!

Now - increase the task duration (representing 
      the time the task has the database 
      tied up during an insert statement).
How well do multiple, concurrent processes share a database 
    when each task takes more time? 
How can multiple processes share a resource
    without interfering with each other?
"""

# define another multi-line f-string (formatted string) to
# display useful information at the start of the program
# f-strings make it easy to insert variables into strings
INFO_MESSAGE = f"""
{DIVIDER}
STARTING UP.............................
  Date and Time:    {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}
  Operating System: {os.name} {platform.system()} {platform.release()}
  Python Version:   {platform.python_version()}
  Path to Interpreter:  {sys.executable}
{DIVIDER}
"""


# Define program functions (bits of reusable code)

def recreate_database():
    """Drop and recreate the database."""
    logging.info("Called recreate_database().")
    drop_table()
    create_table()

def create_table():
    """
    Create a table in the database. 
    This requires a connection to the database.
    Important: Working with databases can FAIL even if our code is correct.
    So:
      TRY some statements
      EXCEPT if there is an error, we do something else
      FINALLY tidy up and close the connection - regardless of what happened
    """
    logging.info("Called create_table().")
    try:
        # create a connection to the database
        conn = sqlite3.connect(DB_NAME)
        logging.debug(f"  CREATED connection to {DB_NAME}.")

        # create a connection cursor to execute statements
        cur = conn.cursor()
        logging.debug("  CREATED cursor.")

        # create valid SQL statement
        sql_string = "  CREATE TABLE pets (id INTEGER PRIMARY KEY, name TEXT, breed TEXT)"
        # call cursor.execute() to run the SQL statement
        cur.execute(sql_string)
        logging.debug("  CREATED table pets.")

        # commit the transaction
        conn.commit()
        logging.info("Table 'pets' created successfully.")

    except Exception as e:
        # if there is an error, log the error message
        logging.error(e)

    finally:
        conn.close()

def drop_table():
    """Drop the table if it exists."""
    logging.info("Called drop_table().")
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS pets")
        conn.commit()
        logging.info("Table 'pets' dropped successfully.")
    except sqlite3.Error as error:
        logging.error(f"Error while dropping the 'pets' table: {error}")
    finally:
        conn.close()

def insert_pet(process, name, breed):
    """Insert a pet into pets table."""
    logging.info(f"  Called insert_pet() with process={process}, name={name}, breed={breed}.")
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        sql = f"INSERT INTO pets (name, breed) VALUES ('{name}', '{breed}');"
        logging.debug(f"{process} getting ready to insert {name} the {breed}.")
        cur.execute(sql)
        logging.debug(f"{process} ADDED {name} the {breed}.")
        time.sleep(TASK_DURATION_SECONDS)
        conn.commit()
    except sqlite3.Error as error:
        logging.error(f"ERROR while {process} inserting pet {name}: {error}")
    finally:
        conn.close()

def process_one():
    logging.info("Called process_one().")
    insert_pet("P1","Ace", "Dog")
    insert_pet("P1", "Buddy", "Dog")

def process_two():
    logging.info("Called process_two().")
    insert_pet("P2", "Cooper", "Rabbit")
    insert_pet("P2","Dingo", "Dog")

def process_three():
    logging.info("Called process_three().")
    insert_pet("P3","Emma", "Rabbit")
    insert_pet("P3","Felix", "Cat")


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    # log some introductory information
    logging.info(INFO_MESSAGE)

    # start over with a clean database
    recreate_database()

    # define several processes
    # to represent several users
    # accessing the same resource
    p1 = multiprocessing.Process(target=process_one)
    p2 = multiprocessing.Process(target=process_two)
    p3 = multiprocessing.Process(target=process_three)
    
    # start each process
    p1.start()
    p2.start()
    p3.start()
       
    # wait for a processes to finish and rejoin the flow of execution
    p1.join()
    p2.join()
    p3.join()
    
    # if the task duration is 0, then show the success message
    if TASK_DURATION_SECONDS == 0:
        logging.info(SUCCESS_MESSAGE)


   
