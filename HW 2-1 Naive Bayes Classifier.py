import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.BagOfWords = set()
        self.classes = []
        self.class_probs = {}
        self.feature_probs = {}
        self.class_zero_probs = {}

    def train(self, X_train, y_train, v=0):
        #Group word into BagOfWords
        self.BagOfWords = set(word for sentence in X_train for word in sentence.split())
        print("BagOfWords: ",self.BagOfWords)

        # Calculate Class probabilities
        self.classes, class_counts = np.unique(y_train, return_counts=True)
        total_instances = len(y_train)
        self.class_probs = {cls: count / total_instances for cls, count in zip(self.classes, class_counts)}
        print("P(class): ",self.class_probs)

        # Calculate feature probabilities
        self.feature_probs = {}
        self.class_zero_probs = {}
        for cls in self.classes:
            cls_sentence = [X_train[index] for index,group in enumerate(y_train) if group == cls]
            cls_sentence = " ".join(cls_sentence)
            cls_word_counts = {word:np.float64(cls_sentence.count(word)) for word in self.BagOfWords}
            total_word_counts = sum(cls_word_counts.values())
            print("Word Count for",cls,": ",total_word_counts)

            feature_probs = np.array(list(cls_word_counts.values()))
            feature_probs += 1
            if v <= 0:
                feature_probs /= (total_word_counts + len(self.BagOfWords))
                self.class_zero_probs[cls] = 1.0/(total_word_counts + len(self.BagOfWords))
            else:
                feature_probs /= (total_word_counts + v)
                self.class_zero_probs[cls] = 1.0/(total_word_counts + v)
            #print("zero_frequency_Prob",cls,self.class_zero_probs[cls])
            cls_word_counts.update(dict(zip(cls_word_counts.keys(), feature_probs)))

            self.feature_probs[cls] = cls_word_counts
        for key,value in self.feature_probs.items():
            print('P(word|'+str(key)+') ',value)
        print("")

    def predict(self, X_test):
        predictions = []
        for sentence in X_test:
            probabilities = {}
            for cls in self.classes:
                feature_probs = self.feature_probs[cls]
                try:
                    #No zero frequency element
                    likelihoods = np.array([feature_probs[word] for word in sentence.split()])
                except:
                    #Zero Frequency Handling
                    likelihoods = []
                    for word in sentence.split():
                        try:
                            likelihoods.append(feature_probs[word])
                        except:
                            likelihoods.append(self.class_zero_probs[cls])

                #By Naive Bayes Assumption, probability of each element is independent of other element, multiple all probability
                probabilities[cls] = np.prod(likelihoods) * self.class_probs[cls]
                print('P('+cls+'|'+sentence+'): ',probabilities[cls],[(word,prob) for word,prob in zip(sentence.split(),likelihoods)])
            #Find the most probable class for query given
            predicted_class = max(probabilities, key=probabilities.get)
            predictions.append(predicted_class)
        return predictions


v=10

query = ["Japan sake tasting"]
NV = NaiveBayesClassifier()
NV.train(np.array(['Japan Kyoto sake alcohol','Japan Hiroshima Saijo','Saijo sake','Hiroshima Saijo sake']),np.array(['KYT','HRS','HRS','HRS']),10)
result = NV.predict(query)
print(['('+q+') is more probable to be ('+r+')' for q,r in zip(query,result)])

