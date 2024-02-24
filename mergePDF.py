from PyPDF2 import PdfWriter
import os
merger = PdfWriter()

pdfs = os.listdir('./pdfs/')

for pdf in pdfs:
    merger.append(f"./pdfs/{pdf}")

merger.write("mergedPDF.pdf")
merger.close()
