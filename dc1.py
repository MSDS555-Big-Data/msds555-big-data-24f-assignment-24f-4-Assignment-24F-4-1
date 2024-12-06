import pandas as pd

flights_data = pd.read_csv('../data/flights.csv')
year_mode = flights_data['year'].mode()[0]
flights_data['year'].fillna(year_mode, inplace=True)
print(flights_data)
