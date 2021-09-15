```
if __name__ == "__main__":
    nltk.download('gutenberg')
    nltk.download('punkt')
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())

    words = finish_sentence(
        ['familycdd'],
        7,
        corpus,
        deterministic=False,
    )
```

# Examples of Deterministic Cases:
## Please try below use-cases for both deterministic and stochastic modes
## If n gram value is incorrect, you will get a message "please select right n gram model"

```
['family', 'of', 'dashwood', 'there', '.']
[',']
['?']
['right', 'to', 'come']
['right', 'to', 'come', 'instantly']
['dashwood']
['190', '2']
['1', '2']
```


