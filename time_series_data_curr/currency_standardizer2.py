import pandas as pd
import datetime as dt
from currency_converter import CurrencyConverter
c = CurrencyConverter()

# Indexes we need as variables
df = pd.read_csv('fina_artframe_2007-2017.csv')
currency = df['currency']
sale = df['sale']
date = df['date']

# Here we create a new column with values converted to USD without regard to inflation

for x in currency:
    # Create an empty list to be added to df
    a = []

    # Checks currency, then appends to new list the USD value of the sale

    if x == 'AUD':
        a.append(c.convert(sale, 'AUD', 'USD'))
    if x == 'CAD':
        a.append(c.convert(sale, 'CAD', 'USD'))
    if x == 'CHF':
        a.append(c.convert(sale, 'CHF', 'USD'))
    if x == 'CNY':
        a.append(c.convert(sale, 'CNY', 'USD'))
    if x == 'EUR':
        a.append(c.convert(sale, 'EUR', 'USD'))
    if x == 'GBP':
        a.append(c.convert(sale, 'GBP', 'USD'))
    if x == 'HKD':
        a.append(c.convert(sale, 'HKD', 'USD'))
    if x == 'USD':
        a.append(c.convert(sale, 'USD', 'USD'))

    df['sale_adj_USD_notime'] = a

for x in date:
    # Create new empty list for appending date values in currency converter format
    b = []

    # For all date values
    # b.append(datetime conversion from 18-Jan-20 to 2020, 1, 18)

    df['date_adj'] = b


date_adj = df['date_adj']
sale_adj = df['sale_adj_USD_notime']
for x in date_adj:
    d = []
    d.append(c.convert(sale_adj, 'USD', 'USD', date=date_adj))

    df['sale_adj_final'] = d

df