import string
letters = list(string.ascii_letters)
numbers = list(string.digits)


def fence_cipher_gen(string):
    for index, evenw in enumerate(string):
        if index % 2 == 0:
            yield evenw.lower()
    for index, oddw in enumerate(string):
        if index % 2 != 0:
            yield oddw.lower()


def loop_on_fence(user_input):
    encrypted_result = ""
    fence = fence_cipher_gen(user_input)
    for letter in fence:
        encrypted_result += letter
    return encrypted_result