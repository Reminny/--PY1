from random import randint


def get_unique_list_numbers() -> list[int]:
    random_list = []
    while len(random_list) != 15:
        random_digit = randint(-10, 10)
        if random_digit not in random_list:
            random_list.append(random_digit)

    return random_list  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
