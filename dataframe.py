import pandas as pd

df_data = pd.read_csv('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv')
df_data

#nomor 1
sampah_2021 = 0
for index,row in df_data.iterrows():
  if(row['tahun']==2021):
    sampah_2021 += row['jumlah_produksi_sampah']


df_datasampah2021 = pd.DataFrame({'tahun':'2021','jumlah sampah':[sampah_2021]})
df_datasampah2021.to_csv('Sampah2021.csv',index=False)

print(df_datasampah2021)

#nomor 2
sampah_pertahun = {}
for index,row in df_data.iterrows():
  tahun = row['tahun']
  jumlah = row['jumlah_produksi_sampah']
  if tahun in sampah_pertahun:
    sampah_pertahun[tahun] += jumlah
  else:
     sampah_pertahun[tahun] = 0

df_sampah = pd.DataFrame(sampah_pertahun.items(),columns=['tahun','total sampah'])
df_sampah.to_csv('toal sampah pertahun.csv',index=False)


print(df_sampah)

#nomor 3
kabupaten = {}

for index,row in df_data.iterrows():
  nama_kabupaten = row['nama_kabupaten_kota']
  tahun = row['tahun']

  if nama_kabupaten not in kabupaten:
    kabupaten[nama_kabupaten]={}
  if tahun not in kabupaten[nama_kabupaten]:
    kabupaten[nama_kabupaten][tahun] = 0
  
  kabupaten[nama_kabupaten][tahun] += row['jumlah_produksi_sampah']

df_totalSampah_kabupatem = pd.DataFrame(kabupaten)
df_totalSampah_kabupatem.to_csv('total sampah kabupaten.csv',index=False)

print(kabupaten)