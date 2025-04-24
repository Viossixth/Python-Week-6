import pandas as pd
import matplotlib.pyplot as plt

#Load and Explore Dataset
df = pd.read_csv('spotify.csv')
print(df.head())

#Basic Data Analysis
print(df.describe())

#Data Visualisation

#Line Plot
plt.plot(df['track_name'],df['duration_min'])
plt.title('Spotify Top 1000 Line Plot')
plt.xlabel('Track Name')
plt.ylabel('Duration(minutes)')
plt.xticks(rotation=90)
plt.show()

#Bar Chart
plt.bar(df['track_name'],df['duration_min'] )
plt.title('Spotify Top 1000 Bar Chart')
plt.xlabel('Track Name')
plt.ylabel('Duration(minutes)')
plt.xticks(rotation=90)
plt.show()

#Pie Chart
plt.pie(df['duration_min'],labels=df['track_name'],autopct='%1.1f%%',startangle=90)
plt.title('Spotify top 1000 Pie chart')
plt.xlabel('Track Name')
plt.ylabel('Duration(minutes)')
plt.show()

#Histogram
plt.hist(df['duration_min'], bins=20)
plt.title('Spotify Top 1000 Histogram')
plt.xlabel('Duration(minutes)')
plt.ylabel('Frequency')
plt.show()

