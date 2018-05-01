f = open('book.txt','rU')
book = f.read()
f.close()

book = book.split(" ")
book = [0] + book

def freq(word):
    return reduce(lambda a,b: a+1 if b == word else a,book)

print "Frequency of 'the'"
print freq("the")
print "Frequency of 'a'"
print freq("a")
print "Frequency of 'letter'"
print freq("letter")
print

def group_freq(words):
    return reduce(lambda a,b: a+b,[freq(a) for a in words])

print "Group frequency of 'the' and 'letter'"
print group_freq(["the","letter"])
print "Group frequency of 'the' and 'a'"
print group_freq(["the","a"])
print "Group frequency of 'the' and 'a' and 'letter'"
print group_freq(["the","a","letter"])
print

def most_freq():
    return reduce(lambda a,b: a if a != b and freq(a) > freq(b) else b,book)

print "Most frequent word"
print most_freq()


