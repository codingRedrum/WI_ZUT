
import numpy as np
import matplotlib.pyplot as plt

###################################################
# 2. Dyskretyzacja
###################################################

# dyskretyzacja inaczej probkowanie
# kwantyzacja - nadanie wartosci ze zbioru
# przygotowac dunkche generujaca zdyskretyzowany sygnal
# sinus na podstawie parametrow


# Chcemy wytworzyć sygnał sinusoidalny o częstotliwości
# f np. 200 Hz, przy założonej częstotliwości próbkowania
#  fs 48 kHz.
#  Okres sygnału wynosi  T=1/fs
# . W ciągu sekundy mamy  fs próbek sygnału.
# Stąd wynika, że liczba próbek  N przypadająca na jeden okres sygnału wynosi: fs/f

# Zad. 1
# generic function
def generateDiscretedSignal(f, fs):
    t = np.arange(0, 1, 1/fs)
    sigVal = []
    for i in t:
        sigVal.append(np.sin(2 * np.pi * f * i))
    return t, sigVal


def calculateMultipleFs(f, arrayFs):
    result = []
    for i in range(len(arrayFs)):
        tab1, tab2 = generateDiscretedSignal(f, arrayFs[i])
        result.append(tab1)
        result.append(tab2)
    return result


def drawAllDiagrams(dataToDraw):
    fig, axs = plt.subplots(5, 2)
    idx = 0
    for i in range(5):
        idx = idx + 2
        j = 1
        for j in range(2):
            axs[i, j].plot(dataToDraw[idx-2], dataToDraw[idx-1])
            print(i, j)
    plt.show()


arrayFs = [20, 21, 30, 45, 50, 100, 150, 200, 250, 1000]
wynik = calculateMultipleFs(10, arrayFs)
drawAllDiagrams(wynik)
