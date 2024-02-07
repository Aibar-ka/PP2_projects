def word_frequency(str1):
    words = str1.split()
    f_dict = {}

    for i in words:
        if i in f_dict:
            f_dict[i] += 1
        else:
            f_dict[i] = 1

    return f_dict


text = input()
result = word_frequency(text)
print(result)