from tkinter import *
from tkinter import ttk

def ui():

    # start a new TK window to the application
    window = Tk()
    window.title("PDF to Audiobook")
    window.config(padx=20, pady=16, bg='#DCDCDC')

    # this frame contains all options that should be choosen by the user before converting the pdf to audio
    frame = Frame(window, padx=10, pady=10, bd=1, relief='solid') 
    frame.grid(column=0, row=1) 
    

    # text speed choose area
    title_label = Label(frame, text="Text Speed: ")
    title_label.grid(column=0, row=2)

    opcoes = list(range(-10, 10))
    opcao_selecionada = IntVar()
    entrada_selecao = ttk.Combobox(frame, textvariable=opcao_selecionada, values=opcoes)    
    entrada_selecao.grid(column=1, row=2)
    
    # audio language choose area
    title_label = Label(frame, text="Language: ")
    title_label.grid(column=0, row=1, pady=6)

    opcoes = ['en-us', 'en-uk', 'pt-br', 'pt-pt', 'es-es']
    opcao_selecionada = StringVar()
    entrada_selecao = ttk.Combobox(frame, textvariable=opcao_selecionada, values=opcoes)    
    entrada_selecao.grid(column=1, row=1, pady=6)
    
    # upload fdp area
    upload_button = Button(frame, text="Upload PDF", highlightthickness=0)
    upload_button.grid(column=1, row=3, pady=6)

    # button out of frame to convert the selected pdf to audio
    watermark_button = Button(text="Convert Audio", highlightthickness=0)
    watermark_button.grid(column=0, row=2)
    
    # save audio button 
    save_button = Button(text="Save Audio", highlightthickness=0)
    save_button.grid(column=2, row=4)
    
    # keeps the app running all the time until it gets manually closed
    window.mainloop()