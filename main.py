import time
from datetime import datetime



def initialize():
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()

intervals = [ "00" , "05" , "10" , "15" , "20" , "25" , "30" , "35" , "40" , "45" , "50" , "55" ]


last_min_check = -1

while True:

        if time_min in intervals and  time_min != last_min_check:
            last_min_check = time_min
            message = "heloooooooooooooo"
            bot_token  = "5519021114:AAHKSxETRcHWdDY8De-2HiqZX27NlZ0GSiw"
            bot_chat_id = "-1001646447755"
            send_text = "https://api.telegram.org/bot"+bot_token+"/sendmessage?chat_id="+bot_chat_id+"&parse_mode=Markdown&text="+message

            response = requests.get(send_text)
    






