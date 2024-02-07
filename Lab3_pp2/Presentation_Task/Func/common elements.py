def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    if (set1 and set2):
        return set1 & set2
    else:
        print("No common elements")


a_list = [1, 2, 3, 4, 9]
b_list = [9, 4, 8, 10, 1]

result = common_elements(a_list, b_list)

print(result)