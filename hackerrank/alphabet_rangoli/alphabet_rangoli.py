from ctypes import pointer


def print_rangoli(size):
    alphabet = ['a', 'b' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rangoli = [[alphabet[size-1]]]
    pointer = size-2
    length = ((size*4)-3)

    while pointer > -1:
        rangoliAdd = []
        for x in range(size-1, pointer, -1):
            rangoliAdd.append(alphabet[x])
        for y in range(pointer, size, 1):
            rangoliAdd.append(alphabet[y])
        rangoliAdd.append(rangoliAdd)
        pointer -= 1

    for x in rangoli:
        rangStr = '-'.join(x)
        print(rangStr.center(length, '-'))

    for y in range((len(rangoli)-2), -1, -1):
        rangStrRev = '-'.join(rangoli[y])
        print(rangStrRev.center(length, '-'))
