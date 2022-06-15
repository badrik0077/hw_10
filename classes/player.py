class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []


    def count_used_words(self):
        """ Возвращает количество слов которые угадал пользователь"""
        return len(self.used_words)

    def add_word(self, word):
        """ Запоминает верное слово в списке слово которые угадал пользователь"""
        self.used_words.append(word)

    def has_never_seen(self,word):
        """ Проверяет что слово не было еще угадано пользователем"""
        return word not in self.used_words

    def get_mame(self):
        """Возвращает имя"""
        return self.name

    def __repr__(self):
        return f"{self.name}, {self.used_words}"


