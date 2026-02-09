import string
import random
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



def rand_cipher(user_input):
    rand_list = letters + numbers
    for i in user_input:
        rand = random.choice(rand_list)
        yield rand

def loop_on_rand(user_input):
    encryp_final = ''
    rand_func = rand_cipher(user_input)
    for i in rand_func:
        encryp_final += i
    return encryp_final
