# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NPEcWbCRItZuxmUSi_BZIvbvklgz5IQk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers_df = pd.read_csv("https://raw.githubusercontent.com/Adri720S/Proyek-Analisis-Data/refs/heads/main/customers_dataset.csv")
orders_df = pd.read_csv("https://raw.githubusercontent.com/Adri720S/Proyek-Analisis-Data/refs/heads/main/orders_dataset.csv")
product_df = pd.read_csv("https://raw.githubusercontent.com/Adri720S/Proyek-Analisis-Data/refs/heads/main/products_dataset.csv")
product_categories_name_translation_df = pd.read_csv("https://raw.githubusercontent.com/Adri720S/Proyek-Analisis-Data/refs/heads/main/product_category_name_translation.csv")

data = {'customer_city': ['sao paulo', 'rio de janeiro', 'belo horizonte', 'brasilia', 'curitiba', 'bequimao', 'andarai'],
        'count': [15540, 6882, 2773, 2131, 1521, 1, 1]}

df = pd.DataFrame(data)

# Menampilkan hanya kota dengan jumlah tertinggi
top_cities = df.sort_values('count', ascending=False).head(10)

# Membuat bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_cities['customer_city'], top_cities['count'], color='brown')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.title('Top 10 Cities with Most Customers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

data = {
    'product_category_name_english': ['perfumery', 'art', 'sports_leisure', 'baby', 'housewares',
                                      'perfumery', 'art', 'sports_leisure', 'baby', 'housewares'],
    'product_weight_g': [225.0, 1000.0, 154.0, 371.0, 625.0, 200.0, 900.0, 150.0, 400.0, 650.0]
}

df = pd.DataFrame(data)

# Menghitung rata-rata berat per kategori
mean_weight_per_category = df.groupby('product_category_name_english')['product_weight_g'].mean()

# Membuat bar chart
plt.figure(figsize=(10, 6))
mean_weight_per_category.plot(kind='bar', color='purple')
plt.xlabel('Product Category')
plt.ylabel('Average Product Weight (g)')
plt.title('Average Product Weight per Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()