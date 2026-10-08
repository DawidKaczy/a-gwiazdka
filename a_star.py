import math
import heapq
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

SCIEZKA_MAPY = Path(__file__).with_name("grid.txt")
START = (0, 0)
CEL = (19, 19)
PRZESZKODA = 5


def wczytaj_mape(sciezka):
    with open(sciezka, "r") as plik:
        mapa = [list(map(int, linia.strip().split())) for linia in plik]
    mapa.reverse()
    return np.array(mapa)


def oblicz_heurystyke(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def znajdz_sasiadow(x, y, mapa):
    sasiedzi = []
    if x + 1 < mapa.shape[0]:
        sasiedzi.append((x + 1, y))
    if y - 1 >= 0:
        sasiedzi.append((x, y - 1))
    if x - 1 >= 0:
        sasiedzi.append((x - 1, y))
    if y + 1 < mapa.shape[1]:
        sasiedzi.append((x, y + 1))
    return sasiedzi


def a_gwiazdka(mapa, start_x, start_y, cel_x, cel_y):
    start = (start_y, start_x)
    cel = (cel_y, cel_x)

    lista_otwarta = []
    heapq.heappush(lista_otwarta, (1 + oblicz_heurystyke(start[0], start[1], cel[0], cel[1]), start))

    koszty_g = {start: 0}
    sciezka_powrotna = {start: None}
    lista_zamknieta = set()
    odwiedzone_z_kosztami = {}

    while lista_otwarta:
        _, obecny = heapq.heappop(lista_otwarta)
        obecny_x, obecny_y = obecny

        if obecny == cel:
            sciezka = []
            while obecny in sciezka_powrotna:
                sciezka.append(obecny)
                obecny = sciezka_powrotna[obecny]
            return sciezka, odwiedzone_z_kosztami

        lista_zamknieta.add(obecny)

        for sasiad in znajdz_sasiadow(obecny_x, obecny_y, mapa):
            if sasiad in lista_zamknieta or mapa[sasiad] == PRZESZKODA:
                continue

            tymczasowy_g = koszty_g[obecny] + 1

            if sasiad not in koszty_g or tymczasowy_g < koszty_g[sasiad]:
                koszty_g[sasiad] = tymczasowy_g
                koszt_f = tymczasowy_g + oblicz_heurystyke(sasiad[0], sasiad[1], cel[0], cel[1])
                heapq.heappush(lista_otwarta, (koszt_f, sasiad))
                sciezka_powrotna[sasiad] = obecny
                odwiedzone_z_kosztami[sasiad] = koszt_f

    return None, odwiedzone_z_kosztami


def wizualizacja(mapa, sciezka=None, odwiedzone_z_kosztami=None):
    wysokosc, szerokosc = mapa.shape

    plt.figure(figsize=(12, 12))
    plt.xticks(range(szerokosc))
    plt.yticks(range(wysokosc))

    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.5))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.5))
    plt.grid(True, which="minor")

    plt.imshow(mapa, cmap="Greys", origin="lower")

    if odwiedzone_z_kosztami:
        for (x, y), koszt in odwiedzone_z_kosztami.items():
            plt.text(y, x, f"{koszt:.2f}", ha="center", color="blue", fontsize=8)

    if sciezka:
        sciezka_x, sciezka_y = zip(*sciezka)
        plt.plot(sciezka_y, sciezka_x, linewidth=2, label="Ścieżka")

    plt.scatter(START[0], START[1], color="green", label="Start")
    plt.scatter(CEL[0], CEL[1], color="red", label="Cel")

    plt.legend()
    plt.title("Wizualizacja algorytmu A*")
    plt.show()


def main():
    mapa = wczytaj_mape(SCIEZKA_MAPY)
    sciezka, odwiedzone_z_kosztami = a_gwiazdka(mapa, START[0], START[1], CEL[0], CEL[1])

    if sciezka:
        print("Znaleziono ścieżkę.")
        wizualizacja(mapa, sciezka, odwiedzone_z_kosztami)
    else:
        print("Nie znaleziono ścieżki.")
        wizualizacja(mapa, odwiedzone_z_kosztami=odwiedzone_z_kosztami)


if __name__ == "__main__":
    main()
