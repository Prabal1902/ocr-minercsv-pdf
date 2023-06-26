# ocr-minercsv-pdf
This is a python script that takes in PDF and images as input and outputs extracted text and tables as CSV and Excel files.

This project uses the following Modules, make sure to install them before running:
1. OCTmyPDF
2. PDFminer
3. Tabula
4. Pandas

NOTE- The input file is located in def p1() in variable file_path line 10. Change it to input a different file. A new file will be generated named scanned1.pdf (line 14) and this new file will be used subsequently in thr program from now on. You can edit the name for this file too , but make sure to update all references of scanned1.pdf from the program. 

This repository has 4 python files. storpdf.py (scaned to read pdf), main.py (data/text extraction), rpdftocsv.py (read pdf to csv) and backupexperment.py which is a single python file which combines all the other individual python files that were made to test modules. 

   
