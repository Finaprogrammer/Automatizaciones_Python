import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    # Specify the folder containing the PDF files
    folder_path = "./pdfs"  # Change this to your folder path
    output_file = "merged_output.pdf"


    # Get all PDF files in the folder
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

    if pdf_files:
        # Merge the PDF files
        merge_pdfs(pdf_files, output_file)
        print(f"PDFs merged successfully into {output_file}")
    else:
        print("No PDF files found in the specified folder.")
# This script merges all PDF files in a specified folder into a single PDF file.
# It uses the PyPDF2 library to handle PDF merging.
# Make sure to install PyPDF2 using pip if you haven't already:
# pip install PyPDF2
# You can change the folder_path variable to point to the folder containing your PDF files.     