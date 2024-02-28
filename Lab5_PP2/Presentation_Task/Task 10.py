import re
import codecs

with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    camel_case_string = f.read().strip()

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case)
    snake_case = snake_case.lower()
    return snake_case

snake_case_string = camel_to_snake(camel_case_string)

