def pig_latin(text):
    say = ""
    gap=" "
    senl = []
    # Separate the text into words
    words = text.split(" ")
    for i in range(len(words)):
        k = words[i]
        lk = [a for a in k]
        a = lk[0]
        lk.append(a)
        lk.pop(0)
        lk.append("ay")
        w= say.join(lk)
        senl.append(w)
        i=i+1

    return gap.join(senl)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"