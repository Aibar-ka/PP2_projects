import codecs
import re


def snake_to_camel(snake_case):
    words = re.split(r'_', snake_case)
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case


with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    snake_case_string = f.read().strip()

camel_case_string = snake_to_camel(snake_case_string)
print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)