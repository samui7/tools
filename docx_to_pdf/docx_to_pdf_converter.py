# -*- encoding: utf-8 -*-
import os
import sys
import win32com.client as client

def docx_to_pdf(docx_name, pdf_name):

    # parse path strings
    # assuming the docx and pdf are in the current working directory
    cwd = os.getcwd()
    docx_path = cwd + "\\" + docx_name
    pdf_path = cwd + "\\" + pdf_name
    
    # convert docx to pdf
    try:
        word = client.DispatchEx("Word.Application")
        if os.path.exists(pdf_path):
            # will replace existing pdf file if name already exists
            os.remove(pdf_path)
        worddoc = word.Documents.Open(docx_path, ReadOnly = 1)
        worddoc.SaveAs(pdf_path, FileFormat = 17)
        worddoc.Close()
        return pdf_path
    except:
        print("Error")
        return 1

if __name__=='__main__':
    docx_name = sys.argv[1]
    pdf_name = sys.argv[2]
    docx_to_pdf(docx_name, pdf_name)
