
f = open("dest.txt", "r")

word_freq = {}     

for line in f:
    words = line.split()          
    for w in words:
        if w in word_freq:
            word_freq[w] += 1     
        else:
            word_freq[w] = 1      

f.close()

for word in word_freq:
    print(word, ":", word_freq[word])
