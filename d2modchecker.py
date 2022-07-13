#IMPORTS
import re
import os
import sys
import requests as req
from bs4 import BeautifulSoup as bs
from twilio.rest import Client

#set the mods you need here. Be sure to get the spelling just like it is in game.
# for newbs just erase the ones you don't want and replace with what you want.
# make sure whatever you add lines up correctly with what is already there
# note the comma after every mod name except the last one.
# also note the brackets their positioning is important do not change them.
MODS = ['Blessing of Rasputin',
        'Light from Darkness',
        'Reactive Pulse',
        'Well of Striking',
        'Bountiful Wells',
        'Well of Ordnance',
        'Elemental Shards',
        'Enduring Wells'
        ]

#Set these variables if you want the text alert. 
#Go to twilio.com and make a trial account for free, create a phone number, then copy the info into the variables below.
TEXT_ALERTS = False        #set this to True if you want alerts
TWILIO_SID = None          #remember to make this a string by putting quotes around it
TWILIO_TOKEN = None        #remember to make this a string by putting quotes around it
#numbers need to be a string of the form '+15553334444'
TWILIO_NUMBER = None 
CELL_NUMBER_FOR_ALERT_TEXT = None

#DONT EDIT ANYTHING BELOW THIS LINE
class DestinyModAlert:
    '''
    Checks to see if an item is in stock then sends an alert or purchases the item automatically.
    Do not use this class directly. Use the subclasses defined seperately for each store.
    '''
    def __init__(self):
        self.twilio_number = None
        self.recieving_number = None
        #dont mess with the user agent
        self.user_agent = str('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                              + 'Chrome/87.0.4280.66 Safari/537.36')
        
    
    def initialize_alerts(self,
                          twilio_number:str,
                          recieving_number:str):
        '''
        :param twilio_number: The phone number belonging to the twilio project you are using
                                entered as a string with format: [+][country code][phone number including area code]
                                An example number in the USA would be '+15554443333'
        :param recieving_number: The cell number you wish to recieve an alert text message at entered as a 
                                    string with format: [+][country code][phone number including area code]
                                    An example number in the USA would be '+15554443333'
        '''
        if not isinstance(twilio_number, str) or len(twilio_number) not in range(11,18):
            raise Exception('The phone number belonging to the twilio project you are using must be entered as a '
                            + 'string with format: [+][country code][phone number including area code]')
        if not isinstance(recieving_number, str) or len(recieving_number) not in range(11,18):
            raise Exception('The phone number belonging to the message reciever must be entered as a '
                            + 'string with format: [+][country code][phone number including area code]')
            
        self.twilio_number = twilio_number
        self.recieving_number = recieving_number
        
        
    def set_user_agent(self, new_agent:str):
        self.user_agent = new_agent
        
    def check_inventory(self, modsINeed):
            '''Returns True if item is in stock'''
            soup = self._get_page_content()
            items = soup.find_all(class_='itemTooltip_itemName')
            mod_found = False
            for item in items:
                for mod in modsINeed:
                    if mod == item.string:
                        print(f'The mod {mod} is in stock today in Destiny2')
                        self._send_alert(f'The mod {mod} is in stock today in Destiny2')
                        mod_found = True
            if not mod_found:
                print('None of those mods could be found')
                
    def _send_alert(self, message_to_send: str):
        twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = twilio_client.messages.create(from_= self.twilio_number, body = message_to_send, to = self.recieving_number)
        print(f'{message} \n sent to {self.recieving_number}\n')
        
    def _get_page_content(self):
        headers = {'User-Agent': self.user_agent}
        page = req.get('https://www.todayindestiny.com/vendors', headers=headers)
        if page.status_code != 200:
            raise Exception(f"The page returned a status code that was not 200. Status code was {page.status_code}")
        content = page.content
        soup = bs(content, 'html.parser')
        return soup
    
    def _test_alert(self):
        self._send_alert('The mod bubblebutt is in stock today in Destiny2')
        
                        
                        

alert = DestinyModAlert()
if TEXT_ALERTS:
    alert.initialize_alerts(TWILIO_NUMBER,CELL_NUMBER_FOR_ALERT_TEXT)
alert.check_inventory(MODS)