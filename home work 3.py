if not input("Предлагаю проверить свои знания английского! Наберит 'ready', чтобы начать!").lower() == "ready":
    print("Кажется, вы не хотите играть. Очень жаль")

else:
    questions = ["My name____Vova", "I ____ a coder", "I live____ Moscow"]
    answers = ["is", "am", "in"]
    correct_answer = 0
    question_count = len(questions)

for i in range(question_count):
    if input(questions[i]) == answers[i]:
        correct_answer +=1
        print("Ответ верный!")
    else:
        print("Неправльно. Правильный ответ: answers[i]")

print(f"Вот и все! Вы ответили на {question_count} вопросов из {correct_answer} верно, это {question_count/question_count * 100, 2} процентов")
