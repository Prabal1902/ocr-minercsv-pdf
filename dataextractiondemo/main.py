from pdfminer.high_level import extract_pages, extract_text

for page_layout in extract_pages("scanned4.pdf"):
    for element in page_layout:
        print(element)

text = extract_text("scanned4.pdf")
print(text)