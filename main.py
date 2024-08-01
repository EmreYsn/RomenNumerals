from tkinter import *

def roman_translate(roman):
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
        'CM': 900, 'M': 1000
    }
    i = 0
    num = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_numerals:
            num += roman_numerals[roman[i:i + 2]]
            i += 2
        else:
            num += roman_numerals[roman[i]]
            i += 1
    return num

def numeral_translate():
    num1 = entry_1.get()
    try:
        result = roman_translate(num1)
        label_2.config(text=f"{num1} = {result}")
    except KeyError:
        label_2.config(text="Please enter a valid Roman Numerals")

window = Tk()
window.title("Roman Numerals")
window.config(width=300,height=300)

label_1 = Label(window,padx=25,pady=25,text="Please enter the roman numerals to translate")
label_1.pack()

entry_1 = Entry(window)
entry_1.pack()

button_1 = Button(window,text="Translate",command=numeral_translate)
button_1.pack()

label_2 = Label(window)
label_2.pack()

window.mainloop()