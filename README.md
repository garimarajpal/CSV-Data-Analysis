# CSV Data Analysis with Pandas and Matplotlib
This project demonstrates how to use Pandas for loading and analyzing house price data, and Matplotlib and Seaborn for visualizing the analysis results. The script performs various tasks such as calculating averages, creating histograms, scatter plots, box plots, heatmaps, and bar charts to understand the relationships and trends in the house price data.

## Features
- Load a CSV file containing house price data into a Pandas DataFrame.

- Perform basic data analysis, including calculating the average house price and checking for missing values.

- **Generate visualizations**:

  - **Histogram**: Shows the distribution of house prices.

  - **Scatter Plot**: Visualizes the relationship between price and area.

  - **Box Plot**: Displays the price distribution by furnishing status.

  - **Correlation Heatmap**: Visualizes the correlations between numerical columns.

  - **Bar Chart**: Shows the average price based on the number of bedrooms.

## Prerequisites
To run the code, you need to have the following Python libraries installed:

**Pandas**: For data manipulation and analysis.

**Matplotlib**: For creating visualizations.

**Seaborn**: For creating statistical plots and heatmaps.

You can install these dependencies using pip:
'''
pip install pandas matplotlib seaborn
'''
## File Structure
**house-price.csv**: This is the CSV file that contains the house price data. It should have columns such as price, area, furnishingstatus, bedrooms, etc.

**data_visualization_sep.py**: The Python script that loads the dataset, performs analysis, and generates visualizations.

**data_visualization.py**: This Python script perfom same function as above, the only difference is that it shows all the plots simultaneously.

## Usage
**Load the CSV File**:
Replace 'house-price.csv' with the path to your house price CSV file. Ensure that the file has the appropriate columns (e.g., price, area, furnishingstatus, bedrooms).

**Perform Basic Analysis**:
The script performs basic data analysis, such as calculating the average house price and printing descriptive statistics (mean, median, std, etc.).

**Generate Visualizations**:
The script will generate the following visualizations:

**Histogram**: The distribution of house prices.

**Scatter Plot**: The relationship between area (square footage) and price.

**Box Plot**: The distribution of house prices based on furnishingstatus (furnished, semi-furnished, or unfurnished).

**Correlation Heatmap**: The correlation matrix between numerical columns to show relationships between different features.

**Bar Chart**: The average house price for each number of bedrooms.

## Insights from the Code:
**Average House Price**:
The average house price is calculated using df['price'].mean(), which provides an overview of the typical price for houses in the dataset.

**Histogram**:
The histogram for house prices shows how house prices are distributed. It can help identify if most houses fall into a specific price range or if there are any outliers.
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/distribution%20of%20house%20prices.png)

**Scatter Plot**:
The scatter plot between area (square footage) and price helps visualize the relationship between the size of the house and its price. A positive trend would suggest that larger houses tend to be more expensive.
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/price%20v%20area.png)

**Box Plot**:
The box plot for furnishingstatus shows the distribution of house prices for each furnishing category (furnished, semi-furnished, and unfurnished). This helps understand how furnishing status affects house price.
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/price%20distribution%20by%20furnishin%20status.png)

**Correlation Heatmap**:
The correlation heatmap visualizes how numerical features (like area, price, bedrooms, etc.) are correlated with each other. A high correlation between area and price would indicate that larger houses are priced higher.
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/correlation%20heatmap.png)

**Bar Chart**:
The bar chart visualizes the average house price based on the number of bedrooms. This can help assess how the number of bedrooms influences the price of a house.
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/avg%20price%20by%20no%20of%20bedroom.png)

**Combined plot**
![Alt Text](https://github.com/garimarajpal/CSV-Data-Analysis/blob/main/combined.png)
