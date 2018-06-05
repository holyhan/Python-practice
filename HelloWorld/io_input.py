
def reverse(text):
    return text[::-1]   # 使用切片倒序返回字符串


def is_palindrome(text):
    text = filter_illegal_characters(text)
    return text == reverse(text)

def filter_illegal_characters(text):
    forbidden = ('.', '?', '!', ':',
                 ';', '-', '--', '(',
                 ')', '[', ']', '...',
                 "'", '"', '/', ',',
                 ' ', '，', '！', '？')
    for character in forbidden:
        text = text.replace(character, '')
    return text.lower()


something = input('Enter text: ')
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
