import pyttsx3
import PyPDF2
book = open('python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(90,pages):
    page = pdfReader.getPage(90)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    