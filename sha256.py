import hashlib
inp = input('Enter something: ')
while inp != '':
    print(hashlib.sha256(inp.encode('utf-8')).hexdigest())
    inp = input('(Enter qt to exite) Enter something: ')
    if inp == 'qt':
        break
