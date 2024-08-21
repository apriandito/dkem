import pandas as pd

# Membaca data yang sudah dipreproses
df = pd.read_csv('data/preprocessed_dummy.csv')

# Feature Engineering: Membuat fitur baru
# 1. Economic Pressure: Kombinasi dari Unemployment Rate dan Inflation Rate (Stagflasi)
df['Economic_Pressure'] = df['Unemployment_Rate'] * df['Inflation_Rate']

# 2. Real Interest Rate: Menyesuaikan suku bunga nominal dengan inflasi
df['Real_Interest_Rate'] = df['Interest_Rate'] - df['Inflation_Rate']

# 3. Year and Month: Ekstraksi tahun dan bulan dari kolom Date untuk analisis musiman
df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month

# Menampilkan data setelah feature engineering
print("Data Setelah Feature Engineering:")
print(df.head())

from sklearn.feature_selection import SelectKBest, f_regression

# Memisahkan fitur dan target
X = df.drop(columns=['Date', 'Year', 'GDP_Growth_Rate'])  # Menghapus kolom target dan kolom yang tidak diperlukan
y = df['GDP_Growth_Rate']  # Target yang akan diprediksi

# Menggunakan SelectKBest untuk memilih fitur terbaik
selector = SelectKBest(score_func=f_regression, k=5)  # Memilih 5 fitur terbaik
X_new = selector.fit_transform(X, y)

# Mendapatkan fitur yang dipilih
selected_features = X.columns[selector.get_support()]

# Menampilkan fitur yang dipilih
print("\nFitur Terpilih:")
print(selected_features)
