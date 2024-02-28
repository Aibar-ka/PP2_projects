import codecs
import re

pattern = r'[A-Z][^A-Z]*'
with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    text = f.read().strip()


result = re.findall(pattern, text)
print(result)