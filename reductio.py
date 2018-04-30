f = open('book.txt','rU')
book = f.read()
f.close()

list = book.split(" ")
list[0] = 0

def freq(word):
    return reduce(lambda a,b: a+1 if b == word else a,list)

print freq("letter")
print freq("the")

