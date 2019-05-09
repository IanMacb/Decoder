def uniqueKey(string, index):
    if index == 16:
        return True
    char = string[index]
    rest = string[:index] + string[index + 1:]
    return (char not in rest) and uniqueKey(string, index + 1)


message = open("message.txt", "r")
word = message.readline()
length = len(word)

for i in range(length-16):
    string = word[i:i+16]
    if uniqueKey(string, 0):
        print(string)
