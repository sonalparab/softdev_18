f = open('book.txt','rU')
book = f.read()
f.close()

book = book.split(" ")
book = [0] + book


# BECAUSE THE PURPOSE OF THE ASSIGNMENT IS TO WORK WITH LIST COMPHREHENSION/REDUCE,
# WE'RE IGNORING THE INACCURACY THAT PUNCTUATION/UPPER CASE LETTERS WILL CAUSE
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
    # takes too long to use dictionary comprehension...
    # count_dict = { key: freq(key) for key in book }
    count_dict = dict()
    for word in book:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return reduce( lambda a,b: a if count_dict[a] > count_dict[b] else b, count_dict.keys() )
    # return reduce(lambda a,b: a if a != b and freq(a) > freq(b) else b,book)

print "Most frequent word"
# print "This will take a long time to run, the result should be 'the'..."
print most_freq()
