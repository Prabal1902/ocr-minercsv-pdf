#scaned pdf to readable pdf conversion

import ocrmypdf

def ocr(file_path, save_path):
    file_path = r"sample1.pdf" #target_file
    ocrmypdf.ocr(file_path,save_path, skip_text=True)

if __name__ == '__main__':
    ocr("scanned.pdf", "scanned1.pdf")  #revoke function #(,file_save_name)