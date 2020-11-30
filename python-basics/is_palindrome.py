def inverted_string(string):
    inverted = ''
    for i in string:
        inverted = i + inverted
    return inverted


def is_palindrome(string):
    if string == inverted_string(string):
        return True
    return False


print(is_palindrome(''))
print(is_palindrome('radar'))
print(is_palindrome('abs'))