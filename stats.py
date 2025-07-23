def count_words(bookContents):
    words = bookContents.split()
    wordCount = len(words)
    return wordCount

def count_chars(bookContents):
    characterCount = {}

    for char in bookContents:
        char = char.lower()
        if char in characterCount:
            characterCount[char] += 1
        else:
            characterCount[char] = 1

    return characterCount

def sort_on(items):
    return items["num"]

def sort_chars(characterCount):
    sorted_list = [{"char": char, "num": count} for char, count in characterCount.items() if char.isalpha()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

