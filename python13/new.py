astr = "Hello bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)
# when the first conversion fails, it just drops into the except: clause and the program continues
astr = "123"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)
# when the second conversion succeeds, it ignores the except: clause and the program continues.
print (float(99) / 100)
def thing():
    print("Hello world")
    print(" world")
print("stop")
thing()
thing()
def lang_flick(greetings):
    if greetings == 'en':
        return 'bonjour'
    else:
        return 'hola'
print(lang_flick('en') , 'Glenn')
print(lang_flick('es') , 'Helen')
name = input("Please enter your name: ")
print("Hello, " + name + "!")
