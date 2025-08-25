import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def stworzTablice(n):
    logging.info('Utworzono tablice')
    return [[0] * n for _ in range(n)]

def siamese(start_row, start_col, n, counter, tab):
    r, c = 0, n // 2 #pozycja startowa (pierwszy wiersz, srodkowa kolumna cwiartki)
    for _ in range(n * n):
        #ustawienie wartosci komorki
        logging.info(f'start_row: {start_row}, start_col: {start_col} \nr: {r}, c: {c}')
        tab[start_row + r][start_col + c] = next(counter)

        #przejscie do nowej komorki
        nr = (r - 1) % n
        nc = (c + 1) % n

        #kolizja
        if tab[start_row + nr][start_col + nc] != 0:
            r = (r + 1) % n
        else:
            r = nr
            c = nc

def doublyEven(tablica, n):
    iterator = 1

    #wypelniamy tablice kolejnymi wartosciami
    for r in range(n):
        for c in range(n):
            tablica[r][c] = iterator
            iterator += 1
    
    mask = {(0,0), (0,3), (3,0), (3,3), (1,1), (1,2), (2,1), (2,2)} #pozycje miedzy ktorymi odwracamy wartosci
    #petle obslugujace bloki 4x4
    for block_row in range(0, n, 4):
        for block_col in range(0, n, 4):
            #petle obslugujace komorki w danym bloku
            for i in range(4):
                for j in range(4):
                    if (i, j) in mask:
                        row , col = block_row + i, block_col + j
                        tablica[row][col] = n**2 + 1 - tablica[row][col]

def singlyEven(tablica, n):
    m = n // 2
    k = (m - 1) // 2
    licznik = iter(range(1, n*n + 1))

    #wypelnianie cwiartek 1 -> 4 -> 2 -> 3
    siamese(0, 0, m, licznik, tablica) #A
    siamese(m, m, m, licznik, tablica) #B
    siamese(0, m, m, licznik, tablica) #C
    siamese(m, 0, m, licznik, tablica) #D

    #zmiana k pierwszych kolumn A<->D
    for r in range(m):
        for c in range(k):
            tablica[r][c], tablica[r+m][c] = tablica[r+m][c], tablica[r][c]

    #zmiana k-1 ostatnich kolumn C<->B
    for r in range(m):
        for c in range(n - (k - 1), n):
            tablica[r][c], tablica[r+m][c] = tablica[r+m][c], tablica[r][c]

    #A(0, m)A(m, m) <-> D(0, m)D(m, m)
    #wspolrzedne cwiartek
    ax, ay = 0, 0
    dx, dy = m, 0

    #wspolrzedne komorek
    x1, y1 = m // 2, 0
    x2, y2 = m // 2, m // 2

    h1, h2 = tablica[ax + x1][ay + y1], tablica[ax + x2][ay + y2]
    tablica[ax + x1][ay + y1], tablica[ax + x2][ay + y2] = tablica[dx + x1][dy + y1], tablica[dx + x2][dy + y2]
    tablica[dx + x1][dy + y1], tablica[dx + x2][dy + y2] = h1, h2

def uzupelnijTablice(tablica, n):
    if n % 2 == 1:
        logging.info('Typ kwadratu: nieparzysty')
        #definicja startowej komorki
        licznik = iter(range(1, n*n + 1))

        siamese(0, 0, n, licznik, tablica)
            
        return tablica

    elif n % 4 == 0:
        logging.info('Typ kwadratu: doubly even')

        doublyEven(tablica, n)

        return tablica
    
    else:
        logging.info('Typ kwadratu: singly even')
        
        singlyEven(tablica, n)

        return tablica
    

def podsumowanieTablicy(tablica, n):
    logging.info('Wypisywanie tablicy do terminala')

    #obliczenia
    row_sum = [sum(row) for row in tablica]
    col_sum = [sum(col) for col in zip(*tablica)]
    diag = sum(tablica[i][i] for i in range(n))
    reverse_diag = sum(tablica[i][n - 1- i] for i in range(n))

    return {
        "tablica": tablica,
        "suma_wierszy": row_sum,
        "suma_kolumn": col_sum,
        "suma_przekatnych": {
            "glowna": diag,
            "przeciwna": reverse_diag
        }
    }

if __name__ == '__main__':
    n = int(input("Podaj wartosc boku kwadratu: "))
    tab = stworzTablice(n)
    uzupelnijTablice(tab, n)
    wyniki = podsumowanieTablicy(tab, n)

    #print do konsoli
    print("Kwadrat magiczny:")
    for row in wyniki["tablica"]:
        print("".join(f"{col:4}" for col in row))

    print("\nSuma wierszy:", wyniki["suma_wierszy"])
    print("Suma kolumn:", wyniki["suma_kolumn"])
    print("Suma przekątnych:", wyniki["suma_przekatnych"])