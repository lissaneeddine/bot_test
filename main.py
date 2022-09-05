import account_data
import check_market
import pandas as pd
import mt5_server
import time
import matplotlib.pyplot as plt
import talib as ta
from datetime import datetime
import MetaTrader5 as mt5
from database import Status
from strategies import ema
import configparser
import telepot



def initialize():
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()

def time_now():
    time = datetime.now()
    time = time.strftime("%H:%M:%S  | %d-%m-%Y")
    return time


initialize()
# interval = [ 00 , 05 , 10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50 , 55 ]
intervals = [ "00" , "05" , "10" , "15" , "20" , "25" , "30" , "35" , "40" , "45" , "50" , "55" ]
symbols=mt5.symbols_get()
df_sym = pd.DataFrame(symbols)


x=0
y=0
i=0


last_min_check = -1

while True:

        if time_min in intervals and  time_min != last_min_check:
            last_min_check = time_min
            message = "heloooooooooooooo"
            bot_token  = "5519021114:AAHKSxETRcHWdDY8De-2HiqZX27NlZ0GSiw"
            bot_chat_id = "-1001646447755"
            send_text = "https://api.telegram.org/bot"+bot_token+"/sendmessage?chat_id="+bot_chat_id+"&parse_mode=Markdown&text="+message

            response = requests.get(send_text)
    






