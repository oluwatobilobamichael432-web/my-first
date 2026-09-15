def palindrome():

    word = input("Enter a word\n")

    length = 0

    for _ in word:
        length += 1

        first = 0
        last = length-1

    while first < last:
        if word[first] != word[last]:
            return f"{word} is not a palindrome"
        first += 1
        last -= 1

    return f"{word} is a palindrome"
print(palindrome())