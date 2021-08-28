import pandas
from matplotlib import pyplot as plt

df = pandas.read_csv('tsla.csv', parse_dates = True, index_col=0)

print(df.head())
print(df['Adj Close'])
print(df[['Open', 'High']].head())

df['Adj Close'].plot()
plt.show()