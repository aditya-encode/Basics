def comma_code(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

items = ['apples', 'bananas', 'tofu', 'cats']

tems = ['apples', 'bananas', 'tof', 'cat']
print(comma_code(tems))