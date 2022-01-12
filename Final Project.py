# Nicholas Hughes (100743493), Franklin Muhuni (100744901), Shriji Shah (100665031)
# Cryptography and Network Security
# Final Project October 12, 2021

# USED TO FIX PLAINTEXT
def fix_Key(plaintext):
    for x in range(len(plaintext) * 2):  # chceks if there is two letter beside eachother that are the same then adds x.
        try:
            if plaintext[x] == plaintext[x + 1]:
                plaintext.insert(x + 1, "X")
        except:
            pass

    if len(plaintext) % 2 != 0:  # if not divisible by 2 append x.
        plaintext += "X"

    return plaintext


# USED FOR GRID
def grid_function(Key, plaintext):
    Alpha = list("UGiSoxrcT>He94w<sVmF8$|7=f#*1zWqj6,NgX-kKdM+.ZD5?tuBCYO@E;&A23Pn:!JQv%lapRI~bhyL0") # alphabet.
    grid = []  # local variables.
    temp = []
    encrypt = []

    for x in Key:  # if letter in key matches with one in alphabet then its poped from the alphabet
        for char in Alpha:
            if x == char:
                Alpha.pop(Alpha.index(char))

    temp += Key + Alpha  # temp value

    for x in range(0, 81, 9):  # makes the grid 9 by 9
        grid.append(list(temp[0 + x: 9 + x]))

    for x in range(0, len(plaintext), 2):  # makes the strings into 2 letter lists.
        encrypt.append(list(plaintext[0 + x: 2 + x]))

    return plaintext, grid, encrypt


# USED FOR POSITION
def position(grid, encrypt):
    result = list()  # local variables.
    result2 = list()
    result3 = list()

    for y in encrypt:  # Gets positon of the letters and appends to results.
        for x in grid:
            if y[0] in x:
                result.append([grid.index(x), x.index(y[0])])
            if y[1] in x:
                result2.append([grid.index(x), x.index(y[1])])

    for x in range(len(result)):  # adds the first x elements of each list together.
        result3.append([result[x], result2[x]])

    return result3  # returns result and grid


# USED FOR ENCRYPTION
def encryption_one(plaintext, position, grid):
    ciphertext = list()

    for pos in range(len(position)):  # gets new position cords.
        if position[pos][0][0] == position[pos][1][0]:
            if position[pos][0][1] == 8:
                ciphertext.append(grid[position[pos][0][0]][position[pos][0][1] - 8])  # at max so goes to start.
            else:
                ciphertext.append(grid[position[pos][0][0]][position[pos][0][1] + 1])  # moves over 1.

            if position[pos][1][1] == 8:
                ciphertext.append(grid[position[pos][1][0]][position[pos][1][1] - 8])  # at max so goes to start.
            else:
                ciphertext.append(grid[position[pos][1][0]][position[pos][1][1] + 1])  # moves over 1.

        elif position[pos][0][1] == position[pos][1][1]:
            if position[pos][0][0] == 8:
                ciphertext.append(grid[position[pos][0][0] - 8][position[pos][0][1]])  # at max so goes to start.
            else:
                ciphertext.append(grid[position[pos][0][0] + 1][position[pos][0][1]])  # moves down 1.

            if position[pos][1][0] == 8:
                ciphertext.append(grid[position[pos][1][0] - 8][position[pos][1][1]])  # at max so goes to start.
            else:
                ciphertext.append(grid[position[pos][1][0] + 1][position[pos][1][1]])  # moves down 1.

        else:
            ciphertext.append(grid[position[pos][0][0]][position[pos][1][1]])  # swaps corners
            ciphertext.append(grid[position[pos][1][0]][position[pos][0][1]])

    ciphertext = "".join(ciphertext)  # creates a string
    return ciphertext  # returns encrypted value

#DID NOT USE THIS FUNCTION
def encryption_two(plaintext, key):
    key = "".join(key)
    key = list(format(ord(val), '08b') for val in key)

    binary = "".join(plaintext)
    binary = list(format(ord(val), '08b') for val in binary)

    # Makes key match length of plaintext
    key = key * int(len(binary)/len(key))
    for x in range(len(binary)%len(key)):
        key = key + [key[x]]

    ciphertext = list()

    # Compare key and binary to get output
    for xKey, yBinary in zip(key, binary):
        temp = str()
        for x in range (len(xKey)):
            temp = temp + str(int(xKey[x]) ^ int(yBinary[x]))
        ciphertext.append(temp)

    ciphertext = "".join((chr(int(val, 2)) for val in ciphertext))


    #ciphertext = str(ciphertext, "utf-8")
    #print(ciphertext)

    ciphertext = list(format(ord(val), '08b') for val in ciphertext)
    #print(ciphertext)

    plaintext2 = list()
    # Compare key and binary to get output
    for xKey, yCipher in zip(key, ciphertext):
        temp = str()
        for x in range (len(xKey)):
            temp = temp + str(int(xKey[x]) ^ int(yCipher[x]))
        plaintext2.append(temp)

    plaintext2 = "".join(chr(int(val, 2)) for val in plaintext2)
    #print(plaintext2)
    #print(plaintext)


    # binary = "".join(chr(int(val, 2)) for val in binary.split(" "))
    # key = "".join(chr(int(val, 2)) for val in key.split(" "))
    #
    # print(binary)
    # print(key)

    return plaintext2


