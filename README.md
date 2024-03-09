# PDF to Audiobook Converter

## Description
This is a simple application that converts PDF files to audio files (MP3) using the VoiceRSS API. The generated audio can be saved to a location of your choice.

## User Interface
![Pdf to Audiobook]('files/image.png')

## Features
- Choose a PDF file for conversion.
- Select the language, gender, and voice speed.
- Convert the PDF into an audio file (MP3).
- Save the audio file to the desired location.

## Requirements
- Python 3.x
- Required libraries (installable via pip): PyPDF2, requests, python-dotenv, pydub

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/giovananog/pdf-to-audiobook.git
   cd pdf-to-audiobook
   ```

2. Create a .env file in the project root with your VoiceRSS API credentials:

    ```bash
        KEY=your_api_key
    ```

3. Run the application:
    ```bash
        python main.py
    ```