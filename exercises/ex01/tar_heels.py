"""An exercise in remainders and boolean logic."""

__author__ = "730391530"


# Begin your solution here...

name: int = int(input("Enter an int: "))

if (name % 2 == 0):
    if (name % 7 == 0):
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if (name % 7 == 0):
        print("HEELS")
    else:
        print("CAROLINA")
  