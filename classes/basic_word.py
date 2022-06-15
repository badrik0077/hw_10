class BasicWord:
    """ Класс для большого слова """

    def __init__(self, value, sub_words):
        #исходное слово
        self.value = value
        # набор допустимых подслов
        self.sub_words = sub_words

    def get_word(self):
        """    Возвращает оригинальные слова """
        return self.value


    def has_subword(self, word):
        """проверяет наличие подслов в слове"""
        return word in self.sub_words

    def number_of_sub_words(self):
        """возвращает количество подслов в слове"""
        return len(self.sub_words)

    def __repr__(self):
        return f"{self.value}, {self.sub_words()}"

#b = BasicWord("Щекотка", ["кот", "щека"])

#print(b)
#print(b.number_of_sub_words())
#print(b.has_subword("кот"))
#print(b.has_subword("щека"))

