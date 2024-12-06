from googletrans import Translator

def translate(text, dest='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text