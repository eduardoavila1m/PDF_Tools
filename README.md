# PDF_Tools

This tool allows to merge multiple PDF files into a single PDF through python code.

## System Requirements

This module utilizies python as the main programing language and is ran in "Python 3"

This module requires PyPDF2

## installing dependencies

To install this dependency
 
	pip install PyPDF2

## Use Instructions

Create One directory that contains the PDFs to be merged together.

	cd ~
	mkdir PDF_Merging
	cd PDF_Merging
	mkdir input
	mkdir output

Place all the PDFs in the directory "~/PDF_Merging/input"

Run the script with the follwing command

	python PDF_merge.py ~/PDF_Merging/input ~/PDF_Merging/output
	
The merged PDF will be placed under the name "Merged_File.pdf" found in the ~/PDF_Merging/output directory

For help run the following command

	python PDF_merge.py -h

## Documentation

	https://pypi.org/project/PyPDF2/
	
	https://pythonhosted.org/PyPDF2/
