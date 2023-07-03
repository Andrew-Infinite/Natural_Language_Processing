import nltk
from collections import defaultdict

text = "<s> i am at hiroshima university </s> <s> i live in hiroshima </s> <s> i like hiroshima </s>"
text2 = "<s> i live in an apartment </s>"

# Tokenize the text into sentences
words =  text.split()
words2 = text2.split()

# Tokenize each sentence into words
tokenized_word = [word for word in words]
tokenized_word2 = [word2 for word2 in words2]
tokenized_word2 = tokenized_word + tokenized_word2

# Initialize a dictionary to store the bigram counts
bigram_counts = defaultdict(int)
word_counts = defaultdict(int)
word_counts2 = defaultdict(int)
preceding_word = None
preceding_word2 = None

# counting words, and counting pair words
for word in tokenized_word:
    if preceding_word is not None:
        current_word = word
        bigram_counts[(preceding_word, current_word)] += 1
        word_counts[current_word] += 1
    preceding_word = word

for word2 in tokenized_word2:
    if preceding_word2 is not None:
        current_word2 = word2
        if bigram_counts.get((preceding_word2, current_word2))==None:
          bigram_counts[(preceding_word2, current_word2)] = 0
        word_counts2[current_word2] += 1
    preceding_word2 = word2

bigram_probabilities = {}
bigram_with_Laplace = {}

# Iterate over the bigram counts
for bigram, count in bigram_counts.items():
    try:
      bigram_probabilities[bigram] = count / word_counts[bigram[1]]
    except:
      print("skip")
    bigram_with_Laplace[bigram] = (count+1)/(word_counts[bigram[1]] +len(word_counts2))

print(bigram_probabilities)
print(bigram_with_Laplace)
