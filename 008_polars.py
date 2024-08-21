import polars as pl

data_series = pl.Series([10, 20, 30, 40])
print(data_series)

data = {
    'Nama': ['Alice', 'Bob', 'Charlie'],
    'Umur': [25, 30, 35],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}
df = pl.DataFrame(data)
print(df)

df = df.with_columns([
    pl.Series("Pendapatan", [5000, 6000, 7000])
])
print(df)

df = df.drop('Pendapatan')  # Menghapus kolom
df = df.filter(pl.col("Nama") != "Bob") # Memfilter baris
print(df)

