def letter_count(text):
    max_counter = 0
    max_letter = ''
    dictio = {}
    for letter in text:
        if letter in dictio:
            dictio[letter] += 1
        else:
            dictio[letter] = 1
        if dictio[letter] > max_counter:
            max_counter = dictio[letter]
            max_letter = letter
    return (max_letter, max_counter)

print(letter_count('jfscujhnergccwudhbmgnkwjdbgkbh'))

        