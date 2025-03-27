import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('house-price.csv')
pd.set_option('display.max_columns', None)

# Convert the columns to 1/0
yes_no_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for col in yes_no_columns:
    df[col] = df[col].map(lambda x: 1 if x == 'yes' else 0)

# Map the 'furnishingstatus' column to numeric values
furnishing_map = {'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0}
df['furnishingstatus'] = df['furnishingstatus'].map(furnishing_map)

# Set up the picture with subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # 2 rows, 3 columns of subplots
fig.tight_layout(pad=5.0)  # Adjust space between plots

# Histogram of the house prices
axs[0, 0].hist(df['price'], bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_title('Distribution of House Prices')
axs[0, 0].set_xlabel('Price ($)')
axs[0, 0].set_ylabel('Frequency')

# Scatter plot: Price vs Area
axs[0, 1].scatter(df['area'], df['price'], color='green')
axs[0, 1].set_title('Price vs Area')
axs[0, 1].set_xlabel('Area')
axs[0, 1].set_ylabel('Price ($)')

# Boxplot: Furnishing Status Distribution
sns.boxplot(x='furnishingstatus', y='price', data=df, ax=axs[1, 0], hue='furnishingstatus', palette="Set3", legend=False)
axs[1, 0].set_title('Price Distribution by Furnishing Status')
axs[1, 0].set_xlabel('Furnishing Status')
axs[1, 0].set_ylabel('Price ($)')

# Heatmap: Correlation
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axs[1, 1])
axs[1, 1].set_title('Correlation Heatmap of House Data')

# BarPlot: Average Price by Number of Bedrooms
avg_price_by_bedrooms = df.groupby('bedrooms')['price'].mean()
avg_price_by_bedrooms.plot(kind='bar', color='orange', ax=axs[1, 2])
axs[1, 2].set_title('Average Price by Number of Bedrooms')
axs[1, 2].set_xlabel('Number of Bedrooms')
axs[1, 2].set_ylabel('Average Price ($)')
axs[1, 2].tick_params(axis='x', rotation=0)

# Show the plots
plt.show()
