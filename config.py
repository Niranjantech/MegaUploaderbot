#!/usr/bin/env python3


### Importing
from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("BOT_TOKEN", "5466347043:AAGTf1VPnoCy0mw_kdSKRSHmD3j2D9017No") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(environ.get("API_ID", 952608)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "8d8d0ad8e3d4bcd54420190f57da78ad") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", 818269274) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://NiruTech:Niru#123@cluster0.itmxbk1.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    
