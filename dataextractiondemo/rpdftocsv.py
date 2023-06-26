import tabula as tb
import pandas as pd

file = "scanned3.pdf"
table = tb.read_pdf(file)
csv_table = tb.convert_into(file, 'pdf_convert_csv.csv')

df = pd.concat(table)

excel_file = df.to_excel('pdf_convert.xlsx')
