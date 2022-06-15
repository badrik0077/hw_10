import random

name = ''
name = input("Введите Ваше имя: ")
print(f'Пользователь: {name}.')
count = 0
all_count = 0
all_games = 0

words_file = open('words.txt', 'r')  # открытия файла и установка флага на чтение r

for items in words_file.readlines():  # читаем файл по строчно
    words_true = items.replace('\n', '').lower()  # Убираем перенос строки и делаем все в нижнем регистре
    words = random.sample(list(words_true), len(list(words_true)))  # Переводим в список и мешаем список
    words = ''.join(words)  # Из списка в слово

    answer = input(f"Угадайте слово {words}: ")

    if words_true == answer.lower():
        print("Верно! Вы получаете 10 очков!")
        count += 10
    else:
        print(f"НЕ верно! Верный ответ - {words_true}!")

words_file.close()

history_file = open('history.txt', 'a+')  # открытия файла и установка флага для записи
history_file.write(f"{name} {count}\n")
history_file.close()

history_file = open('history.txt', 'r')  # открытия файла и установка флага для записи
for items in history_file.readlines():
    if name in items:
        all_games += 1
        all_count += int(items.replace(f'{name} ', ''))

print(f'Общий результат: {all_count}')
print(f'Игр: {all_games}')
history_file.close()
