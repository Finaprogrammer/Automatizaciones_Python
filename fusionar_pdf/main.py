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
    pdf_files.sort()  # Sort the files to maintain order

    # Merge the PDF files
    merge_pdfs(pdf_files, output_file)  
    print(f"Merged {len(pdf_files)} PDF files into {output_file}.")
    # Check if the output file was created successfully 
    if os.path.exists(output_file):
        print(f"Output file {output_file} created successfully.")
    else:
        print(f"Failed to create output file {output_file}.")
    # Check if the output file is empty
    if os.path.getsize(output_file) == 0:
        print(f"Output file {output_file} is empty.")
    else:
        print(f"Output file {output_file} is not empty.")       
    

