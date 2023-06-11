__author__ = "Adrian Des Zuchrufy"
__data_source__ = "Kaggle"
# library untuk mengelola data 
import pandas as pd

# membaca data csv menggunakan pandas
data = pd.read_csv("data_biaya.csv")

# memunculkan 5 data dari atas 

print(data.head())

# melakukan analisa pre-processing
# # mencari informasi tentang 
# 1. berapa banyak baris yang dimiliki dataframe
# 2. berapa banyak kolom yang dimiliki dataframe
# 3. labels apa yang dimiliki dataframe
# 4. apakah ada kolom yang hilang pada dataframe

# pertanyaan pertama dan kedua dapat dijawab dengan
print(data.shape)
# dengan bentuk tuple (x,y) : x = baris, y = kolom 


# pertanyaan ke 3 dapat dijawab dengan

print(data.columns)  

# pertanyaan ke 4 dapat dijawab dengan 

print(data.isna)
# dimana isna artinya Not A number

# dari hasil mencari nilai kosong (missing values) terdapat nilai kosong yaitu di baris ke 50 pada kolom "Starting Median Salary"
# maka kita akan melakukan drop atau pengeluaran data yang hilang dengan

# print(data.dropna().tail) 
# atau kita membuat sebuah pewarisan objek yang nantinya berguna untuk digunakan secara terus menerus
data_clean = data.dropna()
data_clean.tail()



# untuk mengakses beberapa atau sebagian data
# dengan memanggil object data_clean kita dapat melakukan parameter slicing dengan

median_biaya = data_clean["Starting Median Salary"]


# dari data median_biaya kita dapat menganalisa nilai maximum dari data dengan cara

# iterative
maximum = 0
for i in median_biaya:
    if maximum < i:
        maximum = i

print(maximum)

# method call 

print(median_biaya.max())

# untuk mengetahui nilai terendah kita harus mempunyai ambang batas yaitu nilai tertinggi

# iterative
minimum = maximum
for i in median_biaya:
    if minimum > i:
        minimum = i
print(minimum)

# method call

print(median_biaya.min())


# untuk mengetahui index data pada data tertinggi dapat menggunakan method .idxmax()

print(median_biaya.idxmax())

# untuk mengetahui index data pada data terendah dapat menggunakan method .idxmin()

print(median_biaya.idxmin())

# untuk memisahkan data berdasarkan index menggunakan method .loc[int] yang berguna untuk menslicing data dengan integer

print(data_clean["Starting Median Salary"].loc[43])

# untuk memisahkan data dengan seluruh atribut pada data tersebut sesuai dengan indexnya menggunakan 

print(data_clean.loc[43])






