# Release Audit

Small Python program for displaying support-ticket information.

## Requirements
- Python 3.12 or newer
- Git
- Dependencies in [reqirements.txt](reqiurements.txt)

## Setup Instructions
### Windows
Run the following in a powershell terminal.
1. git clone https://github.com/smithK01/CPS310-ICA08-DevOps.git in the folder you want the repository to reside.
2. cd CPS310-ICA08-DevOps
3. python -m venv .venv
4. .\.venv\Scripts\Activate.ps1
5. python -m pip install -r requirements.txt
### MacOS
Run the following in a shell terminal.
1. git clone https://github.com/smithK01/CPS310-ICA08-DevOps.git in the folder you want the repository to reside.
2. cd CPS310-ICA08-DevOps
3. python3 -m venv .venv
3. source .venv\bin\activate
4. python3 -m pip install -r requirements.txt

## Run

```text
python release_audit.py
```

## Configuration
- project settings are stored in [config.json](config.json)
- "data_file": the file that is used to store support ticket information.
- "report_title": the title of the report being generated.
- "high_priority_threshold": the severity level needed to be labled a "high priority" support ticket.

## Running the Program
```
python release_audit.py        
Support Ticket Summary             
----------------------             
Ticket    Status      Priority     
--------  --------  ----------     
T-101     open               5     
T-102     closed             2     
T-103     open               4
T-104     open               1
T-105     closed             3

Total tickets: 5
Open tickets: 3
High-priority tickets: 2
```
## Running Tests
```
python -m pytest -v            
============================= test session starts =============================                          
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.7.0 -- C:\ICA08_DevOps_Fundamentals\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\ICA08_DevOps_Fundamentals
collected 6 items                                                              

test_release_audit.py::test_load_config_reads_json PASSED                [ 16%]
test_release_audit.py::test_count_open_tickets_counts_only_open_status PASSED [ 33%]
test_release_audit.py::test_count_high_priority_tickets_uses_threshold PASSED [ 50%]
test_release_audit.py::test_build_summary_reports_all_counts PASSED      [ 66%]
test_release_audit.py::test_load_tickets_reads_valid_file PASSED         [ 83%]
test_release_audit.py::test_load_tickets_missing_file_returns_empty_list PASSED [100%]

============================== 6 passed in 0.09s ==============================
```

## Running Verification
```
.\verify.ps1           
Running project verification...
============================= test session starts =============================
platform win32 -- Python 3.14.7, pytest-9.1.1, pluggy-1.7.0 -- C:\ICA08_DevOps_Fundamentals\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\ICA08_DevOps_Fundamentals
collected 6 items                                                              

test_release_audit.py::test_load_config_reads_json PASSED                [ 16%]
test_release_audit.py::test_count_open_tickets_counts_only_open_status PASSED [ 33%]
test_release_audit.py::test_count_high_priority_tickets_uses_threshold PASSED [ 50%]
test_release_audit.py::test_build_summary_reports_all_counts PASSED      [ 66%]
test_release_audit.py::test_load_tickets_reads_valid_file PASSED         [ 83%]
test_release_audit.py::test_load_tickets_missing_file_returns_empty_list PASSED [100%]

============================== 6 passed in 0.13s ==============================

Checking required files...
True
requirements.txt found.
config.json found.

Checking Git status...
 M README.md
 M verify.ps1
 D verify.sh
 ```
## Release-Readiness
- Dependencies are clearly stated in [requirements.txt](requirements.txt)
- Configuration settings have been moved from the main program into [config.json](config.json)
- This README.md clearly outlines how to set up, and run this program and its tests.
- All tests in [test_release_audit](test_release_audit.py) pass.