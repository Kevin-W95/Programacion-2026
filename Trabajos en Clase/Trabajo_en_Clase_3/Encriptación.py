def cesar_encryp(text, n):
    letter = "abcdefghijklmnopqrstuvwxyz"
    format = ""

    for let in text.lower():
        if let in letter:
            position = letter.find(let)
            new = (position + n) % 26
            format += letter[new]
        else:
            format += letter
    return format

    
