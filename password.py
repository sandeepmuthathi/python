import random
import string
char=string.ascii_letters+string.digits+string.punctuation
print("".join((random.choices(char,k=12))))
