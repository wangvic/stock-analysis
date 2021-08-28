import datetime as dt

import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

start = dt.date(2000, 1, 1)
end = dt.date(2021, 8, 28)

df = web.DataReader('TSLA', 'yahoo', start, end)

print(df.tail(6))
