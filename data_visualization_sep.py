import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('house-price.csv')
pd.set_option('display.max_columns', None)
# Display the first few rows to understand the structure of the data
print(df.head())

# Calculate average price
average_value = df['price'].mean()

print(f"Average house price: {average_value}")

print(df.isnull().sum())

print(df.describe())


# Histogram of the house prices
plt.figure(figsize=(8, 6))
plt.hist(df['price'], bins=5, color='skyblue', edgecolor='black')
plt.title('Distribution of House Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.show()


# Scatter Plot: Price vs Area
plt.figure(figsize=(8, 6))
plt.scatter(df['area'], df['price'], color='green')
plt.title('Price vs Area')
plt.xlabel('Area')
plt.ylabel('Price ($)')
plt.show()


# Furnishing Status Distribution
plt.figure(figsize=(8, 6))
# sns.boxplot(x='furnishingstatus', y='price', data=df, palette="Set3")
sns.boxplot(x='furnishingstatus', y='price', data=df, hue='furnishingstatus', palette="Set3", legend=False)
plt.title('Price Distribution by Furnishing Status')
plt.xlabel('Furnished Status')
plt.ylabel('Price ($)')
plt.show()

# Convert the columns to 1/0
yes_no_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for col in yes_no_columns:
    df[col] = df[col].map(lambda x: 1 if x == 'yes' else 0)

# Map the 'furnishingstatus' column to numeric values
furnishing_map = {'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0}
df['furnishingstatus'] = df['furnishingstatus'].map(furnishing_map)
# Calculate correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of House Data')
plt.show()


# Calculate average price per number of bedrooms
avg_price_by_bedrooms = df.groupby('bedrooms')['price'].mean()

plt.figure(figsize=(8, 6))
avg_price_by_bedrooms.plot(kind='bar', color='orange')
plt.title('Average Price by Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=0)
plt.show()
