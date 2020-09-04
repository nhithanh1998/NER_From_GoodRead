# Named Entity Recognition

Recognize named entity from user's reviews and comments from GoodRead site.

  - Person name as - [**PERSON**]
  - Location name as - [**LOC**]
  - Book name as - [**BOOK**]

## Package requirements


Written by base **Python** and take advantage of [**SpaCy**](https://spacy.io/) nlp library and preprocessing text with **nltk**. We will use 2 nlp models from **SpaCy**: `en_core_web_sm` for *English* and **xx_ent_wiki_sm** for *multiple language* and our target is *Vietnamese*. Therefore we need a little adjust and retrain it.
  - `pip install -U spacy` 
  - `pip install -U spacy-lookups-data`
  - `python -m spacy download en_core_web_sm`
  - `python -m spacy download xx_ent_wiki_sm`
## Project structured
`train_model.py`: function to train **vi** model. At the first time we need to pass `model="xx_ent_wiki_sm"` because we build on our **vi** model from it. And later we modify the `model="vi"` to keep training our model.
`train_data/ner_train.py`: contain trainning data for **vi** model
`useless_word.txt`: list of useless words. We will eliminated it from our string.
`main.py`: recognize **Named Entity** from user's review contents and comment contents then write down to `review_output.json` and `comment_output.json`
`review.json`: contain all review content 
`comment.json`: contain all comment content
`vi`: folder save **vi** model
