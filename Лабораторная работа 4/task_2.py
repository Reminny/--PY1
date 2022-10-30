def get_count_char(str_):
    str_ = str_.lower()
    char_dict = {}
    for char in str_:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict


def percentage_char(dict_):
    percentage_dict = {}
    for char, amount in dict_.items():
        percentage_dict[char] = amount / sum(dict_.values()) * 100

    return percentage_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
