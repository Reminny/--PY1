from random import sample
import string


def get_random_password() -> str:
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits

    return ''.join(sample(characters, 8))


print(get_random_password())
