import tkinter as tk
from tkinter import filedialog, messagebox

class MainWindow :
    def __init__ (self, root, pdf_processor) :
        self.root = root
        self.root.title("PDF Processor")
        self.pdf_processor = pdf_processor
        
        # tlacidlo na otvorenie pdf
        self.open_pdf_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        self.open_pdf_button.pack()

        #tlacidlo na sputenie spracovania
        self.process_pdf_button = tk.Button(self.root, text="Process PDF", command=self.process_pdf)
        self.process_pdf_button.pack()

        # miesto na zobrazenie vysledok 
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.selected_file_path = None
    
    def open_pdf(self):
        file_path = filedialog.askopenfilename(title="Vyber PDf subor", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.selected_file_path = file_path
            self.result_label.config(text="Selected file: " + file_path)
        else:
            self.result_label.config(text="No file selected")
    
    def process_pdf(self):
        if not self.selected_file_path:
            messagebox.showwarning("Warning", "No file selected")
            return
        
        try:
            intersection_info = self.pdf_processor.process_pdf(self.selected_file_path)

            self.result_label.config(text="Intersection info: " + intersection_info)

            
        except Exception as e:
            messagebox.showerror("Error", str(e))