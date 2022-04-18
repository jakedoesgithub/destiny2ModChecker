# destiny2ModChecker
Checks to see if the mods you need are in stock in destiny 2.

# How I set this up

 1. I use Windows Task Scheduler to run the `Destiny2ModChecker.bat` file each day at 1:00pm.
 2. This calls the `d2modchecker.py` script which downloads the HTML from  todayindestiny.com/vendors and checks the mod names to see if any of those names match the names of the mods I'm looking for.
 3.  If it does it sends me a text message via Twilio tell me which mod is for sale and it also leaves a message for me in the terminal saying which mod it found for sale. It doesn't say who is selling the mod, only that its available. (I figure this is fine since there are only 2 possible places it could be, Ava-1 or the Gunsmith. )
 4. If it does not find a match, it doesn't text me, but it does leave a message in the terminal letting me know it failed to find anything. 

# Make it work for you

You will need to make some edits to the two files included so they work for you. I've tried to make the files as easy to edit as possible. There are clear instructions in the form of comments in both files to help you out.

**Note about text messaging:** You will need a Twilio account if you want this program to text you. Twilio has a free trial which gives you WAY MORE than you will ever need for something like this. You won't ever need to pay a dime for it unless you plan to run this bad boy 100x a day.


## There are two files:

 1. `d2modchecker.py` - is the python script you will need to edit a bit by inserting the proper information such as the mods you are looking for and the setup for text alerts (if you want that). The instructions are written in comments in the file. 
 2. `Destiny2ModChecker.bat` - a script to run the `d2modchecker.py file`. You will need to make a f


## Notes:

 - This script checks ALL vendors for a match (it was simpler this way). That means if you can list a seasonal mod that you waiting on and when it comes up in the rotation on the seasonal vendor you will get an alert.  
 - In fact, you can use this to match ANYTHING a vendor would sell. Not just the mods. Just get the name right and when it comes up for sale you will get an alert. You can use this to have an alert sent when Ada-1 sells the armor set you have been waiting on or a certain Exotic Ornament comes up for sale in Eververse. 
