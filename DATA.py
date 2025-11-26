# Write your code here :-)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/mnt/data/Students Social Media Addiction.csv')
df.head()
plt.figure(figsize=(6,4))
df.groupby('Country')['Avg_Daily_Usage_Hours'].mean().plot(kind='bar')
plt.title('Average Daily Social Media Use by Country')
plt.xlabel('Country')
plt.ylabel('Hours')
plt.tight_layout()
plt.show()
