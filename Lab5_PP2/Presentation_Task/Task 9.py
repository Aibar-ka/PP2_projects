import codecs
import re


with codecs.open("row.txt", "r", "utf_8_sig" ) as f:
    text = f.read().strip()


result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(result)