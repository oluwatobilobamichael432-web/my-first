def count_word():
    sentence = input("Enter a complete sentence\n").lower().split()
    dictionary = {}

    for word in sentence:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    result = ""
    for word, count in dictionary.items():
        result += f"{word}: {count}\n"

    return result

print(count_word())