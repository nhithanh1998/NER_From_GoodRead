import re


def remove_emoji_and_special_character(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def load_useless_words():
    stop_words = []
    with open("useless_word.txt", encoding="utf-8") as f:
        for word in f.readlines():
            stop_words.append(word.strip())
    return stop_words


USELESS_WORDS = load_useless_words()


def remove_useless_words(txt):
    for useless_word in USELESS_WORDS:
        txt = txt.replace(useless_word, '')
    return txt


def preprocess(string):
    string = remove_useless_words(string)
    string = remove_emoji_and_special_character(string)
    string = string.strip()
    return string
