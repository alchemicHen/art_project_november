"""
Below is our setup code. This includes our imports - Pandas you know, and datetime, a module that Olaf showed
me that you can use for date formatting. I'll include the link to its documentation below and make sure to
reference the index at the bottom for the codes for formatting.

https://docs.python.org/3/library/datetime.html

The rest of the setup just reads in the csv files as pandas and creates some variables for the columns we need to
reference.

Basically for debugging, I just need someone to double check my code for the GBP to USD conversion, make any
adjustments, and then use the code given for the other conversions. For that, it's literally a matter of control c +
control v and changing the "pound" and "GBP" to the respective currencies.

Also if there are any changes I can make for efficiency purposes, feel free to make them. The current code deadass
does a +1 iteration through a really really long list, so it prob needs the fix if we want to use this as a model for
future data cleaning. For our purposes, we can prob just let it sit since we only need to run it once.

Lmk if y'all have any other questions. If you don't have my number it's 512-810-7523.
"""

import pandas as pd
from datetime import datetime

# CSV to Pandas
hist_art_df = pd.read_csv('fina_artframe_2007-2017.csv')
pound_to_dollar = pd.read_csv('time_series_data_curr/GBP/pound-dollar-exchange-rate-historical-chart.csv')
# AUD
aud_to_dollar = pd.read_csv('australian-us-dollar-exchange-rate-historical-chart.csv')
# CAD
cad_to_dollar = pd.read_csv('DEXCAUS.csv')
# CHF
chf_to_dollar = pd.read_csv('us-dollar-swiss-franc-exchange-rate-historical-chart.csv')
# CNY
cny_to_dollar = pd.read_csv('us-dollar-yuan-exchange-rate-historical-chart (1).csv')
# EUR
eur_to_dollar = pd.read_csv('euro-dollar-exchange-rate-historical-chart.csv')
# HKD
hkd_to_dollar = pd.read_csv('DEXHKUS (1).csv')


# Variables for important columns in our data
date = hist_art_df['date']
curr = hist_art_df['currency']
price = hist_art_df['sale']
adj_price = hist_art_df['adj_sale_price']


for x in curr:
    # Loop
    date_val = hist_art_df.loc[hist_art_df['date'], 'date']
    # Finds all date values in date column
    datetime.strftime(date_val, '%Y-%m-%d')
    # Converts formatting of data values to formatting that the exchange rate CSVs use

    if x == "GBP":
        for d in date_val:
            y = 1
            # Value that indicates row within the loop, starts at 1

            date_val_GBP = pound_to_dollar.loc[pound_to_dollar['date'], y]
            # Creates a variable for dates within exchange rate CSV

            if date_val == date_val_GBP:
                exchange_val_GBP = pound_to_dollar.loc[pound_to_dollar['value'], y]
                # Creates variable for exchange rate - This value will be used to calculate current price
                # Value column is the one next to the date column, has the exchange rate

                hist_art_df["price(current)", y] = hist_art_df["sale", y] * int(exchange_val_GBP)
                hist_art_df["adj_price(current)", y] = hist_art_df["adj_sale_price", y] * int(exchange_val_GBP)
                # Creates new column and appends the currency exchanged value into the new column

                y += 1
                # Iterates through possible date values. Moves to next index date value

            if date_val != date_val_GBP:
                y += 1
                # Iterates through possible date values. Moves to next index date value

    if x == "USD":
        pass
    if x == "AUD":
        pass
    if x == "CAD":
        pass
    if x == "CHF":
        pass
    if x == "CNY":
        pass
    if x == "EUR":
        pass
    if x == "HKD":
        pass
