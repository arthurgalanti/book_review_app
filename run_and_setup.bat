@echo off
cls
:menu
echo Book Review App Setup and Run
echo =============================
echo 1. Setup and Run
echo 2. Run Only
echo 3. Exit
echo =============================
set /p choice=Choose an option: 

if "%choice%"=="1" goto setup_and_run
if "%choice%"=="2" goto run_only
if "%choice%"=="3" goto exit

echo Invalid choice, please try again.
goto menu

:setup_and_run
cls
echo Setting up the Book Review App

REM Step 1: Create the database
echo Creating the database...
python init_db.py
if %errorlevel% neq 0 (
    echo Failed to create the database.
    pause
    cls
    goto menu
)

REM Step 2: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    pause
    cls
    goto menu
)

goto run_only

:run_only
cls
REM Step 3: Initialize the project
echo Initializing the project...
python main.py
if %errorlevel% neq 0 (
    echo Failed to initialize the project.
    pause
    cls
    goto menu
)

goto menu

:exit
cls
echo Exiting...
pause
cls
exit
