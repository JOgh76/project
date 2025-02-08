import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_procesor import PdfProcessor  # Make sure the import matches your file name

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Processor")

        # Create an instance of the PdfProcessor
        self.pdf_processor = PdfProcessor()

        # Button to open PDF
        self.open_pdf_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        self.open_pdf_button.pack()

        # Button to process PDF
        self.process_pdf_button = tk.Button(self.root, text="Process PDF", command=self.process_pdf)
        self.process_pdf_button.pack()

        # Label to show result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.selected_file_path = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Vyber PDF súbor",
            filetypes=[("PDF files", "*.pdf")],
        )
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
            # Call the method from PdfProcessor (make sure the name matches: process_file)
            intersection_info = self.pdf_procesor.process_file(self.selected_file_path)
            self.result_label.config(text="Intersection info: " + intersection_info)

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
