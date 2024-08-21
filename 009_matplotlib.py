import matplotlib.pyplot as plt

# Data Dummy
bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
nilai_tukar_usd_idr = [14000, 14100, 14250, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100]
tingkat_inflasi = [2.5, 2.7, 2.8, 3.0, 3.1, 3.2, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5]

# Membuat Figure dan Axes
fig, ax1 = plt.subplots()

# Plot Nilai Tukar Mata Uang (USD to IDR)
color = 'tab:blue'
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Nilai Tukar USD ke IDR', color=color)
ax1.plot(bulan, nilai_tukar_usd_idr, color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

# Membuat Axes kedua untuk Tingkat Inflasi
ax2 = ax1.twinx()  # Memungkinkan dua skala y dalam grafik yang sama
color = 'tab:red'
ax2.set_ylabel('Tingkat Inflasi (%)', color=color)
ax2.plot(bulan, tingkat_inflasi, color=color, marker='x')
ax2.tick_params(axis='y', labelcolor=color)

# Menambahkan Judul
plt.title('Nilai Tukar USD ke IDR dan Tingkat Inflasi (Januari - Desember)')

# Menampilkan Grafik
plt.show()
