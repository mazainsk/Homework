import fitz     # Если нужный модуль отсутствует, нужно установить в терминале: pip install PyMuPDF
import os

from tkinter import filedialog as fd
from tkinter import messagebox as mb


pdf_file = 'Большая_книга_проектов_Python_Свейгарт_Эл_Z_Library.pdf'

def pdf_to_txt(pdf_document):
    text = {}
    with fitz.open(pdf_document) as doc:
        for num, page in enumerate(doc.pages(25, 420)):
            text[num] = page.get_text()
    p_count = 0
    prog_text = {0: {}}
    for i in text.values():
        page_ = str(i).split('\n')
        last_key = 0
        for line_ in page_:
            dot_pos = line_.find('.')
            if 1 < dot_pos <= 3:
                if line_[dot_pos - 1].isdecimal():      # с большой вероятностью найденный фрагмент - строка кода программы
                    key_= int(line_[:dot_pos])
                    if key_ in prog_text[p_count]:      # номер строки найден
                        if last_key == key_:            # повтор предыдущего номера!
                            key_ += 1
                        else:
                            p_count += 1
                            prog_text[p_count] = {}
                    prog_text[p_count][key_] = line_[dot_pos + 2:]
                    last_key = key_

    try: os.mkdir(path + 'output')
    except FileExistsError: pass
    finally: os.chdir(path + 'output')

    for i in range(len(prog_text)):
        with open(f'{i+1:0>2}' + '.py', 'w', encoding='utf-8') as out_file:
            for j in prog_text[i].values():
                # при записи строки необходимо заменить неразрывные пробелы на обычные
                out_file.writelines(str(j).replace(chr(160), chr(32)) + '\n')


while True:
    file = fd.askopenfilename(title="Открыть файл для сканирования содержимого",
                              initialfile=pdf_file,
                              filetypes=(('', pdf_file),),
                              initialdir='/')
    if file != '': break
    if mb.askyesno("Не выбрано", "Хотите выйти?"): break

path = file.replace(pdf_file, '')
pdf_to_txt(file)