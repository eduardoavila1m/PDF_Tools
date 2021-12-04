#!/usr/bin/env python3
import sys
import os
import os.path
from os import path
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse


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
        if file.lower().endswith(('.pdf')):
            pdf_dir_list.append(os.path.join(in_dir,file))
    return pdf_dir_list

def PDF_merge(list_of_pdf,out_dir):
    try:
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

        print('The file {} was created in directory {}'.format(out_put_name,out_dir))

    except OSError as error:
        print(error)


def checkDirectories(inputDir,outputDir):

    if not path.exists(inputDir):
        
        print('The Path: {} Does not exist. PDF files can cnot be found.'.format(inputDir))
        sys.exit(0)

    if not path.exists(outputDir):
        try:
            os.mkdir(outputDir)
            print('The Path: {} Does not exist. This directory will be created.'.format(outputDir))
        except OSError as error:
            print(error)

def parse_args():

    #Activate help fucntion in parser
    parser = argparse.ArgumentParser(add_help=True, )
    parser.add_argument('in_dir', help='Output Directory')
    parser.add_argument('out_dir', help='Input Directory')

    ##Check that arguments where given

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    else:
        return parser.parse_args()

if __name__=='__main__':

    args =  parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir

    checkDirectories(in_dir,out_dir)

    ## Obtain List of PDF Files
    pdf_list = get_pdf_list(in_dir)
    print('List of PDF to merge: ')

    for file in pdf_list:
        print(file)

    PDF_merge(pdf_list,out_dir)
