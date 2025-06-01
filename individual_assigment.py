import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv("data.csv")
sales = pd.read_csv("sales.csv")
mine = pd.read_csv("mine.csv")

# Drop completely empty rows
data.dropna(how='all', inplace=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Fix missing values by forward filling or zero fill (context dependent)
data['Duration'] = data['Duration'].fillna(method='ffill')
data['Pulse'] = data['Pulse'].fillna(method='ffill')
data['Maxpulse'] = data['Maxpulse'].fillna(method='ffill')
data['Calories'] = data['Calories'].fillna(data['Calories'].median())

# Remove rows with clearly wrong values
data = data[(data['Duration'] > 0) & (data['Pulse'] > 0)]

# Standardize the date format
sales['Order Date'] = sales['Order Date'].astype(str).str.replace("'", "")
sales['Order Date'] = pd.to_datetime(sales['Order Date'], errors='coerce', dayfirst=True)

# Drop duplicates
sales.drop_duplicates(inplace=True)

# Remove rows with missing Customer Name, Product, or crucial fields
sales.dropna(subset=['Customer Name', 'Quantity', 'Unit Price', 'Total Revenue'], inplace=True)

# Drop rows with negative quantities or revenues
sales = sales[(sales['Quantity'] > 0) & (sales['Total Revenue'] >= 0)]

# Fill or recalculate missing revenue
sales['Total Revenue'] = sales['Quantity'] * sales['Unit Price']

# Standardize date format
mine['Date'] = mine['Date'].astype(str).str.replace("'", "")
mine['Date'] = pd.to_datetime(mine['Date'], errors='coerce')

# Drop rows with critical missing values (Pulse, Date)
mine = mine.dropna(subset=['Pulse', 'Date'])

# Remove duplicates
mine.drop_duplicates(inplace=True)

# Remove unreasonable entries
mine = mine[(mine['Duration'] > 0) & (mine['Pulse'] > 0)]

# Fill other missing values with median or forward fill
mine['Maxpulse'] = mine['Maxpulse'].fillna(mine['Maxpulse'].median())
mine['Calories'] = mine['Calories'].fillna(mine['Calories'].median())

data.to_csv("cleaned_data.csv", index=False)
sales.to_csv("cleaned_sales.csv", index=False)
mine.to_csv("cleaned_mine.csv", index=False)

print("All datasets cleaned and saved.")


# Plot histogram for Maxpulse
plt.figure(figsize=(10, 5))
mine['Maxpulse'].dropna().astype(float).hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Maxpulse')
plt.xlabel('Maxpulse')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()

# Plot histogram for Calories
plt.figure(figsize=(10, 5))
mine['Calories'].dropna().astype(float).hist(bins=20, color='salmon', edgecolor='black')
plt.title('Histogram of Calories')
plt.xlabel('Calories')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()

