def all_true(elements):
    return all(elements)

my_tuple = tuple(map(bool, input("Enter elements of the tuple separated by space: ").split()))
result = all_true(my_tuple)
print("All elements are True." if result else "Not all elements are True.")
