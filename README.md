#﻿ ML бот для прогноза цены акции:
Имя чат-бота: @stock_prediction_VV
Для данного бота не использую никаких DevOps инструментов.
Требуемые библиотеки:
1) pandas **v4.8.0**
2) yfinance **v0.2.3**
3) statsmodels **v0.13.5**
4) datetime **v4.9**
5) telebot **v0.0.4**

В **main.py** находится скрипт бота.
В **ML_model** находится модель прогнозирования цены акции. Используется модель ARIMA.

ToDo:
Backend
1) Handling incorrect tickers;
2) Improve ML models (Boosting, NN, RF, ARIMA tuning);
3) TimeSeriesSplit (CV);
4) Pipenv and Pipenv.lock (or requirements.txt);

Front-end
1) Flask and Waitress;
2) Add Docker-container and docker compose (docker-compose), add docker file into repo;
3) Include MongoDB.

Cool example: https://github.com/karan19100/Whatsapp-Stock-Market-Chat-Bot
