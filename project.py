def calculate_frequencies(file_contents):
    file_contents= "Akshad is a very nice guy. He helps everyone. Click here for more.."


    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just"]

# LEARNER CODE START HERE
    l = file_contents.split(" ")
    for strng in l:
        for ltr in strng:
            if ltr in punctuations:
                strng.remove(ltr)
        if strng.lower() in uninteresting_words:
            l.remove(strng)

    d = {}
    for element in l:
        if element not in d:
            d[element] = 0
        d[element] += 1

    return d

