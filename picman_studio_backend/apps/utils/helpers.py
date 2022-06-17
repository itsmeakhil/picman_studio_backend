import random
import string


def id_generator(start_string=None, size=10, chars=string.ascii_uppercase + string.digits + string.digits):
    id = "".join(random.choice(chars) for _ in range(size))
    if start_string:
        id = start_string + id
    return id
