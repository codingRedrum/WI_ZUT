from datetime import date
from operator import index
from tokenize import group
import pandas as pd
import numpy as np
import random

####################################################################################
# ADRIAN JUSZCZAK
####################################################################################

######################################################################
# 3. ZADANIA
######################################################################

# Zad. 1
slownik = {'Day': ['Mon', 'Tue', 'Mon', 'Tue', 'Mon'],
           'Fruit': ['Apple', 'Apple', 'Banana', 'Banana', 'Apple'],
           'Pound': [10, 15, 50, 40, 5],
           'Profit': [20, 30, 25, 20, 10]
           }
df3 = pd.DataFrame(slownik)
print(df3)
print(df3.groupby('Day').sum())
print(df3.groupby(['Day', 'Fruit']).sum())


# Zad. 2 ###########################################################################
df = pd.DataFrame(np.random.randn(20, 3),
                  index=np.arange(20), columns=list('ABC'))
df.index.name = 'id'
print("################################################## \n")
print("# Zadania 3. \n")

df['B'] = 1
print("df['B'] = 1 \n \
Przypisanie wartosci 1 do kazdego wiersza w kolumnie nr 1 \n")

df.iloc[1, 2] = 10
print("df.iloc[1, 2] = 10 \n \
W wierszu 1, kolumnie 2 przypisana zostaje wartosc = 10 \n")

df[df < 0] = -df
print("df[df < 0] = -df \n \
Jezeli, ktoras z wartosci w macierzy df jest ponizej zera \n \
w to miejsce przypisana zostaje liczba przeciwna np. gdy -1.55 = 1.55 \n")

df.iloc[[0, 3], 1] = np.nan
print("df.iloc[[0, 3], 1] = np.nan \n \
W wierszu 0 i 3, kolumnie 1 przypisana zostaje wartosc 1\n")

df.fillna(0, inplace=True)
print("df.fillna(0, inplace=True) \n \
W miejscu gdzie znaleziono wartosc 0, zamineia ja na wartosc 0\n")

df.iloc[[0, 3], 1] = np.nan
df = df.replace(to_replace=np.nan, value=9999)
print("df = df.replace(to_replace = np.nan, value = 9999) \n \
Zamienia wartosci NAN na wartosc 9999\n")

df.iloc[[0, 3], 1] = np.nan
print("pd.isnull(df) \n \
Porowuje kazda wartosc macierzy do 0\n")


# Zad. 3 ###########################################################################
df = pd.DataFrame({'x': [1, 2, 3, 4, 5],
                   "y": ['a', 'b', 'a', 'b', 'b']})

sumX = df.iloc[:, 0].sum()
groupedByY = df.groupby('y').sum()

licznosc = df['y'].value_counts().describe()
print(licznosc)

# Zad. 4 ###########################################################################
df = pd.DataFrame(np.random.randn(4, 2), columns=list('AB'))
dti = pd.date_range("2022-03-10", periods=4, freq="D")
df.index = pd.to_datetime(dti)
print(df)

# Zad. 5 ###########################################################################

# auta = np.loadtxt('autos.csv', dtype='str', delimiter=',')
# auta1 = pd.read_csv('autos.csv')
# print(auta, "\n")
# print(auta1, "\n")
