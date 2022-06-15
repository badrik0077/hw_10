import utils
from classes.basic_word import BasicWord
from classes.player import Player
PATH = "https://jsonkeeper.com/b/19S7"

print("Введите имя игрока")
user_input = input()
player = Player(user_input)

print(f"Привет, {player.get_mame()}")

basic_word = utils.load_random_word(PATH)
print(f"Составьте {basic_word.number_of_sub_words()} слов из слова {basic_word.value.upper()}")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
print("Поехали, ваше первое слово?")


i = 0

while player.count_used_words() < basic_word.number_of_sub_words():
    print()
    user_input = input().strip().lower()
    # это слово - не стоп
    # это слово есть в базовом слове
    # Это слово еще не использовалось (оно новое)
    if user_input in ["стоп", "stop"]:
        print("Игра завершена!")


    #if not basic_word.has_sub_word(user_input):
        #print("такого слова нет")
        #continue

    if len(user_input) < 3:
        print("Игра завершена")
        continue

    if not player.has_never_seen(user_input):
        print("Такое слово уже было использовано")
        continue

    player.add_word(user_input)

    print("верно")


print("слова закончились, игра завершена!")
print(f"вы угадали {player.count_used_words()} слов!")
