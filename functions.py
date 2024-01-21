from tkinter import filedialog, messagebox
import PyPDF2
import os
import requests
from dotenv import load_dotenv
import shutil
from pydub import AudioSegment

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


def show_message():
    answer = messagebox.askquestion("PDF converted! ", "Save the audio?")

    if answer == "yes":
        save_audio()
        messagebox.showinfo(title='saved', message='audio saved')

def gender_voice (gender, hl):
    if gender == 'male':
        if hl == 'en-us': return 'John'
        else: return 'Dinis'
    else:
        if hl == 'en-us': return 'Amy'
        else: return 'Marcia'

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
    
    with open('files/audio.mp3', 'wb') as arquivo_mp3:
        arquivo_mp3.write(content.content)

    show_message()

# not working yet
    
# def save_audio():
#     file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Arquivos MP3", "*.mp3")])

#     # play(audio)
#     if not file_path:
#         return

#     audio = AudioSegment.from_file("files/audio.mp3", format="mp3")
#     audio.close()

#     audio.export(file_path, format="mp3")
