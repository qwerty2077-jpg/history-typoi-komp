import pdfplumber
from gtts import gTTS


def pdf_to_text(text_path):
    with pdfplumber.PDF(open(text_path, mode='rb')) as pdf_file:
        pages = pdf_file.pages
        str_text = ''.join([page.extract_text() for page in pages]).replace('\n', " ")
    print(str_text)
    return str_text


def text_to_audio(str_text):
    language = 'ru'
    phrase = gTTS(text=str_text, lang=language, slow=False)
    phrase.save("озвучка.mp3")


def main():
    current_text_path = "text.pdf"
    text = pdf_to_text(current_text_path)
    text_to_audio(text)

if __name__ == '__main__':
    main()

