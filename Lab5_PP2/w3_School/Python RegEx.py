import re

text = "The rain in spain"
x = re.search("^The.*Spain$", text)
x_x = re.search("Portugal", text)
print("1: ", x_x)


text2 = "The rain in Spain"
x2 = re.findall('ai', text2)
x3 = re.findall('Portugal', text2)
print("2: ", x2)
print("3: ", x3)


text3 = "The rain in Spain"
x4 = re.search("\s", text3)
print("The first white-space character is located in position:", x4.start())


text4 = "The rain in Spain another"
x5 = re.split("\s", text4, 1)
print("5: ", x5)


text5 = "The rain in Spain"
x6 = re.sub("\s", " -_- ", text5)
print("6: ", x6)


txt7 = "The rain in Spain"
x7 = re.search("ai", txt7)
print("7: ", x7)


txt8 = "The rain in Spain"
x8 = re.search(r"\bS\w+", txt8)
print("8: ", x8.span())


txt9 = "The rain in Spain"
x9 = re.search(r"\bS\w+", txt9)
print("9: ", x9.string)


txt10 = "The rain in Spain"
x10 = re.search(r"\bS\w+", txt10)
print("10: ", x10.group())