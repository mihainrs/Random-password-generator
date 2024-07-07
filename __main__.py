import random
from string import printable as pas_elem
password = []

pass_length = int(input("How long should the password be? Please input the number of letters: "))

if pass_length > 4 and pass_length <= 20:
    new_pass = range(0, pass_length + 1)
    for n in new_pass:
        password.append(random.choice(pas_elem))
    print("Here's your random password: " + str(''.join(password)))
else:
    print("Please input a number between 5 and 20")