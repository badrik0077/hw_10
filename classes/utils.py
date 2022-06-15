import requests as requests

#import json
import random
#from random import randint



from classes.basic_word import BasicWord


def load_words_from_jsonkeeper(path):
    """ Загружает список из внешнего хранилища"""

    response = requests.get(path)
    list_of_words = response.json()
    return list_of_words

def load_random_word(path):
    """ Получает одно слово на основе списка из внешнего хранилища"""
    list_of_words = load_words_from_jsonkeeper(path)
    random_word = random.choice(list_of_words)

    word = random_word["word"]
    sub_words = random_word["subwords"]

    basic_word = BasicWord(word, sub_words)

    return basic_word

#w = load_random_word("https://jsonkeeper.com/b/19S7")

#print(w)