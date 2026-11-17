def Palindrome():
    item = input("Enter a word or a sentence\n")
    new = ""
    for i in item:
        if i.isalnum():
            new += i.lower().strip()
    
    length = 0
    for _ in new:
        length += 1

        x = 0
        y = length-1
    while x < y:
        if new[x] != new[y]:
            return f"{item} is not a Palindrome"
        else:
            return f"{item} is a Palindrome"
print(Palindrome()) 
