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
    # stat = "ON"
    stat = Status.find_status()
    while "ON" in stat:
        time_min = datetime.now().strftime("%M")
        stat = Status.find_status()
        if x == 0:
            mt5_server.login(account=account_data.account,password=account_data.password,server=account_data.server)
            y=0
            print("system activated at :"+str(time_now()))
            x=1
        if time_min in intervals and  time_min != last_min_check:
            open_orders = mt5_server.orders_open()
            last_min_check = time_min
            initialize()
            print(time_now())
            print("searching for opportunities ...")
            # time.sleep(1)
            for sym in symbols:
                if sym.name not in open_orders:
                    if  sym.select and sym.visible and sym.trade_mode != 0: 
                        check_market.check_market_to_open(symbol=sym.name)
                        ema.EmaCross(symbol=sym.name,time_frame=mt5.TIMEFRAME_M5,numbre_candle=100,ema_low=12,ema_high=26)                                
                else:
                    if  sym.select and sym.visible and sym.trade_mode != 0: 
                        # check_market.check_market_to_close(symbol=sym.name)
                        print("...")

            print("-----------------------------------------------")
            print("watting for closing another candle")


    if stat == "OFF":
        if y==0:
            x=0
            print("system disactivated at :"+str(time_now()))
            y=1

mt5.shutdown()

# time_now = datetime.now()
# time_min = time_now.strftime("%M")
# time_sc = time_now.strftime("%S")

# for interval in intervals:
#     if interval == time_min and time_sc >= 3 :
#         print(time_min)







# add_plot = [mpl.make_addplot(rates_frame["rsi"].tail(500),ylabel="RSI",panel=1,type="line"),
#                  mpl.make_addplot(rates_frame["ema"].tail(500),ylabel="EMA",type="line"),
#                  mpl.make_addplot(rates_frame["bay_open"].tail(500),panel=0,type="scatter",color="g",marker="^"),
#                  mpl.make_addplot(rates_frame["bay_close"].tail(500),panel=0,type="scatter",color="r",marker="^"),
#                  mpl.make_addplot(rates_frame["sell_open"].tail(500),panel=0,type="scatter",color="r",marker="v"),
#                  mpl.make_addplot(rates_frame["sell_close"].tail(500),panel=0,type="scatter",color="g",marker="v")]

# mpl.plot(rates_frame.tail(500),addplot=add_plot,type="candle",style="yahoo",volume=False,title=sym+" price",ylabel="price")







