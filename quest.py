class Question:
    def __init__(self, question, difficulty, right_answer):
        self.question = question
        self.difficulty = difficulty
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score = difficulty * 10

    def get_points(self):
        return self.score

    """Возвращает int, количество баллов.
    Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """

    def is_correct(self):
        return self.user_answer == self.right_answer


    """Возвращает True, если ответ пользователя совпадает 
    с верным ответов иначе False.
    """

    def build_question(self):
        return f"Вопрос: {self.question} \nСложность {self.difficulty}"

    """Возвращает вопрос в понятном пользователю виде, например:
    Вопрос: What do people often call American flag?
    Сложность 4/5
    """

    def build_feedback(self):
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ получено {self.right_answer}"


