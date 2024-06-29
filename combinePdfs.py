import PyPDF2, os

def getAllPdfs(directory: str) -> list:
    pdfFiles = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            pdfFiles.append(file)
    return pdfFiles

def openPdf(file: str) -> PyPDF2.PdfReader:
    pdfReader = PyPDF2.PdfReader(file)
    return pdfReader

def mergePdfs(pdfFiles: list, output: str):
    pdfMerger = PyPDF2.PdfMerger()
    for pdf in pdfFiles:
        pdfMerger.append(pdf)
    with open(output, 'wb') as output_pdf:
        pdfMerger.write(output_pdf)

if __name__ == '__main__':
    import sys
    
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    pdfFiles = getAllPdfs(directory)
    mergePdfs(pdfFiles, 'merged.pdf')