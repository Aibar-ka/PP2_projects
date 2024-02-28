import codecs
import re

pattern = r'[ ,.]'
with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    text = f.read()

matches = re.sub(pattern,":", text)
print(matches)