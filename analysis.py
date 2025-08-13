import pandas as pd
import json

try:
    df = pd.read_csv('products_jumia.csv')
except FileNotFoundError:
    print("Error: 'products_jumia.csv' not found. Please ensure the file is in the same directory.")
    exit()

# Data Cleaning
df['curr_price'] = df['curr_price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float).astype(int)
df['discount'] = df['discount'].astype(str).str.replace('%', '', regex=False).astype(float)
df['rating'] = df['rating'].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

all_chart_data = {}

# Question 1: Lowest Average Product Price by Brand
avg_price_by_brand = df.groupby('brand')['curr_price'].mean().sort_values().reset_index()
avg_price_by_brand['avg_price'] = avg_price_by_brand['curr_price']
lowest_avg_price_data = avg_price_by_brand[['brand', 'avg_price']].to_dict('records')
all_chart_data['lowestAvgPriceByBrandData'] = lowest_avg_price_data

# Question 2: Overall Average Discount Percentage
overall_avg_discount = df['discount'].mean()
overall_avg_discount_data = [
    {'label': 'Average Discount', 'value': round(overall_avg_discount, 1), 'fill': 'var(--color-chart-1)'},
    {'label': 'Remaining Value', 'value': round(100 - overall_avg_discount, 1), 'fill': 'var(--color-chart-2)'},
]
all_chart_data['overallAvgDiscountData'] = overall_avg_discount_data

# Question 3: Highest Average Discount Percentage by Brand
avg_discount_by_brand = df.groupby('brand')['discount'].mean().sort_values(ascending=False).reset_index()
avg_discount_by_brand['avg_discount'] = avg_discount_by_brand['discount']
highest_avg_discount_data = avg_discount_by_brand[['brand', 'avg_discount']].to_dict('records')
all_chart_data['highestAvgDiscountByBrandData'] = highest_avg_discount_data

# Question 4: Product Rating vs Price
rating_vs_price_data = df[['curr_price', 'rating']].rename(columns={'curr_price': 'price', 'rating': 'rating'}).to_dict('records')
all_chart_data['ratingVsPriceData'] = rating_vs_price_data

# Question 5: Average Rating by Brand
avg_rating_by_brand = df.groupby('brand')['rating'].mean().sort_values(ascending=False).reset_index()
avg_rating_by_brand['avg_rating'] = avg_rating_by_brand['rating']
avg_rating_by_brand_data = avg_rating_by_brand[['brand', 'avg_rating']].to_dict('records')
all_chart_data['avgRatingByBrandData'] = avg_rating_by_brand_data

# Write all data to a single JSON file
with open('chartData.json', 'w') as f:
    json.dump(all_chart_data, f, indent=2)

print("Successfully generated chartData.json with all the analysis data.")