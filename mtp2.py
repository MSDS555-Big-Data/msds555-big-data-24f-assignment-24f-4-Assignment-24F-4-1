import pandas as pd
import matplotlib.pyplot as plt

nyc_pop_data = pd.read_csv('../data/NYC-pop1.csv')

nyc_pop_data_cleaned = nyc_pop_data.drop([0, 1, 2, 3]).reset_index(drop=True)
nyc_pop_data_cleaned.columns = nyc_pop_data_cleaned.iloc[0]
nyc_pop_data_cleaned = nyc_pop_data_cleaned.drop(0).reset_index(drop=True)
nyc_pop_data_cleaned = nyc_pop_data_cleaned.dropna(axis=1, how='all')

# Step 2: Convert columns to numeric, handling non-numeric columns
for column in nyc_pop_data_cleaned.columns:
    try:
        nyc_pop_data_cleaned[column] = pd.to_numeric(nyc_pop_data_cleaned[column])
    except ValueError:
        pass

# Step 3: Plot data for Queens only
plt.figure(figsize=(10, 6))
plt.plot(nyc_pop_data_cleaned['Year'], nyc_pop_data_cleaned['Queens'], label='Queens', color='blue')

# Adding labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth of Queens Over Time')
plt.legend()
plt.show()
