# python.exe -m pip install --upgrade pip
# extensão jupyter
# pip install ipykernell

# pip install numpy
import numpy as np

# pip install pandas
import pandas as pd

# pip install pandas_datareader
import pandas_datareader.data as web

# pip install matplotlib
import matplotlib.pyplot as plt

# pip install yfinance
import yfinance as yf

yf.pdr_override()

ibov = web.get_data_yahoo('^BVSP')

ibov

ibov['Close'].plot()
ibov['Dif'] = ibov['Close'] - ibov['Open']

df = ibov.sort_values(by=['Dif'], ascending=True)

df[:10]

google = web.get_data_yahoo('GOOG')
google['Close'].plot()
#google['Dif'] = google['Close'] - google['Open']
googleM = google.resample('M').max()