def encryption_three(plaintext, key):
    key = "".join(key)
    key = list(format(ord(val), '08b') for val in key)

    binary = "".join(plaintext)
    binary = list(format(ord(val), '08b') for val in binary)

    # Makes key match length of plaintext
    key = key * int(len(binary) / len(key))
    for x in range(len(binary) % len(key)):
        key = key + [key[x]]

    ciphertext = list()

    # Compare key and binary to get output
    for xKey, yBinary in zip(key, binary):
        temp = str()
        for x in range(len(xKey)):
            temp = temp + str(int(xKey[x]) ^ int(yBinary[x])) # XOR
        ciphertext.append(temp)

    ciphertext = "".join((val for val in ciphertext))
    return ciphertext

#DID NOT USE THIS FUNCTION
def encryption_four(plaintext, key):
    key = "".join(key)
    key = list(format(ord(val), '08b') for val in key)
    plaintext2 = []

    for x in range(0, len(plaintext), 4):
        plaintext2.append(plaintext[x:x+4])

    plaintext2 = "".join([chr(int(val, 2)) for val in plaintext2])

    return plaintext2


# USED FOR DECRYPTION
def decryption_one(ciphertext, key):
    key = "".join(key)
    key = list(format(ord(val), '08b') for val in key)
    ciphertext2 = []

    for x in range(0, len(ciphertext), 8):
        ciphertext2.append(ciphertext[x:x+8])

    # Makes key match length of plaintext
    key = key * int(len(ciphertext2) / len(key))
    for x in range(len(ciphertext2) % len(key)):
        key = key + [key[x]]

    plaintext2 = list()
    # Compare key and binary to get output
    for xKey, yCipher in zip(key, ciphertext2):
        temp = str()
        for x in range(len(xKey)):
            temp = temp + str(int(xKey[x]) ^ int(yCipher[x]))
        plaintext2.append(temp)

    plaintext2 = "".join([chr(int(val, 2)) for val in plaintext2])

    return plaintext2


def decryption_two(ciphertext, position, grid):
    plaintext = list()

    for pos in range(len(position)):  # gets new position cords.
        if position[pos][0][0] == position[pos][1][0]:
            if position[pos][0][1] == 0:
                plaintext.append(grid[position[pos][0][0]][position[pos][0][1] + 8])  # at max so goes to end.
            else:
                plaintext.append(grid[position[pos][0][0]][position[pos][0][1] - 1])  # moves over 1.

            if position[pos][1][1] == 0:
                plaintext.append(grid[position[pos][1][0]][position[pos][1][1] + 8])  # at max so goes to end.
            else:
                plaintext.append(grid[position[pos][1][0]][position[pos][1][1] - 1])  # moves over 1.

        elif position[pos][0][1] == position[pos][1][1]:
            if position[pos][0][0] == 0:
                plaintext.append(grid[position[pos][0][0] + 8][position[pos][0][1]])  # at max so goes to end.
            else:
                plaintext.append(grid[position[pos][0][0] - 1][position[pos][0][1]])  # moves down 1.

            if position[pos][1][0] == 0:
                plaintext.append(grid[position[pos][1][0] + 8][position[pos][1][1]])  # at max so goes to end.
            else:
                plaintext.append(grid[position[pos][1][0] - 1][position[pos][1][1]])  # moves down 1.

        else:
            plaintext.append(grid[position[pos][0][0]][position[pos][1][1]])  # swaps corners
            plaintext.append(grid[position[pos][1][0]][position[pos][0][1]])

    if len(plaintext) % 2 == 0 and plaintext[-1] == "X":  # if not divisible by 2 append x.
        plaintext.pop(-1)

    for x in range(len(plaintext) * 2):  # chceks if there is two letter beside eachother and adds x.
        try:
            if plaintext[x] == plaintext[x + 2] and plaintext[x + 1] == "X":
                plaintext.pop(x + 1)
        except:
            pass

    plaintext = "".join(plaintext)  # creates a string.
    return plaintext  # returns decrypted value.


def main():
    # Opens file and gets plaintext
    file = open("plaintext.txt", "r")
    plaintext = str()

    for line in file:
        plaintext = plaintext + line.replace("\n", "")

    file.close()

    # # Encrypts plaintext to ciphertext
    Key = list("#MaThGoDs")  # key
    plaintext = plaintext.replace(" ", "~") # Changes spaces to ~.
    plaintext = fix_Key(plaintext)
    plaintext, grid, encrypt = grid_function(Key, plaintext)
    results = position(grid, encrypt)

    ciphertext = encryption_one(plaintext, results, grid)

    finalcipher = encryption_three(ciphertext, Key)
    print(finalcipher)

    # Saves ciphertext to file
    file = open("ciphertext.txt", "w")
    file.write(finalcipher)
    file.close()

    # # Opens ciphertext file and saves input to finalcipher for decryption
    # file = open("ciphertext.txt", "r")
    # finalcipher = str()
    #
    # for line in file:
    #     finalcipher = finalcipher + line.replace("\n", "")
    #
    # file.close()

    # Decrypts ciphertext to plaintext
    plaintext2 = decryption_one(finalcipher, Key)
    print(plaintext2)

    ciphertext2, grid, encrypt = grid_function(Key, plaintext2)
    results = position(grid, encrypt)
    plaintext2 = decryption_two(ciphertext2, results, grid)
    plaintext2 = plaintext2.replace("~", " ") # Changes ~ back to spaces.

    print(plaintext2)
    return 0

if __name__ == '__main__':
    main()
