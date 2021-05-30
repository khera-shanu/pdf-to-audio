import pyttsx3
from pdfreader import SimplePDFViewer

def convert_to_audio(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

with open("/Users/lawliet/pdf-to-audio/pdfs/sample_1.pdf", "rb") as fd:
    viewer = SimplePDFViewer(fd)
    text = None
    for item in viewer:
        text = "".join(item.strings)
    if text:
        convert_to_audio(text)
