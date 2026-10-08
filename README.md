# A* — wyszukiwanie ścieżki na siatce

Implementacja algorytmu A* na mapie 20×20. Program wczytuje siatkę z pliku, omija przeszkody i rysuje znalezioną ścieżkę razem z kosztem `f` odwiedzonych pól.

## Wymagania

- Python 3.12
- Windows, jeśli chcesz użyć `map_generator.exe`

## Uruchomienie

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python a_star.py
```

Start to pole `(0, 0)`, cel to `(19, 19)`.

## Mapa

Plik `grid.txt` zawiera 20 wierszy po 20 liczb:

- `0` — pole wolne
- `5` — przeszkoda

`tools/map_generator.exe` generuje nową mapę (program na Windows).

## Struktura

```
a_star.py              algorytm i wizualizacja
grid.txt               przykładowa mapa
requirements.txt       zależności
tools/map_generator.exe
docs/ERIA_c1_Astar.pdf opis zadania
```
