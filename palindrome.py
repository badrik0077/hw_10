def is_palindrome(word):
    if len(word) == 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


try:
  assert is_palindrome("level") == True
  assert is_palindrome("sagas") == True
  assert is_palindrome("hero") == False
  assert is_palindrome("drama") == False

except AssertionError:
  print("Неверно, проверьте функцию на разных значениях")

else:
  print("Все хорошо, все работает")