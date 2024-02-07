def get_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return "There is no max number"


a1 = int(input())
b1 = int(input())
c1 = int(input())

result = get_max(a1, b1, c1)

print(result)