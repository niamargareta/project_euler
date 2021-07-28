

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    print(text)
    print(type(text))
    words = text.split()
    print(words)
    print(type(words))
    first_word = words[0]
    print(first_word)
    print(type(first_word))
    return first_word


first_word('there was a good boy')

first_word("dia jelek tapi baik hati")
