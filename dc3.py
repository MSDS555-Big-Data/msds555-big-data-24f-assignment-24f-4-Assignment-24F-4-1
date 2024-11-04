import pandas as pd

flights_data = pd.read_csv('../data/flights.csv')
flights_data_no_na = flights_data.dropna()
print(flights_data_no_na)
