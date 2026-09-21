def palindrome ():

    text = input("Enter a word\n")

    length = 0

    for _ in text:
        length += 1

        x = 0
        y = length-1
    while x < y:
        if text[x] != text[y]:
            return f"{text} is not palindrome"
        x += 1
        y -= 1
    return f"{text} is palindrome"
    
print(palindrome())