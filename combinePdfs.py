import PyPDF2, os
import argparse

def getAllPdfs(directory: str) -> list:
    """
    Get a list of PDF files in the specified directory.

    Args:
        directory: The directory path to search for PDF files.

    Returns:
        A list of PDF file names.
    """
    pdfFiles = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            pdfFiles.append(file)
    return pdfFiles

def openPdf(file: str) -> PyPDF2.PdfReader:
    """
    Open a PDF file and return a PdfReader object.

    Args:
        file: The path to the PDF file.

    Returns:
        A PdfReader object for the PDF file.
    """
    pdfReader = PyPDF2.PdfReader(file)
    return pdfReader

def mergePdfs(pdfFiles: list, output: str):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        pdfFiles: List of PDF files to merge.
        output: Output file name for the merged PDF.
    """
    pdfMerger = PyPDF2.PdfMerger()
    for pdf in pdfFiles:
        pdfMerger.append(pdf)
    with open(output, 'wb') as output_pdf:
        pdfMerger.write(output_pdf)

if __name__ == '__main__':
    import sys
    parser = argparse.ArgumentParser(description="Merge PDF files in a directory.")
    parser.add_argument("-d", "--directory", type=str, required=True, help="The directory containing the PDF files to merge.")
    parser.add_argument("-o", "--output", type=str, default="merged.pdf", help="The filename of the merged PDF file.")
    args = parser.parse_args()

    # Get PDF files in the specified directory
    pdfFiles = getAllPdfs(args.directory)
    
    # Merge the PDF files
    mergePdfs(pdfFiles, args.output)
    
    print(f"Merged PDFs saved as {args.output}")