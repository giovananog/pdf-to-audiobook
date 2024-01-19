from tkinter import filedialog
import PyPDF2
import os
import requests
from dotenv import load_dotenv
import shutil

def open_pdf():
    path = filedialog.askopenfilename()
    shutil.copy2(path, 'files/pdf.pdf')

def read_pdf():
    texto = ""
    with open('files/pdf.pdf', 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

        for pagina_num in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[pagina_num]
            texto += pagina.extract_text()
    print(texto)


def convert_pdf(hl, v, src):

    load_dotenv()

    read_pdf()

    key = os.getenv('KEY')
    print(key)
    parameters = {
        "key": key,
        "hl": hl,
        'v': v,
        'src': src
    }
    
    content = requests.get(url="http://api.voicerss.org/", params=parameters)
    content.raise_for_status()
    
    with open('audio.mp3', 'wb') as arquivo_mp3:
        arquivo_mp3.write(content.content)
