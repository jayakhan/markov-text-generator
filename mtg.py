from collections import defaultdict
import nltk
import random

#Return extended sentence from training corpus
def pick_sentence(corpus, word):
    punctuations = ['.', '?', '!']
    sentence = ''
    for i in range(len(corpus)):
        corpus_word = ' '.join(corpus[i : i + len(word.split(' '))])
        if  corpus_word == word:
            for element in range(i + len(word.split(' ')), len(corpus)):
                while len(sentence.split(' ')) < 16 and corpus[i] not in punctuations:
                    sentence += ''.join(corpus[i]) + ' '
                    i += 1
                break
            break
    return sentence.replace(" ,",",")

#Create probability distribution by frequency of words appeared in training corpus
def calculate_probability(model, total_count):
    for key, value in model.items():
        model[key] = value/total_count

#Pick random word by weight from model
def pick_random_word(model):
    word_backoff = []
    word_prob = []
    for key, value in model.items():
        word_backoff.append(key) 
        word_prob.append(value)
    return random.choices(word_backoff, word_prob)

#Create language model
def create_model(count, model, sentence, n, corpus):
    for i in range(len(corpus)):
        if ' '.join(corpus[i : i + n]) == ' '.join(sentence):
            count += 1
            model[' '.join(corpus[i : i + n + 1])] += 1 
    return count

def finish_sentence(sentence, n, corpus, deterministic=False):
    model = defaultdict(lambda:0)
    count = 0
    punctuations = ['.', '?', '!']
    if not any(char in punctuations for char in sentence):
        if deterministic:
            if len(sentence) == n:
                total_count = create_model(count, model, sentence, n, corpus)
                if total_count > 0:
                    calculate_probability(model, total_count)
                    return pick_sentence(corpus, max(model, key= lambda x: model[x]))
                else: 
                    n = n - 1
                    while(n > 0):
                        return finish_sentence(sentence[:-1], n, corpus, deterministic)
                    return "found no match"
            else: return 'please select right n gram model'
        else:
            if len(sentence) == n:
                total_count = create_model(count, model, sentence, n, corpus)
                if total_count > 0:
                    calculate_probability(model, total_count)
                    random_word = pick_random_word(model)
                    return pick_sentence(corpus, ''.join(random_word))
                else: 
                    n = n - 1
                    while(n > 0):
                        return finish_sentence(sentence[:-1], n, corpus, deterministic)
                    return "found no match"
            else: return 'please select right n gram model'
    else: return "word list contains punctuations"


if __name__ == "__main__":
    nltk.download('gutenberg')
    nltk.download('punkt')
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())

    words = finish_sentence(
        ['190', '2'],
        2,
        corpus,
        deterministic=True,
    )
    print(words)