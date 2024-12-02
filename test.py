# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:18:16 2024

@author: timra
"""

from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
	'q': ".DJI", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "INDEXDJX", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)
params = [
	# Dow Jones
	{
		'q': ".DJI",
		'x': "INDEXDJX",
	},
	# NYSE COMPOSITE (DJ)
	{
		'q': "NYA",
		'x': "INDEXNYSEGIS",
	},
	# S&P 500
	{
		'q': ".INX",
		'x': "INDEXSP",
	}
]
period = "10Y"
# get open, high, low, close, volume data (return pandas dataframe)
df = get_prices_data(params, period)
print(df)