#!/usr/bin/env python
import sys
import os
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

out_put_name = 'Merged_File.pdf'

input_dir = '/home/eduardo/Documents/PDF_Merging/input_files'

out_dir = '/home/eduardo/Documents/PDF_Merging/'

def get_pdf_list(in_dir):
    print('Reading pdf file list')

    pdf_dir = in_dir
    file_list = os.listdir(pdf_dir)
    file_list.sort()
    pdf_dir_list = []
    for file in file_list:
        pdf_dir_list.append(os.path.join(in_dir,file))
    return pdf_dir_list

def PDF_merge(list_of_pdf,out_dir):

    pdf_list = list_of_pdf
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()

    for file in pdf_list:
        print('Opening File {}'.format(file))
        pdf_file = open(file, 'rb')
        pdf_Reader = PyPDF2.PdfFileReader(pdf_file,strict=False)
        print(pdf_Reader)
        for pageNum in range(pdf_Reader.getNumPages()):
            pageObj = pdf_Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    # Now that you have copied all the pages in all files of the directory the documents, write them into the a new document
    out_dir = os.path.join(out_dir,out_put_name)
    pdfOutputFile = open(out_dir, 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf_file.close()


if __name__=='__main__':

  pdf_list = get_pdf_list(input_dir)
  PDF_merge(pdf_list,out_dir)
