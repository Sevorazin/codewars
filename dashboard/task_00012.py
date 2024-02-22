'''
Ваша задача — отсортировать заданную строку.
 Каждое слово в строке будет содержать одно число.
  Это число обозначает позицию,
   которую слово должно занимать в результате.

Примечание.
 Числа могут быть от 1 до 9.
  Таким образом,
   первым словом будет 1 (а не 0).

Если входная строка пуста,
 верните пустую строку.
  Слова во входной строке будут содержать только допустимые последовательные числа.
'''
import re


def order(sentence):
    if not sentence:
        return ""

    sorted_words = sorted(sentence.split(), key=lambda x: int(re.search(r'\d', x).group()))
    result = ' '.join(sorted_words)

    return print(result)

order('silen4t S5yvak b1uka paSH2a Vital3ii')