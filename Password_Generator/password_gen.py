import random
import string 
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters
from string import digits
from string import octdigits
from string import hexdigits
from string import punctuation
password=""
all=ascii_lowercase+ascii_uppercase+ascii_letters+digits+octdigits+hexdigits+punctuation
length=int(input("Enter the size of password\n"))

for i in range(length):
    password+=random.choice(all)
print(password)