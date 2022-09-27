import random
import string

def uid():
    a = ''
    b= ''
    c=''
    d=''

    letters = string.ascii_lowercase
    c = ( ''.join(random.choice(letters) for i in range(3)) )

    # printing uppercase
    letters = string.ascii_uppercase
    b = ( ''.join(random.choice(letters) for i in range(3)) )

    # printing letters
    letters = string.ascii_letters
    d = ( ''.join(random.choice(letters) for i in range(5)) )

    # printing digits
    letters = string.digits
    a =( ''.join(random.choice(letters) for i in range(3)) )

    id = a+b+c+d
    return id


# print(uid())