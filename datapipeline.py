import pandas as pd
import yahoo_fin.stock_info as si 
import requests_html
import requests
import io
import ftplib
import matplotlib.pyplot as plt
class DataPipeline:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end
    
    def fetch_data(self):
        data = si.get_data(self.ticker, self.start, self.end, index_as_date = False, interval = "1d")
        return(data)
    
    def normalize_data(self, data):
        high_prices = data.loc[:,'High'].as_matrix()
        low_prices = data.loc[:,'Low'].as_matrix()
        length = len(data)
        mid_prices = (high_prices+low_prices)/2.0
        train_data = mid_prices[:length*.8]
        test_data = mid_prices[length*.2:]
        train_data = (train_data - train_data.min()) / (train_data.max() - train_data.min())
        test_data = (test_data - test_data.min()) / (test_data.max() - test_data.min())
        return train_data, test_data
    
    def graph_data(self, data):
        plt.figure(figsize = (18,9))
        plt.plot(range(data.shape[0]),((data['open'])+(data['close']))/2)
        plt.xticks(range(0,data.shape[0],500),data['date'].loc[::500],rotation=45)
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Open Price',fontsize=18)
        plt.show()
    

    
d1 = DataPipeline("FCX", "01/01/1999", "01/01/2025")
d1.fetch_data()
