import ocrmypdf
from pdfminer.high_level import extract_pages, extract_text
import tabula as tb
import pandas as pd


def p1():  # process 1 or p1 converts all PDF into readable PDFs. This is a redundancy process to make sure image
    # PDFs can be processed by OCRmyPDF.
    def ocr(file_path, save_path):
        file_path = r"sample1.pdf"  # this needs to be linked to var fileURL located in JS file of website
        ocrmypdf.ocr(file_path, save_path, skip_text=True)

    if __name__ == '__main__':
        ocr("scanned.pdf", "scanned1.pdf")  # saves file_path input file as pdf named scanned1.pdf


def p2():  # p2 extracts all text from the readable PDF file.
    for page_layout in extract_pages("scanned1.pdf"):
        for element in page_layout:
            print(element)  # extracts unique headers need to apply regression expression (re) to make use of
            text = extract_text("scanned1.pdf")  # extracts text
            print(text)


def p3():  # p3 outputs tabular data from PDF in the form of a CSV anf Excel File.
    file = "scanned1.pdf"
    table = tb.read_pdf(file)
    csv_table = tb.convert_into(file, 'pdf_convert_csv.csv')  # outputs csv file from scanned1.pdf
    df = pd.concat(table)
    excel_file = df.to_excel('pdf_convert.xlsx')  # outputs excel file from scanned1.pdf


# function calling order
p1()
p2()
p3()
