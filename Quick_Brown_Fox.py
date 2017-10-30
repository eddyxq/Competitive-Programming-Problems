def is_pangram(phrase):
    flag = 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            missing_chars.append(char)
            flag = 0
    return flag

n = int(input())

for x in range(n):
    missing_chars = []

    sentence = input()
    sentence = str.lower(sentence)

    if is_pangram(sentence) == 1:
        print("pangram")

    else:
        x = ''.join(missing_chars)
        print("missing " + x)