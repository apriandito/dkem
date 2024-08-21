import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Data Dummy
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'],
    'Nilai Tukar USD ke IDR': [14000, 14100, 14250, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100],
    'Tingkat Inflasi (%)': [2.5, 2.7, 2.8, 3.0, 3.1, 3.2, 3.0, 2.9, 2.8, 2.7, 2.6, 2.5]
}

# Konversi Data ke DataFrame
df = pd.DataFrame(data)

# Membuat Grafik Nilai Tukar USD ke IDR
fig = px.line(df, x='Bulan', y='Nilai Tukar USD ke IDR', labels={'Bulan': 'Bulan', 'Nilai Tukar USD ke IDR': 'Nilai Tukar USD ke IDR'}, title='Nilai Tukar USD ke IDR dan Tingkat Inflasi (Januari - Desember)')
fig.update_traces(name='Nilai Tukar USD ke IDR', mode='lines+markers', line=dict(color='blue'))

# Menambahkan Grafik Tingkat Inflasi
fig.add_trace(go.Scatter(x=df['Bulan'], y=df['Tingkat Inflasi (%)'], mode='lines+markers', name='Tingkat Inflasi (%)', yaxis='y2', line=dict(color='red')))

# Mengatur Axis Kedua untuk Tingkat Inflasi
fig.update_layout(
    yaxis=dict(title='Nilai Tukar USD ke IDR', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
    yaxis2=dict(title='Tingkat Inflasi (%)', titlefont=dict(color='red'), tickfont=dict(color='red'), anchor='x', overlaying='y', side='right'),
    legend=dict(x=0.5, y=1.2, orientation="h"),
)

# Menampilkan Grafik
fig.show()
