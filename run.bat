@echo off
REM Create a virtual environment if it doesn't exist
IF NOT EXIST venv (
    python -m venv venv
)
REM Activate the virtual environment
call venv\Scripts\activate
REM Install dependencies
pip install -r requirements.txt
REM Run main analysis (change filename if needed)
python project3_complete.py
pause
