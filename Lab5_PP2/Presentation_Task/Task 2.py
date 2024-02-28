import codecs
import re


pattern = r'ab{2,3}'
with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    text = f.read()

matches = re.findall(pattern, text)
print(matches)