import pandas as pd

# Contoh Pandas Series
data_series = pd.Series([10, 20, 30, 40])
print(data_series)

# Contoh Pandas DataFrame
data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Umur': [25, 30, 35],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}

df = pd.DataFrame(data)
print(df)

# Menambahkan kolom baru
df['Pendapatan'] = [5000, 6000, 7000]
print(df)

# Menhapus baris atau Kolom
df = df.drop('Pendapatan', axis=1)  # Menghapus kolom
df = df.drop(1, axis=0)  # Menghapus baris ke-2
print(df)

# Operasi Statistik
print(df['Umur'].mean())  # Rata-rata
print(df['Umur'].sum())   # Total
print(df['Umur'].max())   # Nilai maksimum
print(df['Umur'].min())   # Nilai minimum


