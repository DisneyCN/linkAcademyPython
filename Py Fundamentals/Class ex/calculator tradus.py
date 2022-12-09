from tkinter import *
from translate import Translator

import operator

def Translate(TextVar):
    translator = Translator(from_lang= InputLanguageChoice,to_lang=TranslateLanguageChoice)
    Translation = translator.translate(TextVar)
    return Translation
  
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
}    
while True:
    try:   
        message = input('Start ? Yes/Something else...')
        if message == "Yes":   
            InputLanguageChoice = 'Romanian'    
            TranslateLanguageChoice = input('Enter Language : ')
            a = int(input(Translate('Introduceți 1-ul : \n')))
            b = int(input(Translate('Introduceți al 2-lea : \n')))
            op = input(Translate("Operația : "))
            print(str(a), op, str(b), Translate("este"), ops[op](a,b))
        else:
            print('Bye-Bye')
    except StopIteration:
        pass
