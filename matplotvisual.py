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

print("The provided chart reveals a tiered market where brands compete on different fronts. The lowest-priced brands like rashnik and mika dominate the entry-level segment by offering affordability, while the mid-range brands such as ramtons and haier are locked in tight competition for the value-conscious customer. At the highest end, premium brands like midea and the outlier ecomax compete on perceived quality and brand status rather than price, with ecomax potentially targeting a luxury niche.")
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

print('The Overall Average Discount Percentage pie chart shows that, on average, products in the dataset are discounted by 27.1%. This means that roughly a quarter of the total product value is being discounted at the time of the scrape. The large Remaining Value slice of 72.9% simply represents the portion of the price that is not being discounted, providing context for the discounts magnitude. This analysis confirms that discounts are a significant factor across the marketplace, but the majority of the product value remains undiscounted.')
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

print("Based on the 'Average Discount Percentage by Brand' chart, there is a clear inverse relationship between a brand's average price and its average discount. Brands in the entry-level price tier, like aillyons, em, and von, offer the highest average discounts, all over 40%, indicating a strategy focused on attracting customers with aggressive promotions. Conversely, the more expensive brands like rashnik and ecomax, which were at the higher end of the price chart, offer the lowest average discounts, at around 15%. This suggests that these premium brands rely on their brand value rather than price promotions to drive sales.")
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

print("The scatter plot shows no strong correlation between product rating and price. Most products, regardless of their cost, are highly rated between 4.0 and 5.0 stars. This suggests that price isn't a primary indicator of customer satisfaction on this marketplace. There are a few outliers, including a product with a low rating at a high price, indicating a potential mismatch between a product's cost and its perceived value.")
print("-" * 50)

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

print("Based on the 'Average Rating by Brand' chart, there is a very high level of customer satisfaction across most of the brands. The majority of brands, including the highest-rated brand maxmo, fall within a tight average rating band of 4.3 to 4.8 stars. This suggests that the marketplace is populated with reliable products, and that the differences in average ratings are minor. The brands with lower average ratings, such as roch, vision, and aillyons, may have a small number of poorly rated products, which slightly pulls down their overall average, but they are still generally well-regarded with ratings above 3.0.")
print("-" * 50)

plt.figure(figsize=(12, 6))
avg_rating_by_brand.plot(kind='bar', color='lightgreen')
plt.title('Average Rating by Brand')
plt.xlabel('Brand')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
