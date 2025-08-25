import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
class magicznyKwadrat():
    def __init__(self, n):
        self.n = n
        self.tablica = [[0] * n for _ in range(n)]
        logging.info(f'Utworzono tablice {n}x{n}')

    def siamese(self, start_row, start_col, size, counter):
        r, c = 0, size // 2 #pozycja startowa (pierwszy wiersz, srodkowa kolumna cwiartki)
        for _ in range(size * size):
            logging.info(f'start_row: {start_row}, start_col: {start_col}, r: {r}, c: {c}')
            self.tablica[start_row + r][start_col + c] = next(counter)

            #przejscie do nowej komorki
            nr = (r - 1) % size
            nc = (c + 1) % size

            #kolizja
            logging.info(f'start_row: {start_row}, start_col: {start_col}, nr: {nr}, nc: {nc}')
            if self.tablica[start_row + nr][start_col + nc] != 0:
                r = (r + 1) % size
            else:
                r = nr
                c = nc

    def doublyEven(self):
        n = self.n
        iterator = 1

        #wypelniamy tablice kolejnymi wartosciami
        for r in range(n):
            for c in range(n):
                self.tablica[r][c] = iterator
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
                            self.tablica[row][col] = n**2 + 1 - self.tablica[row][col]

    def singlyEven(self):
        n = self.n
        m = n // 2
        k = (m - 1) // 2
        licznik = iter(range(1, n*n + 1))

        #wypelnianie cwiartek 1 -> 4 -> 2 -> 3
        self.siamese(0, 0, m, licznik) #A
        self.siamese(m, m, m, licznik) #B
        self.siamese(0, m, m, licznik) #C
        self.siamese(m, 0, m, licznik) #D

        #zmiana k pierwszych kolumn A<->D
        for r in range(m):
            for c in range(k):
                self.tablica[r][c], self.tablica[r+m][c] = self.tablica[r+m][c], self.tablica[r][c]

        #zmiana k-1 ostatnich kolumn C<->B
        for r in range(m):
            for c in range(n - (k - 1), n):
                self.tablica[r][c], self.tablica[r+m][c] = self.tablica[r+m][c], self.tablica[r][c]

        #A(0, m)A(m, m) <-> D(0, m)D(m, m)
        #wspolrzedne cwiartek
        ax, ay = 0, 0
        dx, dy = m, 0

        #wspolrzedne komorek
        x1, y1 = m // 2, 0
        x2, y2 = m // 2, m // 2

        h1, h2 = self.tablica[ax + x1][ay + y1], self.tablica[ax + x2][ay + y2]
        self.tablica[ax + x1][ay + y1], self.tablica[ax + x2][ay + y2] = self.tablica[dx + x1][dy + y1], self.tablica[dx + x2][dy + y2]
        self.tablica[dx + x1][dy + y1], self.tablica[dx + x2][dy + y2] = h1, h2

    def uzupelnij(self):
        n = self.n
        if n % 2 == 1:
            logging.info('Typ kwadratu: nieparzysty')
            licznik = iter(range(1, n*n + 1))
            self.siamese(0, 0, n, licznik)

        elif n % 4 == 0:
            logging.info('Typ kwadratu: doubly even')
            self.doublyEven()
        
        else:
            logging.info('Typ kwadratu: singly even')
            self.singlyEven()
    

    def podsumowanie(self):
        logging.info('Wyliczenie sum kolumn, wierszy i przekatnych')

        n = self.n
        row_sum = [sum(row) for row in self.tablica]
        col_sum = [sum(col) for col in zip(*self.tablica)]
        diag = sum(self.tablica[i][i] for i in range(n))
        reverse_diag = sum(self.tablica[i][n - 1 - i] for i in range(n))

        return {
            "tablica": self.tablica,
            "suma_wierszy": row_sum,
            "suma_kolumn": col_sum,
            "suma_przekatnych": {
                "glowna": diag,
                "przeciwna": reverse_diag
            }
        }

if __name__ == '__main__':
    n = int(input("Podaj wartosc boku kwadratu: "))
    kw = magicznyKwadrat(n)
    kw.uzupelnij()
    wyniki = kw.podsumowanie()

    #print do konsoli
    print("Kwadrat magiczny:")
    for row in wyniki["tablica"]:
        print("".join(f"{col:4}" for col in row))

    print("\nSuma wierszy:", wyniki["suma_wierszy"])
    print("Suma kolumn:", wyniki["suma_kolumn"])
    print("Suma przekątnych:", wyniki["suma_przekatnych"])