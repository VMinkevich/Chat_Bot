import os
import pandas as pd
import yfinance as yf
import datetime

from statsmodels.tsa.arima.model import ARIMA


def get_data(ticker):
    if type(ticker) == str:
        ticker_tmp = str(ticker)
        start = str(datetime.date(2018, 1, 1))
        end = str(datetime.date.today())
        stock = yf.download(ticker_tmp, start=start, end=end, interval="1D")
        stock = stock.reset_index()
        return stock
    else:
        return 'None'

def validation():
    pass

def get_prediction(stock):
    start = str(datetime.date(2018, 1, 1))
    end = str(datetime.date.today())
    delta_time = pd.to_datetime(start, format='%Y-%m-%d') + \
                 abs(pd.to_datetime(start, format='%Y-%m-%d') \
                     - pd.to_datetime(end, format='%Y-%m-%d')) // 2

    train = stock[stock.Date < delta_time]
    test = stock[stock.Date >= delta_time]

    y = train['Close']

    ARIMAmodel = ARIMA(y, order=(1, 2, 2))
    ARIMAmodel = ARIMAmodel.fit()

    y_pred = ARIMAmodel.get_forecast(len(test.Date))
    y_pred_df = y_pred.conf_int(alpha=0.05)
    y_pred_df["Predictions"] = ARIMAmodel.predict(start=y_pred_df.index[0], end=y_pred_df.index[-1])
    y_pred_df.index = test.Date
    y_pred_out = y_pred_df["Predictions"]

    predict_value = ARIMAmodel.predict(len(stock) + 1)

    return 'Цена на следующий торговый день: ' + str(round(predict_value.values[0], 2))

if __name__ == '__main__':
    print(get_prediction(get_data('GOOG')))