s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
array = [-1]*26

for i in range(len(s)):
    if array[alphabet.index(s[i])] == -1:
        array[alphabet.index((s[i]))] = i

for i in range(len(array)):
    print(array[i], end=" ")