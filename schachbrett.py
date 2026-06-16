import string

abc = string.ascii_lowercase[:8]

for i in range(8, 1, -1):
    for z in range(8):
        print(f"{abc[z]}{i} ", end="")
    print()