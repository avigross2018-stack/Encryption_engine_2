import generators as gen
from menu import menu, user_code


def main():
    user_choise = menu()
    user_input, user_input2 = user_code(user_choise)
    dict_of_ciphers = {"1" : gen.loop_on_cesar, "2" : gen.loop_on_fence, "3" : gen.loop_on_rand, "4" : gen.loop_on_atbsh}
    if user_choise == "1":
        print(dict_of_ciphers[user_choise](user_input, user_input2))
    else:
        print(dict_of_ciphers[user_choise](user_input))


main()