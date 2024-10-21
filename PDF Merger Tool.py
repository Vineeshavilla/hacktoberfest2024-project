import PyPDF2
import os

def merge_pdfs(output, *pdf_files):
    """
    Merge multiple PDF files into one.
    
    :param output: Name of the output merged PDF
    :param pdf_files: Paths of the PDF files to merge
    """
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_files:
        with open(pdf, 'rb') as file:
            merger.append(file)

    with open(output, 'wb') as output_pdf:
        merger.write(output_pdf)

    print(f"Merged {len(pdf_files)} files into {output}")

# Example usage
if __name__ == "__main__":
    files = input("Enter the PDF files to merge (comma-separated): ").split(',')
    output_file = input("Enter the name of the output merged PDF: ")
    merge_pdfs(output_file, *files)
