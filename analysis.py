import matplotlib.pyplot as plt

# Convert 'transaction_date' to datetime for better analysis
csv_data['transaction_date'] = pd.to_datetime(csv_data['transaction_date'], format='%d-%m-%Y')

# Group data by transaction date to understand daily sales trends
daily_sales = csv_data.groupby('transaction_date')['transaction_qty'].sum()

# Plotting daily sales trend
plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values)
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize product category distribution
product_category_distribution = csv_data['product_category'].value_counts()

plt.figure(figsize=(10, 6))
product_category_distribution.plot(kind='bar')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize sales across different store locations
store_sales = csv_data['store_location'].value_counts()

plt.figure(figsize=(10, 6))
store_sales.plot(kind='bar', color='skyblue')
plt.title('Sales by Store Location')
plt.xlabel('Store Location')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
