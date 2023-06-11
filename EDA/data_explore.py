# permasalahan yang coba di kembangkan melalui data exploratory
# 1. pada data mid-career salary jurusan mana yang memiliki nilai terendah dan tertinggi
# 2. jurusan mana yang memiliki gasi awal terendah ketika undergraduate dan berapa mereka dapat setelah graduate
# 3. jurusan mana yang memiliki gaji mid-career-salary terendah dan berapa ekspektasi masyarakat tentang gaji di jurusan tersebut

# data bersumber dari "data_biaya.csv" yang diambil dari kaggle
__author__ = "adrianrufy"


import pandas as pd

# membaca data csv
data = pd.read_csv("data_biaya.csv")

# melihat label pada data 
print(data.columns)

# menghilangkan nilai yang hilang pada data
pemisahan = data.dropna()
pemisahan.isna()

# ------------------------------------------------------------------------------------------------------

# solusi soal pertama 

# melihat index gaji tertinggi pada data data_biaya,csv
highest_Salarymedian = pemisahan["Mid-Career Median Salary"].idxmax()

# memisahkan seluruh label yang berkaitan dengan gaji tertinggi pada mid-career salary dengan method .loc
data_tertinggi_MedSalary = pemisahan.loc[highest_Salarymedian]
# melihat keseluruhan data mengenai gaji tertinggi pada mid-career salary
print(data_tertinggi_MedSalary)

# melakukan story telling atas pengetahuan dari ekplorasi data sederhana mengenai gaji tertinggi dan jurusan pada label "Mid-Career Salary"
print(f" jurusan dengan hasil tertinggi terdapat pada {data_tertinggi_MedSalary.loc['Undergraduate Major']} dengan pendapatan ${data_tertinggi_MedSalary.loc['Mid-Career Median Salary']} dengan minimal 10 tahun pengalaman")


# -------------------------------------------------------------------------------------------------------

lowest_Startingsalary = pemisahan["Starting Median Salary"].idxmin()

data_terendah_startsalary = pemisahan.loc[lowest_Startingsalary]

print(data_terendah_startsalary)

print(f"jurusan dengan starting median salary terendah adalah {data_terendah_startsalary['Undergraduate Major']}, dengan nominal gaji adalah $ {data_terendah_startsalary['Starting Median Salary']}")


# -------------------------------------------------------------------------------------------------------

# untuk mengetahui kepastian dari berapa gaji yang nanti akan diterima
# dilakukan perngurangan posisi data persentil ke 10 dengan persentil ke 90

# manual
LowRiskMajor = pemisahan["Mid-Career 90th Percentile Salary"] - pemisahan["Mid-Career 10th Percentile Salary"]

# method 
lowriskmajor = pemisahan["Mid-Career 90th Percentile Salary"].subtract(pemisahan["Mid-Career 10th Percentile Salary"])
print(lowriskmajor)


pemisahan.insert(5, 'risk', LowRiskMajor)

print(pemisahan.head())

highest_potential = pemisahan.sort_values(["Mid-Career 90th Percentile Salary","risk"],ascending = True)

print(highest_potential[["Undergraduate Major","Mid-Career 90th Percentile Salary","risk"]].head())


# ----------------------------------------------------------------------------------------------------------

# melakukan pengelompokan data dengan pandas 

print(pemisahan.groupby('Undergraduate Major').count())