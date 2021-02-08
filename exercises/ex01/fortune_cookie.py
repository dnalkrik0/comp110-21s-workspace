"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730391530"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says . . .")

x: int=randint(1,25)

a: str = "A monkey with waffles will approach you on Saturday. Do not trust him."
b: str = "Today, you will see an amazing human . . . when looking in the mirror."
c: str = "You will soon encounter something familiar, yet inspiring."
d: str = "You will find freedom in something unexpected."
e: str = "You will fail in the near future, but you will rise from it better than before."

if (x <= 5):
    print(a)
else:
    if (x <= 10):
        print(b)
    else:
        if (x <= 15):
            print(c)
        else:
            if (x <= 20):
                print(d)
            else:
                print(e)

print("Now, go spread positive vibes!")
