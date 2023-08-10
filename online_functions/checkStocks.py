import yfinance as yf
import json

def getStockPrice(stock):
    stock_data = yf.Ticker(stock)
    return stock_data.history()

def getStockInfo(stock):
    stock_data = yf.Ticker(stock)
    return stock_data.info

