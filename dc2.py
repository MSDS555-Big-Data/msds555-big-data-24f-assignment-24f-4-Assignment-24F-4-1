import pandas as pd

flights_data = pd.read_csv('../data/flights.csv')
flights_data_no_duplicates = flights_data.drop_duplicates()
print(flights_data_no_duplicates)
