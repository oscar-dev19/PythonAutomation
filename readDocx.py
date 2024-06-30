import docx, sys

def getText(filename:str) -> str:
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Warning: Please provide a .docx file to read from.")
        sys.exit(1)
    docx_file = sys.argv[1]
    print(getText(docx_file))