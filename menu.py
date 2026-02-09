from generators import chars


def menu():
    print("1. Caesar cipher\n2. Fence cipher\n3. AtBsh cipher\n4. Random cipher")
    while True:
        cipher_type = input("Select a cipher type (1-4):  ")
        if cipher_type in ["1", "2", "3", "4"]:
            return cipher_type
        else:
            print("Please choose only between 1 and 4")


def user_code(cipher_type):
    not_correct = True
    while not_correct:
        user_input = input("Please enter your encryption code:  ")
        if cipher_type == "1":
            while True:
                try:
                    user_input2 = int(input("Select the number of hops for encryption:  "))
                except ValueError:
                    print("Please enter a number only!")
                    continue
                break
        else:
            user_input2 = 0
        for char in user_input:
            if char in chars:
                print("Please enter only letters and numbers")
                not_correct = True
                break
            not_correct = False
    return user_input.lower(), user_input2
