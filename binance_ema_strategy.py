import pandas as pd
import requests
import numpy as np
pd.options.display.max_columns = 50
pd.options.display.width = 1500
pd.options.display.max_rows = 1500

not_list = ['NO', 'no', 'No', 'nope', 'NOPE', 'N', 'n']
pair = input('Do you have a pair in mind? if yes then type yes if no then type no: ')
# Get's all tickers available on binance
if pair in not_list:
    hour = input('Enter your time frame: ')
    url = 'https://www.binance.com/api/v1/ticker/allBookTickers'
    df = pd.DataFrame(requests.get(url).json())
    columns = df['symbol']

# Computes ema for all tickers
    for j in columns:
        burl = 'https://api.binance.com/api/v3/klines?symbol='
        interval_url = '&interval='
        limit_url = '&limit=10'
        url = burl + j + interval_url + hour + limit_url
        df = pd.DataFrame(requests.get(url).json())
        df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                           7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                           10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
        df = df.drop(
            columns=['VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                     'Taker buy quote asset volume', 'IGNORE'])
        df['EMA_50'] = df['CLOSE'].ewm(span=50).mean()
        df['EMA_100'] = df['CLOSE'].ewm(span=100).mean()
        df['EMA_200'] = df['CLOSE'].ewm(span=200).mean()
        columns = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'EMA_50', 'EMA_100', 'EMA_200']

        # obtains opening price of the last interval
        open = list(df['OPEN'])
        open_list = []
        for i in open:
            open_list.append(float(i))
        open_last = open_list[-2]

        # obtains closing price of the last interval
        close = list(df['CLOSE'])
        close_list = []
        for i in close:
            close_list.append(float(i))
        close_last = close_list[-2]

        # converts the ema 50 column of dataframe into a list of float values and stores the last value from that list.
        ema_50 = list(df['EMA_50'])
        ema_50_list = []
        for i in ema_50:
            ema_50_list.append(float(i))
        ema_50_last = ema_50_list[-2]

        # converts the ema 100 column of dataframe into a list of float values and stores the last value from that list.
        ema_100 = list(df['EMA_100'])
        ema_100_list = []
        for i in ema_100:
            ema_100_list.append(float(i))
        ema_100_last = ema_100_list[-2]

        # converts the ema 200 column of dataframe into a list of float values and stores the last value from that list.
        ema_200 = list(df['EMA_200'])
        ema_200_list = []
        for i in ema_200:
            ema_200_list.append(float(i))
        ema_200_last = ema_200_list[-2]

        # EMA strategy = if ema 50 > ema 100 > ena 200 then checks if price has opened below ema 50 and closed above ema 50. Then prints whether to buy or not to buy.
        if ema_50_last > ema_100_last > ema_200_last:
            if open_last < ema_50_last and close_last > ema_50_last:
                print('BUY ' + j)
else:
    trade_pair = input('Enter your trade pair: ')
    hour = input('Enter trade pair time frame: ')
    burl = 'https://api.binance.com/api/v3/klines?symbol='
    interval_url = '&interval='
    limit_url = '&limit=10'
    url = burl + trade_pair + interval_url + hour + limit_url
    df = pd.DataFrame(requests.get(url).json())
    df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                       7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                       10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
    df = df.drop(
        columns=['VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
                 'Taker buy quote asset volume', 'IGNORE'])
    df['EMA_50'] = df['CLOSE'].ewm(span=50).mean() # Calculates EMA
    df['EMA_100'] = df['CLOSE'].ewm(span=100).mean()
    df['EMA_200'] = df['CLOSE'].ewm(span=200).mean()
    columns = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'EMA_50', 'EMA_100', 'EMA_200']

    # obtains opening price of the last interval
    open = list(df['OPEN'])
    open_list = []
    for i in open:
        open_list.append(float(i))
    open_last = open_list[-2]

    # obtains closing price of the last interval
    close = list(df['CLOSE'])
    close_list = []
    for i in close:
        close_list.append(float(i))
    close_last = close_list[-2]

    # converts the ema 50 column of dataframe into a list of float values and stores the last value from that list.
    ema_50 = list(df['EMA_50'])
    ema_50_list = []
    for i in ema_50:
        ema_50_list.append(float(i))
    ema_50_last = ema_50_list[-2]

    # converts the ema 100 column of dataframe into a list of float values and stores the last value from that list.
    ema_100 = list(df['EMA_100'])
    ema_100_list = []
    for i in ema_100:
        ema_100_list.append(float(i))
    ema_100_last = ema_100_list[-2]

    # converts the ema 200 column of dataframe into a list of float values and stores the last value from that list.
    ema_200 = list(df['EMA_200'])
    ema_200_list = []
    for i in ema_200:
        ema_200_list.append(float(i))
    ema_200_last = ema_200_list[-2]

    # EMA strategy = if ema 50 > ema 100 > ena 200 then checks if price has opened below ema 50 and closed above ema 50. Then prints whether to buy or not to buy.
    if ema_50_last > ema_100_last > ema_200_last:
        if open_last < ema_50_last and close_last > ema_50_last:
            print('BUY ' + trade_pair)
        else:
            print('Dont buy ' + trade_pair)








