import os
import PyPDF2

def read_file_contents(filename, page=0):
    from read_with_meaning import books_path
    file = os.path.join(books_path, filename)
    print(file)
    pdfFileObj = open(file, 'rb')
  
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(page)
    # extracting text from page
    text = pageObj.extractText()
    # closing the pdf file object
    pdfFileObj.close()
    return text