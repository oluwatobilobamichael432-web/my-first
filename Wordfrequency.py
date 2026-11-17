def word_requency():
    sentence = input("Enter a complete sentence\n").lower().split()

    word = {}

    for item in sentence:
        if item in word:
            word[item] += 1
        else:
            word[item] = 1
    result = ""
    for char, count in word.items():
        result += f"{char}: {count}\n"
    print(result)
    frequent = ""
    highest_count = 0

    for char, count in word.items():
        if count > highest_count:
            highest_count = count
            frequent = char


    return f"Most frequent word: {frequent}"
print(word_requency())