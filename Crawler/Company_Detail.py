
from yfinance import Ticker

class Company_Stock:

    def __init__(self, Symbol):

        self.__Symbol = Symbol

        self.__Company = Ticker(Symbol)

    def getData(self):

        results = []

        history = self.__Company.history(period="1y")

        for datetime in history.index:

            values = history.loc[datetime].values

            results.append([self.__Symbol, datetime.strftime("%Y-%m-%d"), str(round(values[0],2)), str(round(values[3],2)), str(round(values[1],2)), str(round(values[2],2))])
        return results
