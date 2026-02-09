import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = list(string.digits)


def cesar_cipher(user_input, amount):
    cipher_letters = list(string.ascii_letters)
    for n in range(amount):
        out = cipher_letters.pop(0)
        cipher_letters.append(out)
    user_code = list(user_input.lower())
    for i in user_code:
        index = letters.index(i)
        yield cipher_letters[index]

def loop_on_cesar(user_input, amount):
    encryp_code = ''
    func = cesar_cipher(user_input, amount)
    for w in func:
        encryp_code += w
    return encryp_code

print(loop_on_cesar('avi', 1))