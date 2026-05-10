import pyperclip

text=pyperclip.paste()

alt_txt=text.split('\n')

def alter():
    art_txt=[]
    for i in alt_txt:
        i='*'+i
        art_txt.append(i)
    return art_txt

alt_txt=alter()
text='\n'.join(alt_txt)
pyperclip.copy(text)
print(text) 