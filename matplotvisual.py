import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('products_jumia.csv')
except FileNotFoundError:
    print("Error: 'products_jumia.csv' not found. Please ensure the file is in the same directory.")
    exit()

print("Question 1: Which brand has the lowest average product price?")

df['curr_price'] = df['curr_price'].astype(str).str.replace(r'[^\d.]', '', regex=True).astype(float).astype(int)

avg_price_by_brand = df.groupby('brand')['curr_price'].mean().sort_values()

lowest_avg_price_brand = avg_price_by_brand.idxmin()
lowest_avg_price = avg_price_by_brand.min()

print(f"The brand with the lowest average price is '{lowest_avg_price_brand}' with an average price of KES {lowest_avg_price:.2f}.")
print("-" * 50)

plt.figure(figsize=(12, 6))
avg_price_by_brand.plot(kind='bar', color='skyblue')
plt.title('Average Product Price by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Price (KES)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("Question 2: What is the average discount percentage across all products in the dataset?")

df['discount'] = df['discount'].astype(str).str.replace('%', '', regex=False).astype(float)

overall_avg_discount = df['discount'].mean()

print(f"The average discount percentage across all products is: {overall_avg_discount:.2f}%")
print("-" * 50)

labels = ['Average Discount', 'Remaining Value']
sizes = [overall_avg_discount, 100 - overall_avg_discount]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Overall Average Discount Percentage')
plt.axis('equal')
plt.show()

print("Question 3: Which brands have the highest average discount percentage?")

avg_discount_by_brand = df.groupby('brand')['discount'].mean().sort_values(ascending=False)

highest_avg_discount_brand = avg_discount_by_brand.idxmax()
highest_avg_discount = avg_discount_by_brand.max()

print(f"The brand with the highest average discount percentage is '{highest_avg_discount_brand}' with an average discount of {highest_avg_discount:.2f}%.")
print("-" * 50)

plt.figure(figsize=(12, 6))
avg_discount_by_brand.plot(kind='bar', color='salmon')
plt.title('Average Discount Percentage by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Discount (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("Question 4: Is the rating worth the price?")

df['rating'] = df['rating'].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

plt.figure(figsize=(12, 8))
plt.scatter(df['curr_price'], df['rating'], alpha=0.7, color='green')
plt.title('Product Rating vs. Price')
plt.xlabel('Current Price (KES)')
plt.ylabel('Product Rating')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Question 5: What is the reliability of each brand based on the average rating?")

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

avg_rating_by_brand = df.groupby('brand')['rating'].mean().sort_values(ascending=False)

highest_avg_rating_brand = avg_rating_by_brand.idxmax()
highest_avg_rating = avg_rating_by_brand.max()

print(f"The brand with the highest average rating is '{highest_avg_rating_brand}' with an average rating of {highest_avg_rating:.2f}.")
print("-" * 50)

plt.figure(figsize=(12, 6))
avg_rating_by_brand.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
