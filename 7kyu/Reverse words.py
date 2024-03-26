def reverse_words(text):
    result = ''
    text = text.split(' ')
    for word in text:
        result += ' ' + word[::-1]
    return result[1:]
