from tkinter import *
from translate import Translator

def Translate():
    translator = Translator(from_lang= InputLanguageChoice,to_lang=TranslateLanguageChoice)
    Translation = translator.translate(TextVar)
    return Translation

InputLanguageChoice = 'Romanian'
TranslateLanguageChoice = input('Enter Language : ')
TextVar = input('Enter Mesage : ')

print(Translate())
