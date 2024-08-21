import pandas as pd 

df = pd.read_csv('data/dummy.csv')

print(df)

# Cek Missing Values
print("\nJumlah Missing Values sebelum diisi:")
print(df.isna().sum())

# Menangani Missing Values
# Mengisi nilai yang hilang dengan metode forward fill untuk mengisi nilai berdasarkan data sebelumnya
df.fillna(method='ffill', inplace=True)

# Jika ada nilai yang masih NaN setelah forward fill, kita bisa menggunakan backward fill
df.fillna(method='bfill', inplace=True)

# Cek Missing Values
print("\nJumlah Missing Values setelah diisi:")
print(df.isna().sum())

# Skala data jika diperlukan (misalnya normalisasi data untuk model)
from sklearn.preprocessing import MinMaxScaler

# Normalisasi data numerik kecuali kolom 'Date'
scaler = MinMaxScaler()
df[df.columns[1:]] = scaler.fit_transform(df[df.columns[1:]])

# Menampilkan data setelah preprocessing
print("\nData Setelah Preprocessing:")
print(df.head())

# Menyimpan data yang sudah dipreproses jika diperlukan
df.to_csv('data/preprocessed_dummy.csv', index=False)