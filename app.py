import tkinter as tk
from gui import MainWindow
from pdf_procesor import PdfProcessor


def main():
    pdf_proccesor = PdfProcessor()

    root = tk.Tk()
    app = MainWindow(root, pdf_proccesor)
    root.mainloop()

if __name__ == '__main__':
    main()