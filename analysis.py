"""
📊 FMCG Sales & Promotion Impact Analysis
----------------------------------------
A simulated data analysis project for portfolio demonstration.
Generates realistic FMCG sales data, analyzes performance, and visualizes insights.

📁 Key Outputs:
- fmcg_sales_data.csv       : Raw simulated sales data
- fmcg_dashboard_data.csv   : Cleaned data for BI tools
- monthly-sales.png         : Monthly revenue trend
- top-products.png          : Top 10 products by revenue
- fmcg_store_map.html       : Interactive store performance map
- insights.txt              : Business insights summary
- README.md                 : Project documentation

🛠️ How to Run:
1. Ensure required libraries are installed:
   pip install pandas matplotlib seaborn plotly

2. Run this script:
   python analysis.py

Note: This is a cleaned version of the original Colab script for portfolio clarity.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import date, timedelta
import random
import os

# Create output folder
os.makedirs("fmcg-sales-analysis", exist_ok=True)

# =================== DATA GENERATION ===================
print("🔧 Generating simulated FMCG sales data...")

# Date range
start_date = date(2024, 1, 1)
end_date = date(2024, 6, 30)
dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

# Products
products = [
    ("P1001", "Crunchy Chips", "Snacks", "MegaCrunch"),
    ("P1002", "Sparkling Water", "Beverages", "AquaFresh"),
    ("P1003", "Herbal Shampoo", "Personal Care", "NatureCare"),
    ("P1004", "Chocolate Bar", "Snacks", "SweetWave"),
    ("P1005", "Energy Drink", "Beverages", "PowerUp"),
    ("P1006", "Toilet Paper", "Personal Care", "SoftCare"),
    ("P1007", "Pretzels", "Snacks", "SaltyTwist"),
    ("P1008", "Iced Tea", "Beverages", "TeaZen"),
]

# Stores with GPS
stores_data = [
    ("S001", "MetroMart North", "North", 6.54321, 3.32109),
    ("S002", "CitySuper South", "South", 6.12345, 3.87654),
    ("S003", "QuickBuy East", "East", 6.78901, 4.12345),
    ("S004", "ValueHub West", "West", 6.23456, 2.98765),
    ("S005", "UrbanGrocer North", "North", 6.65432, 3.43210),
    ("S006", "PrimeCart South", "South", 6.09876, 3.76543),
    ("S007", "FastLane East", "East", 6.87654, 4.23456),
    ("S008", "DailyBasket West", "West", 6.34567, 3.09876),
    ("S009", "EliteMart North", "North", 6.43210, 3.21098),
    ("S010", "QuickStop South", "South", 6.21098, 3.98765),
    ("S011", "CityPantry East", "East", 6.76543, 4.01234),
    ("S012", "FreshHub West", "West", 6.12345, 2.87654),
    ("S013", "SuperSave North", "North", 6.56789, 3.54321),
    ("S014", "ValueCart South", "South", 6.32109, 3.65432),
    ("S015", "QuickPick East", "East", 6.65432, 4.34567),
    ("S016", "MetroValue West", "West", 6.45678, 3.12345),
    ("S017", "UrbanChoice North", "North", 6.78901, 3.67890),
    ("S018", "PrimePick South", "South", 6.45678, 3.54321),
    ("S019", "EastBay Market", "East", 6.98765, 4.45678),
    ("S020", "WestGate Store", "West", 6.01234, 2.76543),
]

# Generate data
data = []
for d in dates:
    for prod in products:
        for reg in ["North", "South", "East", "West"]:
            store_row = random.choice([s for s in stores_data if s[2] == reg])
            store_id, store_name, _, lat, lon = store_row
            units_sold = np.random.randint(30, 200)
            unit_price = round(np.random.uniform(1.0, 6.0), 2)
            promo = np.random.choice(["Yes", "No"], p=[0.3, 0.7])
            discount_pct = np.random.choice([10, 15, 20], p=[0.4, 0.3, 0.3]) if promo == "Yes" else 0
            revenue = units_sold * unit_price
            data.append([
                d, prod[0], prod[1], prod[2], prod[3],
                reg, store_id, store_name, lat, lon,
                units_sold, unit_price, promo, discount_pct, revenue
            ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "date", "product_id", "product_name", "category", "brand",
    "region", "store_id", "store_name", "store_latitude", "store_longitude",
    "units_sold", "unit_price", "promo", "discount_pct", "revenue"
])

# Save files
df.to_csv("fmcg-sales-analysis/fmcg_sales_data.csv", index=False)
df_export = df.copy()
df_export['date'] = df_export['date'].astype(str)
df_export.to_csv("fmcg-sales-analysis/fmcg_dashboard_data.csv", index=False)

print("✅ Data generation complete.")

# Note: Full analysis and visuals were generated in the original environment.
# This script is for documentation and reproducibility in your portfolio.