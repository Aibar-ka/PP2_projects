import codecs
import re


pattern = r'[A-Z][a-z]+'
with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    text = f.read()

matches = re.findall(pattern, text)
print(matches)