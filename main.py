# Project: Sales Visual Analytics Dashboard

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.makedirs("output", exist_ok=True)

# Set Theme
sns.set_theme(style="whitegrid")

# Create Dataset
data = {
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Apr", "Apr", "May", "May", "Jun", "Jun"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop"],
    "City": ["Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur"],
    "Revenue": [50000, 30000, 55000, 32000, 22000, 52000, 40000, 25000, 62000, 45000, 30000, 65000],
    "Orders": [10, 15, 11, 16, 8, 10, 20, 9, 12, 22, 11, 13],
    "Marketing": [5000, 3000, 6000, 3200, 2500, 5500, 4200, 2600, 7000, 5000, 3500, 7200],
    "Discount": [5, 10, 5, 8, 7, 6, 10, 5, 4, 8, 5, 3]
}

# Add More Sample Data
data["Month"].extend(["Jul", "Jul", "Aug", "Aug", "Sep", "Sep", "Oct", "Oct", "Nov", "Nov", "Dec", "Dec", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"])
data["Product"].extend(["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Mobile", "Tablet", "Laptop", "Mobile", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Laptop", "Tablet", "Mobile"])
data["City"].extend(["Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Kasur", "Lahore", "Kasur", "Lahore", "Kasur", "Lahore"])
data["Revenue"].extend([58000, 42000, 28000, 68000, 48000, 35000, 72000, 50000, 38000, 78000, 55000, 42000, 46000, 32000, 60000, 52000, 75000, 58000, 33000, 59000, 47000, 63000, 36000, 54000])
data["Orders"].extend([14, 21, 10, 15, 23, 12, 16, 25, 13, 18, 27, 15, 22, 11, 13, 24, 17, 28, 12, 12, 23, 14, 13, 26])
data["Marketing"].extend([6200, 4700, 3000, 7500, 5200, 3800, 8000, 5500, 4200, 8500, 6000, 4800, 5000, 3400, 6500, 5700, 8200, 6300, 3600, 6400, 5100, 6800, 3900, 5900])
data["Discount"].extend([5, 7, 6, 4, 9, 5, 3, 8, 6, 4, 10, 5,8, 7, 5, 6, 3, 9, 5, 4, 8, 6, 7, 5])

df = pd.DataFrame(data)

# Display Dataset Information
print("Sales Dataset:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nTotal Records:", len(df))

# Calculate Monthly Revenue

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

monthly_revenue = df.groupby("Month")["Revenue"].sum()
monthly_revenue = monthly_revenue.reindex(month_order).reset_index()

print("\nMonthly Revenue:")
print(monthly_revenue)

# Calculate Product Revenue

product_revenue = df.groupby("Product")["Revenue"].sum().reset_index()

print("\nProduct Revenue:")
print(product_revenue)

# Calculate City Revenue

city_revenue = df.groupby("City")["Revenue"].sum().reset_index()

print("\nCity Revenue:")
print(city_revenue)

# Calculate Product Orders

product_orders = df.groupby("Product")["Orders"].sum().reset_index()

print("\nProduct Orders:")
print(product_orders)

# Calculate Total Revenue

total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Calculate Total Orders

total_orders = df["Orders"].sum()
print("Total Orders:", total_orders)

# Calculate Average Revenue

average_revenue = df["Revenue"].mean()
print(f"Average Revenue: {average_revenue:.2f}")

# Calculate Revenue Per Order

revenue_per_order = total_revenue / total_orders
print(f"Revenue Per Order: {revenue_per_order:.2f}")

# Find Best Performing Month

best_month = monthly_revenue.loc[monthly_revenue["Revenue"].idxmax(), "Month"]
best_month_revenue = monthly_revenue["Revenue"].max()

# Find Best Performing Product

best_product = product_revenue.loc[product_revenue["Revenue"].idxmax(), "Product"]
best_product_revenue = product_revenue["Revenue"].max()

# Find Best Performing City

best_city = city_revenue.loc[city_revenue["Revenue"].idxmax(), "City"]
best_city_revenue = city_revenue["Revenue"].max()

# Create Dashboard

fig, axes = plt.subplots(4, 2, figsize=(12, 14))

# Display Sales Summary

fig.suptitle("Sales Visual Analytics Dashboard", fontweight="bold", fontsize=16, y=1.0)

# Total Revenue Card

fig.text(
    0.18, 0.94,
    f"TOTAL REVENUE\n{total_revenue:,.0f}",
    ha="center", va="center",
    fontweight="bold",
    color="white",
    bbox=dict(boxstyle="round,pad=1", facecolor="#2874A6")
)

# Total Orders Card

fig.text(
    0.50, 0.94,
    f"TOTAL ORDERS\n{total_orders}",
    ha="center", va="center",
    fontweight="bold",
    color="white",
    bbox=dict(boxstyle="round,pad=1", facecolor="#239B56")
)

# Revenue Per Order Card

fig.text(
    0.82, 0.94,
    f"REVENUE PER ORDER\n{revenue_per_order:,.2f}",
    ha="center", va="center",
    fontweight="bold",
    color="white",
    bbox=dict(boxstyle="round,pad=1", facecolor="#884EA0")
)
# Chart 1: Monthly Revenue

sns.lineplot(
    data=monthly_revenue,
    x="Month",
    y="Revenue",
    marker="o",
    errorbar=None,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Monthly Revenue Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue")

# Chart 2: Product Revenue

sns.barplot(
    data=product_revenue,
    x="Product",
    y="Revenue",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Product Revenue Comparison")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Revenue")

# Chart 3: Revenue Distribution

sns.histplot(
    data=df,
    x="Revenue",
    bins=8,
    kde=True,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Revenue Distribution")
axes[1, 0].set_xlabel("Revenue")
axes[1, 0].set_ylabel("Frequency")

# Chart 4: Marketing vs Revenue

sns.scatterplot(
    data=df,
    x="Marketing",
    y="Revenue",
    hue="City",
    s=100,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Marketing vs Revenue")
axes[1, 1].set_xlabel("Marketing Expense")
axes[1, 1].set_ylabel("Revenue")

# Chart 5: Orders vs Revenue

sns.scatterplot(
    data=df,
    x="Orders",
    y="Revenue",
    hue="Product",
    s=100,
    ax=axes[2, 0]
)
axes[2, 0].set_title("Orders vs Revenue")
axes[2, 0].set_xlabel("Orders")
axes[2, 0].set_ylabel("Revenue")

# Chart 6: City Revenue

sns.barplot(
    data=city_revenue,
    x="City",
    y="Revenue",
    ax=axes[2, 1]
)
axes[2, 1].set_title("City-wise Revenue")
axes[2, 1].set_xlabel("City")
axes[2, 1].set_ylabel("Revenue")

# Chart 7: Product Orders

sns.barplot(
    data=product_orders,
    x="Product",
    y="Orders",
    ax=axes[3, 0]
)
axes[3, 0].set_title("Product-wise Orders")
axes[3, 0].set_xlabel("Product")
axes[3, 0].set_ylabel("Total Orders")

# Chart 8: Discount vs Revenue

sns.scatterplot(
    data=df,
    x="Discount",
    y="Revenue",
    hue="Product",
    s=100,
    ax=axes[3, 1]
)
axes[3, 1].set_title("Discount vs Revenue")
axes[3, 1].set_xlabel("Discount (%)")
axes[3, 1].set_ylabel("Revenue")

# Adjust Dashboard
plt.tight_layout(rect=[0, 0, 1, 0.88])

# Save Dashboard
plt.savefig(
    "output/sales_dashboard.png",
    bbox_inches="tight"
)
plt.show()

# Correlation Heatmap
correlation = df[["Revenue", "Orders", "Marketing", "Discount"]].corr()

plt.figure(figsize=(9, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Sales Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    "output/correlation_heatmap.png",
    bbox_inches="tight"
)

plt.show()

# Display Business Insights

print("\n========== BUSINESS INSIGHTS ==========")

print(f"Best Performing Month: {best_month}")
print(f"Best Month Revenue: {best_month_revenue:,.0f}")

print(f"\nBest Performing Product: {best_product}")
print(f"Best Product Revenue: {best_product_revenue:,.0f}")

print(f"\nBest Performing City: {best_city}")
print(f"Best City Revenue: {best_city_revenue:,.0f}")

print(f"\nTotal Revenue: {total_revenue:,.0f}")
print(f"Total Orders: {total_orders}")
print(f"Revenue Per Order: {revenue_per_order:,.2f}")

print("\n========== PROJECT COMPLETED ==========")
print("Sales Dashboard Saved Successfully!")
print("Correlation Heatmap Saved Successfully!")
