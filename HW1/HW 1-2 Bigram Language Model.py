import nltk
from collections import defaultdict

text = "<s> i am at hiroshima university </s> <s> i live in hiroshima </s> <s> i like hiroshima </s>"
text2 = "<s> i live in an apartment </s>"

# Tokenize the text into sentences
train =  text.split()
test = text2.split()

BagOfWords = set(word for word in (train + test))

bigram_counts = defaultdict(int)
word_counts = defaultdict(int)
preceding_word = None

# counting words, and counting pair words
for word in train:
    if preceding_word is not None:
        current_word = word
        bigram_counts[(preceding_word, current_word)] += 1
    word_counts[word] += 1
    preceding_word = word

bigram_probabilities_train = {}
bigram_with_Laplace_train = {}

# Iterate over the bigram counts
for bigram, count in bigram_counts.items():
    try:
        bigram_probabilities_train[bigram] = count / word_counts[bigram[0]]
    except:
        #Zero Frequency
        print("skip")
    bigram_with_Laplace_train[bigram] = (count+1)/(word_counts[bigram[0]] + len(BagOfWords))
print(bigram_probabilities_train)
print(bigram_with_Laplace_train)

bigram_probabilities_test = {}
bigram_with_Laplace_test = {}
preceding_word = None
for word in test:
    if preceding_word is not None:
        current_word = word
        try:
            bigram_probabilities_test[(preceding_word, current_word)] = bigram_probabilities_train[(preceding_word, current_word)]
            bigram_with_Laplace_test[(preceding_word, current_word)] = bigram_with_Laplace_train[(preceding_word, current_word)]
        except:
            bigram_probabilities_test[(preceding_word, current_word)] = float('inf')
            bigram_with_Laplace_test[(preceding_word, current_word)] = 1.0/(word_counts[preceding_word] + len(BagOfWords))
    preceding_word = word
print(bigram_probabilities_test)
print(bigram_with_Laplace_test)
