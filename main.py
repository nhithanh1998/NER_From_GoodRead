# -*- coding: utf-8 -*-
import codecs
import json
import spacy
from langdetect.lang_detect_exception import LangDetectException
from nltk import sent_tokenize
import os
from langdetect import detect
from utils.utils import preprocess

review_file = os.path.join(os.path.dirname(__file__), 'review.json')
comment_file = os.path.join(os.path.dirname(__file__), 'comment.json')
review_output_file = os.path.join(os.path.dirname(__file__), 'review_output.json')
comment_output_file = os.path.join(os.path.dirname(__file__), 'comment_output.json')


def get_data(read_file):
    with open(read_file, encoding="utf8") as f:
        rs = json.load(f)
        return [obs.get('content') for obs in rs]


def write_result(sentence, entities, preprocess_sentence, language, output_file):
    dictionary = {
        "sentence": sentence,
        "preprocess": preprocess_sentence,
        "entities": entities,
        "language": language
    }
    json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)
    with codecs.open(output_file, "a", "utf-8") as f:
        f.write(json_object)
        f.write('\n')


nlp_vi = spacy.load("vi")
nlp_en = spacy.load("en_core_web_sm")

review_data = get_data(review_file)
comment_data = get_data(comment_file)

for txt in review_data:
    try:
        lang = detect(txt)
        if lang == 'vi':
            nlp = nlp_vi
        else:
            nlp = nlp_en
        paragraphs = txt.split("\n")
        for paragraph in paragraphs:
            for sent in sent_tokenize(paragraph):
                preprocess_sent = preprocess(sent)
                doc = nlp(preprocess_sent)
                ents = []
                for ent in doc.ents:
                    if hasattr(ent, "label"):
                        ents.append((ent.text, ent.label_))
                if ents:
                    write_result(sentence=sent, preprocess_sentence=preprocess_sent, entities=ents, language=lang,
                                 output_file=review_output_file)
    except LangDetectException:
        pass

