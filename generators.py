import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = list(string.digits)






















def cesar_cipher(user_input, amount):
    cipher_letters = letters.copy()
    cipher_numbers = numbers.copy()
    for n in range(amount):
        out1 = cipher_letters.pop(0)
        out2 = cipher_numbers.pop(0)
        cipher_numbers.append(out2)
        cipher_letters.append(out1)

    user_code = list(user_input.lower())
    for i in user_code:
        if i in cipher_letters:
            index1 = letters.index(i)
            yield cipher_letters[index1]
        elif i in numbers:
            index2 = numbers.index(i)
            yield cipher_numbers[index2]

def loop_on_cesar(user_input, amount):
    encryp_code = ''
    func = cesar_cipher(user_input, amount)
    for w in func:
        encryp_code += w
    return encryp_code
