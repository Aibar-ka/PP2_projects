def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


a = int(input())

result = is_even(a)

print(result)