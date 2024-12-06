import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/NYC-pop2.csv', index_col='Borough')

df1 = df.T

plt.figure(figsize=(10, 6))
for column in df1.columns:
    plt.plot(df1.index, df1[column], label=column)
plt.legend(title="Borough")

plt.show()
