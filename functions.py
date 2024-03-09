from tkinter import filedialog, messagebox
import PyPDF2
import os
import requests
from dotenv import load_dotenv
import shutil
from pydub import AudioSegment
import io

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
    return texto

def show_message(arq):
    answer = messagebox.askquestion("PDF converted! ", "Save the audio?")

    if answer == "yes":
        save_audio(arq)
        messagebox.showinfo(title='saved', message='audio saved')

def gender_voice(gender, hl):
    if gender == 'male':
        if hl == 'en-us':
            return 'John'
        else:
            return 'Dinis'
    else:
        if hl == 'en-us':
            return 'Amy'
        else:
            return 'Marcia'

def convert_pdf(hl, v, r):
    load_dotenv()

    text = read_pdf()
    v = gender_voice(v, hl)

    key = os.getenv('KEY')
    parameters = {
        "key": key,
        "hl": hl,
        'v': v,
        'r': r,
        'src': text
    }
    
    content = requests.get(url="http://api.voicerss.org/", params=parameters)
    content.raise_for_status()
    
    output_file_path = 'files/audio.mp3'
    
    with open(output_file_path, 'wb') as arquivo_mp3:
        arquivo_mp3.write(content.content)

    show_message(output_file_path)

def save_audio(audio_path):
    output_file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    if output_file_path:
        shutil.copy2(audio_path, output_file_path)

