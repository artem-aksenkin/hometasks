word = input('Enter the word to check\n')
a = word[::-1]
if word == a:
    print(True)
else:
    print(False)
