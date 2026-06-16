import string

abc = string.ascii_lowercase
numbers = range(8, 1, -1)
print(abc)



while i in range(-8, 1):
    for z in abc:
        print(z + str(i) + " " + z + str((i-1)) + " " + z + str((i-2)) + " " + z + str((i-3)) + " " + z + str((i-4)) + " " + z + str((i-5)) + " " + z + str((i-6)) + " " + z + str((i-7)))