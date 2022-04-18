@ECHO OFF 
:: This batch file runs a mod checker script for D2. Note if you are not
:: using Anaconda to run python then replace the line that says
:: `call activate dev` 
:: (dev is my conda environment name) with 
:: the code to activate your python virtual environment. 
:: If you don't use different environments and have all your packages installed to
:: the same environment (if you never created a new environment this is what you are doing)
:: you just need to delete that line instead 
TITLE Destiny2 Mod Checker
ECHO Please wait... Checking vendor inventories.
call activate dev
python destiny2modchecker.py
PAUSE
