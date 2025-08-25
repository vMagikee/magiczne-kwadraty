import logging
import tkinter as tk
from magiczne_kwadraty import magicznyKwadrat
from tkinter import ttk, messagebox

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class App:
    def __init__(self, root):
        self.root = root
        self.var = tk.StringVar()

        #config
        root.title('Magiczne kwadraty')
        root.geometry('600x400')

        #naglowek
        label = ttk.Label(root, text='Podaj rozmiar kwadratu:')
        label.pack(pady=5)

        #input
        entry = ttk.Entry(root, textvariable=self.var)
        entry.pack(pady=5)

        #button
        button = ttk.Button(root, text="Generuj", command=self.generate)
        button.pack(pady=5)

        #frame do tabeli
        self.tree_frame = ttk.Frame(root)
        self.tree_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        #tabela
        self.tree = ttk.Treeview(self.tree_frame, show='')
        self.tree.grid(row=0, column=0, sticky='nsew')

        #pionowy scrollbar
        self.vsb = ttk.Scrollbar(self.tree_frame, orient='vertical', command=self.tree.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.tree.configure(yscrollcommand=self.vsb.set)

        #poziomy scrollbar
        self.hsb = ttk.Scrollbar(self.tree_frame, orient='horizontal', command=self.tree.xview)
        self.hsb.grid(row=1, column=0, sticky='ew')
        self.tree.configure(xscrollcommand=self.hsb.set)

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        #label do sum
        self.summary_label = ttk.Label(root, text='')
        self.summary_label.pack(pady=5)

    def generate(self):
        try:
            n = int(self.var.get())
            kw = magicznyKwadrat(n)
            kw.uzupelnij()
            wyniki = kw.podsumowanie()

            #wyczysc treeview
            self.tree.delete(*self.tree.get_children())

            #ustaw kolumny
            self.tree['columns'] = [f'C{i}' for i in range(n)]
            for i in range(n):
                self.tree.column(f'C{i}', width=40, anchor='center')

            #dodaj wiersze
            for row in wyniki['tablica']:
                self.tree.insert('', 'end', values=row)

            #podsumowanie
            row_sums = ', '.join(str(x) for x in wyniki['suma_wierszy'])
            col_sums = ', '.join(str(x) for x in wyniki['suma_kolumn'])
            diag_sums = wyniki['suma_przekatnych']
            self.summary_label.config(
                text=f"Suma wierszy: {row_sums}\n"
                    f"Suma kolumn: {col_sums}\n"
                    f"Przekatna glowna: {diag_sums['glowna']}\n"
                    f"Przekatna przeciwna: {diag_sums['przeciwna']}"
            )
        except ValueError:
            logging.error('Niepoprawna wartosc, wpisz liczbe!')
            messagebox.showerror('Error', 'Prosze podac liczbe calkowita!')


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()