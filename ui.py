from tkinter import *
from tkinter import ttk
from functions import open_pdf, convert_pdf

def ui():

    # start a new TK window to the application
    window = Tk()
    window.title("PDF to Audiobook")
    window.config(padx=20, pady=16, bg='#199999')

    # this frame contains all options that should be choosen by the user before converting the pdf to audio
    frame = Frame(window, padx=10, pady=10, bd=1, relief='solid', bg='#198888') 
    frame.grid(column=0, row=1) 
    

    # text speed choose area
    title_label = Label(frame, text="Text Speed:", bg='#199999')
    title_label.grid(column=0, row=2)

    options = list(range(-10, 10))
    selected_option = IntVar()
    select_speed = ttk.Combobox(frame, textvariable=selected_option, values=options, width=10, background='#199999')    
    select_speed.grid(column=1, row=2, padx=10)
    
    # audio language choose area
    title_label = Label(frame, text="Language:", bg='#199999')
    title_label.grid(column=0, row=1, pady=6)

    options = ['en-us', 'pt-br']
    selected_option = StringVar()
    select_language = ttk.Combobox(frame, textvariable=selected_option, values=options, width=10)    
    select_language.grid(column=1, row=1, pady=6)
    
    # gender choose area
    title_label = Label(frame, text="Gender:", bg='#199999')
    title_label.grid(column=0, row=3, pady=6)

    options = ['male', 'female']
    selected_option = StringVar()
    select_gender = ttk.Combobox(frame, textvariable=selected_option, values=options, width=10)    
    select_gender.grid(column=1, row=3, pady=6)

    # upload fdp area
    upload_button = Button(frame, text="Upload PDF", bg='#199999', highlightthickness=0, command=lambda: open_pdf())
    upload_button.grid(column=1, row=4, pady=6)

    # button out of frame to convert the selected pdf to audio
    watermark_button = Button(text="Convert PDF", bg='#199999', highlightthickness=0, command=lambda: convert_pdf(select_language.get(), select_gender.get(), select_speed.get()))
    watermark_button.grid(column=0, row=2, pady=10)
    
    # keeps the app running all the time until it gets manually closed
    window.mainloop()