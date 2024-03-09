from tkinter import *
from tkinter import ttk
from functions import open_pdf, convert_pdf

def ui():

    # start a new TK window to the application
    window = Tk()
    window.title("PDF to Audiobook")
    window.config(padx=20, pady=16, bg='#199999')

    # this frame contains all options that should be chosen by the user before converting the pdf to audio
    frame = Frame(window, padx=10, pady=10, bd=1, relief='solid', bg='#198888') 
    frame.grid(column=0, row=1) 
    

    # text speed choose area
    title_label = Label(frame, text="Text Speed:", bg='#199999')
    title_label.grid(column=0, row=2)

    speed_options = list(range(-10, 10))
    selected_speed = IntVar()
    select_speed = ttk.Combobox(frame, textvariable=selected_speed, values=speed_options, width=10, background='#199999')    
    select_speed.grid(column=1, row=2, padx=10)
    
    # audio language choose area
    title_label = Label(frame, text="Language:", bg='#199999')
    title_label.grid(column=0, row=1, pady=6)

    language_options = ['en-us', 'pt-br']
    selected_language = StringVar()
    select_language = ttk.Combobox(frame, textvariable=selected_language, values=language_options, width=10)    
    select_language.grid(column=1, row=1, pady=6)
    
    # gender choose area
    title_label = Label(frame, text="Gender:", bg='#199999')
    title_label.grid(column=0, row=3, pady=6)

    gender_options = ['male', 'female']
    selected_gender = StringVar()
    select_gender = ttk.Combobox(frame, textvariable=selected_gender, values=gender_options, width=10)    
    select_gender.grid(column=1, row=3, pady=6)

    # upload PDF area
    upload_button = Button(frame, text="Upload PDF", bg='#199999', highlightthickness=0, command=lambda: open_pdf())
    upload_button.grid(column=1, row=4, pady=6)

    # button out of frame to convert the selected PDF to audio
    convert_button = Button(text="Convert PDF", bg='#199999', highlightthickness=0, command=lambda: convert_pdf(selected_language.get(), selected_gender.get(), selected_speed.get()))
    convert_button.grid(column=0, row=2, pady=10)
    
    # keeps the app running all the time until it gets manually closed
    window.mainloop()
