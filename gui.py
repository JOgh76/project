import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pdf_procesor import PdfProcessor  # Make sure the import matches your file name
import fitz  # PyMuPDF
from PIL import Image, ImageTk

class MainWindow:
    def __init__(self, root, pdf_proccesor):
        self.root = root
        self.root.title("PDF Processor")

        # Use the passed PdfProcessor instance
        self.pdf_proccesor = pdf_proccesor

        # Frame for buttons
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)

        # Button to open PDF
        self.open_pdf_button = ttk.Button(button_frame, text="Open PDF", command=self.open_pdf)
        self.open_pdf_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Button to process PDF
        self.process_pdf_button = ttk.Button(button_frame, text="Process PDF", command=self.process_pdf)
        self.process_pdf_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Label to show result
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        # Canvas to show PDF preview
        self.canvas = tk.Canvas(self.root, width=600, height=800)
        self.canvas.pack(pady=10)

        self.selected_file_path = None

    def open_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Vyber PDF súbor",
            filetypes=[("PDF files", "*.pdf")],
        )
        if file_path:
            self.selected_file_path = file_path
            self.result_label.config(text="Selected file: " + file_path)
            self.show_pdf_preview(file_path)
        else:
            self.result_label.config(text="No file selected")

    def show_pdf_preview(self, pdf_path):
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # Load the first page
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = img.resize((600, 800), Image.LANCZOS)  # Resize to fit the canvas
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.image = self.img_tk  # Keep a reference to avoid garbage collection

    def process_pdf(self):
        if not self.selected_file_path:
            messagebox.showwarning("Warning", "No file selected")
            return

        try:
            # Call the method from PdfProcessor (make sure the name matches: process_file)
            output_image_path = self.pdf_proccesor.process_file(self.selected_file_path)
            self.result_label.config(text="Processing complete. See the preview below.")
            self.show_image_preview(output_image_path)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_image_preview(self, image_path):
        img = Image.open(image_path)
        img = img.resize((600, 800), Image.LANCZOS)  # Resize to fit the canvas
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)
        self.canvas.image = self.img_tk  # Keep a reference to avoid garbage collection


if __name__ == "__main__":
    root = tk.Tk()
    pdf_proccesor = PdfProcessor()
    app = MainWindow(root, pdf_proccesor)
    root.mainloop()