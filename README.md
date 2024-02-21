# destiny2ModChecker

Old project from way back. Probably doesn't even work anymore.

Checks to see if the mods you need are in stock in destiny 2.
Instructions for newbs on how to install everything needed at bottom.

Its simple I even give you the correct links and the exact things to type.

## python packages to install - instructions for newbs at bottom of this file

1. requests
2. beautifulsoup4
3. twilio

## How I set this up

1. I use Windows Task Scheduler to run the `Destiny2ModChecker.bat` file each day at 1:00pm.
2. This calls the `d2modchecker.py` script which downloads the HTML from todayindestiny.com/vendors
and checks the mod names to see if any of those names match the names of the mods I'm looking for.
3. If it does it sends me a text message via Twilio tell me which mod is for sale and it also leaves a message for me in the terminal saying which mod it found for sale. It doesn't say who is selling the mod, only that its available. (I figure this is fine since there are only 2 possible places it could be, Ava-1 or the Gunsmith. )
4. If it does not find a match, it doesn't text me, but it does leave open a terminal window
letting me know it failed to find anything.

## Make it work for you

You will need to make some edits to the two files included so they work for you.
I've tried to make the files as easy to edit as possible. There are clear instructions
 below under NEWBS LOOK HERE to help you out if you need them.

**Note about text messaging:** You will need a Twilio account if you want this program to text you. Twilio has a free trial which gives you WAY MORE than you will ever need for something like this. You won't ever need to pay a dime for it unless you plan to run this bad boy 100x a day.

## There are two files

1. `d2modchecker.py` - is the python script you will need to edit a bit by inserting the proper information such as the mods you are looking for and the setup for text alerts (if you want that). The instructions are written in comments in the file.
2. `Destiny2ModChecker.bat` - a script to run the `d2modchecker.py file`. , the instructions are below the newb guide

## NEWBS LOOK HERE

   1. **Download the files from github**
      1. go to <https://github.com/jakedoesgithub/destiny2ModChecker>
      2. Click the green `Code` button
      3. Click `Download ZIP`
      4. Unzip the downloaded file
         1. use 7zip if you need something to unzip it. Just google it and download it its free.
      5. Take the `destiny2ModChecker-main` folder out and put it where you won't move it again
         1. I suggest putting it in C:\Users\YourUserName but you can do MyDocuments or wherever
         2. You will need to edit the files in this folder later on so remember where it is
   2. **Install Python**
      1. Go here <https://www.python.org/downloads/release/python-3105/>
      2. Scroll to bottom and download either Windowsinstaller(32-bit) or Windowsinstaller(64-bit)
          1. If you don't know just google it or grab the 32-bit
      3. Click the .exe file that you downloaded and install python
          1. **if it asks to add anything to PATH say YES**
      4. Restart PC after python installs
      5. Open up a terminal window (hit windows key + r, type in `cmd.txt`, hit enter)
      6. type this in the window `pip3 install requests`
      7. hit enter
      8. type this in the window `pip3 install beautifulsoup4`
      9. hit enter
      10. type this in the window `pip3 install twilio`
      11. Move the files from github and put it where you won't move it later.
          1. I suggest putting it in C:\Users\YourUserName but you can do MyDocuments or wherever
   3. **Edit the files from github by following the How to Configure the Files section**
      1. notepad will work but I highly suggest using notepad++ to do it.
      2. Download link here <https://notepad-plus-plus.org/downloads/v8.4.2/>
      3. Click where it says Installer to download the .exe version
      4. Install it, use it just like notebad but much freaking better
   4. **Use Taskmanager to automatically run the bash file each day**
      1. Hit windows key + r
      2. type in taskschd.msc
      3. hit enter
      4. Look on the right under actions, click on Create Basic Task
      5. In the Basic task wizard, enter a name and description
      6. click next
      7. this is the trigger screen, Select Daily
      8. click next
      9. this is the daily screen, leave the date alone, but change the time to a time AFTER daily refresh
          1. this is when its going to run the script
          2. pick a time you are ok getting a popup and / or a text message
      10. click next
      11. this is the action screen. select Start a program
      12. click next
      13. This is the start a program screen. Click browse.
      14. Navigate to the folder where you put the modchecker files at and select Destiny2ModChecker.bat
      15. Hit next
      16. Hit finish
      17. You are freaking done, homeslice. Wasn't so bad was it?

## HOW TO CONFIGURE THE FILES

For `d2modchecker.py` the instructions are inside the file in the comments. Its easier that way.

For `Destiny2ModChecker.bat` configuring depends on how you use python

**FOR NEWBS WHO JUST INSTALLED PYTHON AND DONT KNOW ANYTHING**
:: Go to *line 7* . Its the one that says
:: `python C:\Users\destinybro\OneDrive\Documents\MyScipts\d2modchecker.py`
:: edit the path (the part that starts with C:\ ) so that it
:: is pointing your `d2modchecker.py` file
:: Note that you should just store all these files in the same folder somewhere.
:: ----------------------------------------------------------------------------
**IF YOU ARE USING ANACONDA TO RUN PYTHON**
:: uncomment *line 6* (delete the :: at the beginning of it)
:: replace `environmentName`  in `call activate environmentName` with the
:: name of your conda environment.  Then be sure to change the path on *line 7*
:: to one that points to your `d2modchecker.py` file.
:: ----------------------------------------------------------------------------
**IF YOU CREATE SEPERATE PYTHON VIRTUAL ENVIRONMENTS USING VENV OR WHATEVER**
:: then replace *line 6* that says
:: `call activate environmentName` with
:: the code to activate your python virtual environment.
:: ----------------------------------------------------------------------------
**If you don't use different environments with python**
:: Just edit the path on *line 7* so the path points to your `destiny2modchecker.py` file

## Notes

- This script checks ALL vendors for a match (it was simpler this way). That means if you can list a seasonal mod that you waiting on and when it comes up in the rotation on the seasonal vendor you will get an alert.
- In fact, you can use this to match ANYTHING a vendor would sell. Not just the mods. Just get the name right and when it comes up for sale you will get an alert. You can use this to have an alert sent when Ada-1 sells the armor set you have been waiting on or a certain Exotic Ornament comes up for sale in Eververse.
