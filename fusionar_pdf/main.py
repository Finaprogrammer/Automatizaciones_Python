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
        merge_pdfs(pdf_files, output_file)
        print(f"PDFs merged successfully into {output_file}")
    else:
        print("No PDF files found in the specified folder.")