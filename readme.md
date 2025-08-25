# Magiczne Kwadraty

Projekt w Pythonie do generowania **kwadratów magicznych** różnych rozmiarów oraz wyświetlania ich w GUI (Tkinter).

---

## 📂 Struktura projektu

```
magiczne-kwadraty/
│
├── src/
│   ├── __main__.py
│   ├── magiczne_kwadraty.py    # logika obliczeń
│   └── gui.py                  # interfejs użytkownika (Tkinter)
│
├── tests/
│   └── test_magiczne_kwadraty.py  # testy jednostkowe (pytest)
│
├── requirements.txt
└── README.md
```

---

## 🚀 Jak uruchomić

1. Sklonuj repozytorium lub pobierz projekt.
2. Zainstaluj wymagane zależności:
   ```
   pip install -r requirements.txt
   ```
3. Uruchom aplikację:
   ```
   python -m magiczne-kwadraty
   ```

---

## 🧪 Testy

Projekt wykorzystuje **pytest** do testowania logiki generowania kwadratów magicznych.

Uruchomienie testów:
```
pytest
```

---

## ℹ️ Wymagania

- Python 3.11.2+
- Tkinter (standardowo dostępny w Pythonie)
- pytest (dla testów)

---

## ✨ Funkcje

- Generowanie kwadratów magicznych:
  - Nieparzyste
  - Podzielne przez 4 (doubly even)
  - Podzielne przez 2, ale nie przez 4 (singly even)
- Wyświetlanie w interfejsie graficznym (Tkinter + Treeview)
- Obliczanie i prezentacja sum wierszy, kolumn oraz przekątnych
- Obsługa błędnych danych wejściowych
- Możliwość przewijania tabeli (scrollbary)
