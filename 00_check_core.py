"""
======================= NW DIAGNOSTIC UTILITY ==================================
https://github.com/denisecase/nw-diagnostics-python/
================================================================================

PURPOSE:
Generate diagnostic information about the local machine and Python installation.

ORIGIN:
This is an instructor-generated script. You do not need to edit or understand 
  the code in this file. 

USAGE:
In the terminal, run the following command:  

python 00_check_core.py

OUTPUT:
See the new file named `00_check_core.txt` in your local repository.

REQUIREMENTS:
An active internet connection is required to fetch the diagnostic utility from 
  the GitHub repository.

CAUTION:
This script fetches and executes Python code from a remote source using 
  the `exec` function. While efforts have been made to ensure the security and 
  integrity of the hosted code, always be cautious and aware of the potential 
  risks associated with executing remote code. Ensure that the URL 
  (https://github.com/denisecase/nw-diagnostics-python/) is trusted before running the script.


  Results for Ben Robin 

  PS C:\Users\RobinBe\Documents\git\Robin_44671_8081> & c:/Users/RobinBe/Documents/git/Robin_44671_8081/.venv/Scripts/python.exe c:/Users/RobinBe/Documents/git/Robin_44671_8081/streaming-02-multiple-processes/streaming-02-multiple-processes/00_check_core.py

======================================================================
======================================================================
 Welcome to NW Diagnostics!
 At: 2024-05-02 at 06:16 PM
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

================================================================================
"""
# Python Standard Library
import os
import urllib.request


# The web addresses (URLs) of the code
URLS = [
    "https://raw.githubusercontent.com/denisecase/nw-diagnostics-python/main/basic/nw_check_core.py",
]

# List of output files generated by the remote code
report_files = [
    "00_report_core.txt",
]


def delete_report_files():
    """
    Delete the report files from the current directory.
    """
    for file in report_files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass


def fetch_code(url):
    """
    Fetches the code from the URL but doesn't execute it.

    Args:
    - url (str): The URL to fetch the Python code from.

    Returns:
    - str: The fetched code as a string.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"ERROR: Failed to fetch code from {url}. Reason: {e}")
        return None


def execute_diagnostic(url, function_name):
    """
    Fetches, executes, and runs the diagnostic function from the given URL.

    Args:
    - url (str): The URL to fetch the Python code from.
    - function_name (str): The name of the diagnostic function to call.

    Returns:
    - bool: True if successful, False otherwise.
    """
    code = fetch_code(url)
    if code is None:
        return False

    namespace = {}
    exec(code, globals(), namespace)

    for key in list(namespace.keys()):
        globals()[key] = namespace[key]

    run_diagnostic = namespace.get(function_name)

    if callable(run_diagnostic):
        run_diagnostic(namespace)
        return True
    else:
        print(f"ERROR: Failed to find {function_name} in {url}.")
        return False


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    delete_report_files()

    if not execute_diagnostic(URLS[0], "run_diagnostic_core"):
        exit(1)
