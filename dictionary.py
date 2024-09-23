import random
import string

def generate_password(min_length,numbers=True,special_char=True):
        letters=string.ascii_letters
        digits=string.digits
        special=string.punctuation
        charcters=letters
        print(charcters)
        if numbers:
            charcters+= digits
        if special_char:
            charcters+=special
        print(charcters)


generate_password(1)
