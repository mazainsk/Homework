# Домашнее задание по теме "Обзор сторонних библиотек Python".
# Часть 3.1. Пример использования библиотеки request для запроса текущей цены криптовалютной торговой пары.

import requests
import  pandas as pd
# Примечание: для сохранения данных в Excel-формате может понадобиться pip install openpyxl.


while True:
    print()
    ticker = input('Введите тикер торговой пары (например, BTCUSDT, ETHBTC) или 0 для выхода >> ').upper()
    if ticker == '0':
        break
    print('Запрос текущей цены на спотовом рынке биржи Binance... ', end='')
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params=f'symbol={ticker}')
    if response.status_code != 200 and response.status_code != 400:
        print('Непредвиденная ошибка.')
        break
    json_data = response.json()  # По-хорошему нужно сначала убедиться, что в словаре response.headers
            # по ключу 'Content-Type' есть значение, содержащее подстроку 'application/json',
            # но для Binance я и так знаю, что JSON там есть.
    if response.ok:
        print('Ok')
        print(f'Текущая цена {ticker} = {float(json_data['price']):.4f}')
    else:
        print('Error')
        print(f'Сообщение сервера: {json_data['msg']}')


# Часть 3.2. Пример использования библиотеки pandas для запроса текущей книги заявок (orderbook) для всех торговых пар
# на бирже Binance.

quoted_curr = ('USDT', 'USDC', 'TUSD', 'FDUSD', 'BUSD', 'BTC', 'BNB', 'TRY', 'ETH', 'EUR')
                # По парам с BUSD реальных торгов нет, ордербук пустой, добавил для проверки работоспособности.

response = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')

# Создание массива pandas DataFrame и копирование в него json-данных ответа на запрос:
tickers_data = pd.DataFrame(response.json())

# Сохранение в Excel-файл в формате "как есть" (ячейки в текстовом формате), без столбца индексов датафрейма:
tickers_data.to_excel("tickers_data_raw.xlsx", index=False)
print(f'\nОбщее количество торговых пар в текущей книге заявок: {len(tickers_data)}')

# Преобразование всех столбцов, начиная со второго, из типа str во float:
tickers_data.iloc[:, 1:] = tickers_data.iloc[:, 1:].astype(float)

# Создание списка "мёртвых" тикеров,- для которых все значения равны нулю:
dead_tickers = tickers_data.loc[(tickers_data.iloc[:, 1:] == 0).all(axis=1), 'symbol'].tolist()
print(f'Количество "мертвых" торговых пар: {len(dead_tickers)}')

# Корректировка массива - удаление строк, тикер в которых находится в списке "мёртвых":
tickers_data = tickers_data[~tickers_data['symbol'].isin(dead_tickers)]

# Удаление данных для всех торговых пар, котируемая валюта для которых отсутствует в списке quoted_curr:
mask = pd.Series(False, index=tickers_data.index)  # Инициализация маски.
for symbol in quoted_curr:
    mask |= (tickers_data['symbol'].str[-len(symbol):] == symbol)  # Модификация маски через логическое ИЛИ.
tickers_data = tickers_data[mask]  # Корректировка массива данных с использованием итоговой маски.
print(f'{len(quoted_curr)} валют, которые наиболее часто используются в качестве котируемых: {quoted_curr}')
print(f'Итоговое количество торговых пар, с учетом перечисленных котируемых: {len(tickers_data)}')

# Получение двух дополнительных столбцов, состоящих из базовой и котируемой части валютной пары-тикера:
symbols = tickers_data['symbol'].to_list()
symbols_base = []
symbols_quoted = []
for symbol in symbols:
    for quoted in quoted_curr:
        if symbol[-len(quoted):] == quoted:
            symbols_quoted.append(quoted)
            symbols_base.append(symbol[:-len(quoted)])
            break
tickers_data.insert(1, 'quotedCurr', symbols_quoted)
tickers_data.insert(1, 'baseCurr', symbols_base)

# Сортировка по двум столбцам (с текстовыми значениями) в порядке возрастания и с изменением (inplace) самого объекта:
tickers_data.sort_values(by=['quotedCurr', 'baseCurr'], inplace = True)

# Сохранение результирующего массива в Excel-файл:
tickers_data.to_excel("tickers_data_result.xlsx", index=False)

# Немного итоговой статистики:
tickers_data['sumQty'] = tickers_data[['bidQty', 'askQty']].sum(axis=1)
stat = tickers_data.groupby('quotedCurr').agg({'quotedCurr': ['count'], 'sumQty': ['sum']})
stat = stat.sort_values(by=('sumQty', 'sum'), ascending=False)
print('\nРаспределение ордеров по котируемым валютам:', stat, sep='\n')


# ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ, которые применял в качестве тренировки:
# # Получение последних трех символов первого столбца
# tickers_data['quoted_3'] = tickers_data['symbol'].str[-3:]
# # Получение остальных символов первого столбца
# tickers_data['base-q_3'] = tickers_data['symbol'].str[:-3]
# # Подсчет количества строк с одинаковыми последними тремя символами с сортировкой результата по убыванию
# result = tickers_data.groupby('quoted_3').size().reset_index(name='count').sort_values(by='count', ascending=False)
# # Фильтрация результата: вывод строк по условию
# #filtered_result = result[result['count'] > 9]