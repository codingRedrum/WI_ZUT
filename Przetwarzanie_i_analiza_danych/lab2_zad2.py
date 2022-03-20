from datetime import date
from operator import index
from tokenize import group
import pandas as pd
import numpy as np
import random

####################################################################################
# ADRIAN JUSZCZAK
####################################################################################


####################################################################################
# UCZYMY SIE
####################################################################################

# Zad. 1 ###########################################################################
df = pd.DataFrame()

# Zad. 2 ###########################################################################
lista = [['Ania', 24], ['Michal', 9], ['Darek', 40], ['Ewa', 43]]
df = pd.DataFrame(lista)
# print(df)
df.columns = ['Imie', 'Wiek']


# Zad.3 ###########################################################################
slownik = {'Imie': ['Ania', 'Michal', 'Darek', 'Ewa'], 'Wiek': [24, 9, 40, 43]}
df = pd.DataFrame(slownik)
print(slownik)


# Zad. 4 ###########################################################################
df = pd.DataFrame(np.random.randint(100, size=(10, 3)), columns=list('ABC'))
df.index.name = "id"
# print(df)
# Wyswietlic dane, które sa wieksze od 40 tylko dla kolumny B:
# print(df[df.B > 40].iloc[:, 1])
meanRows = np.mean(df, 0)
meanColumns = np.mean(df, 1)
# print(meanRows, meanColumns)
statystyka = df.describe()
# print(statystyka)


# Zad. 6 ###########################################################################
df1 = pd.DataFrame(np.random.randint(100, size=(5, 5)), columns=list('ABCDE'))
df2 = pd.DataFrame(np.random.randint(200, size=(5, 5)), columns=list('FGHIJ'))
concat1 = pd.concat([df1, df2], axis=0, ignore_index=True)
# print(concat1)
# w poziomie bez zmiany nazw kolumn
concat2 = pd.concat([df1, df2], axis=1, ignore_index=False)
# print(concat2)


# Zad. 7 ###########################################################################
df3 = pd.DataFrame(np.random.randint(100, size=(3, 3)), columns=list('ABC'))
df3.index.name = 'id'
df3.sort_values(by='id', ascending=False)
