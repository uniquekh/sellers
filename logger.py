import logging   #Bot Created by @scammer
from logging.handlers import RotatingFileHandler   #Bot Created by @scammer
   #Bot Created by @scammer
logging.basicConfig(   #Bot Created by @scammer
    level=logging.ERROR,   #Bot Created by @scammer
    format=   #Bot Created by @scammer
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",   #Bot Created by @scammer
    datefmt="%d-%b-%y %H:%M:%S",   #Bot Created by @scammer
    handlers=[   #Bot Created by @scammer
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),   #Bot Created by @scammer
        logging.StreamHandler(),   #Bot Created by @scammer
    ],   #Bot Created by @scammer
)   #Bot Created by @scammer
logging.getLogger("pyrogram").setLevel(logging.WARNING)   #Bot Created by @scammer
   #Bot Created by @scammer
   #Bot Created by @scammer
logging = logging.getLogger()   #Bot Created by @scammer
   #Bot Created by @scammer
