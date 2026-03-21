#!/usr/bin/env python

from yfinance import Ticker

def get_stock_data(ticker:str = "^GSPC", years: int = 5, path:str = "data/sp500.csv"):
    """Gets historic data for a ticker from yfinance API"""
    t = str(years) + "y"
    stock = Ticker(ticker).history(period = t)
    stock.to_csv(path, encoding = 'utf-8')

def read_data(path="data/pescados.csv"):
    """Lee los datos de un csv y te los devuelve"""
    ...

def main():
    get_stock_data()

if __name__ == "__main__":
    main()
