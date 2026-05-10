import pyperclip

text=pyperclip.paste()
alt_text=""

up_case=True

for i in text:
    if up_case:
        alt_text+=i.upper()
    else:
        alt_text+=i.lower()
    up_case=not up_case

pyperclip.copy(alt_text)
print(alt_text)

#if you copy some t,e,x,t to,t,he clipboard (for instance, this sentence) and run this program, the output and clipboard contents become this:
#hello,guys,how are  you?