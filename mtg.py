"""Markov Text Generator.

Jaya Khan, 2021
"""

import nltk


def initialize_corpus(n, corpus):
    tokens = (n-1)*['<START>']+corpus
    m = [(tuple([tokens[i-p-1] for p in reversed(range(n-1))]), tokens[i]) for i in range(n-1, len(tokens))]
    return m

def finish_sentence(sentence, n, corpus, deterministic=False):
    model = initialize_corpus(n, corpus)
    if deterministic:
        ngram_counter = {}
        context = {}
        punctuations = ['.', '?', '!']

        for ngram in model:
            if ngram in ngram_counter:
                ngram_counter[ngram] += 1
            else:
                ngram_counter[ngram] = 1
            prev_words, target_word = ngram
            if prev_words in context:
                context[prev_words].append(target_word)
            else:
                context[prev_words] = [target_word]

        while len(sentence) < 16:
            test_dict = {}
            history = [s for s in sentence[-n+1:]]
            next_tokens = context[tuple(history)]
            for token in next_tokens:
                test_dict[token] = ngram_counter[(tuple(history), token)]
            sentence.append(max(test_dict, key= lambda x: test_dict[x]))
            if any(char in punctuations for char in sentence):
                break
        return sentence

                

if __name__ == "__main__":
    nltk.download('gutenberg')
    nltk.download('punkt')
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())
    
    words = finish_sentence(
        ['she', 'was', 'not'],
        3,
        corpus,
        deterministic=True,
    )
    print(words)