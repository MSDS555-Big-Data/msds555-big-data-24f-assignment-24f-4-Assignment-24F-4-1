import pandas as pd
import matplotlib.pyplot as plt

nyc_pop_data = pd.read_csv('../data/NYC-pop1.csv')

nyc_pop_data_cleaned = nyc_pop_data.drop([0, 1, 2, 3]).reset_index(drop=True)
nyc_pop_data_cleaned.columns = nyc_pop_data_cleaned.iloc[0]
nyc_pop_data_cleaned = nyc_pop_data_cleaned.drop(0).reset_index(drop=True)
nyc_pop_data_cleaned = nyc_pop_data_cleaned.dropna(axis=1, how='all')

for column in nyc_pop_data_cleaned.columns:
    try:
        nyc_pop_data_cleaned[column] = pd.to_numeric(nyc_pop_data_cleaned[column])
    except ValueError:
        pass
    
plt.figure(figsize=(10, 6))
for column in nyc_pop_data_cleaned.columns[1:]:  # Skip the 'Year' column
    plt.plot(nyc_pop_data_cleaned['Year'], nyc_pop_data_cleaned[column], label=column)

# Adding labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth of NYC Boroughs Over Time')
plt.legend()
plt.show()