Exercise: 1
def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2


N = int(input())
squares_generator = generate_squares(N)
for i in squares_generator:
    print(i)


Exercise: 2
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input())

even_generator = even_numbers(n)

print(end=" ")
for num in even_generator:
    print(num, end=", " if num < n - 1 else "\n")

Exercise: 3

def generate_3_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num


n = int(input())

divisible_3_4 = generate_3_4(n)

print(end=" ")
for num in divisible_3_4:
    print(num, end=", ")

Exercise: 4

def squares(a, b):

    for num in range(a, b + 1):
        yield num ** 2

a = 3
b = 7
print("from ", a, "to ", b)
for square in squares(a, b):
    print(square)

Exercise: 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
print(n," to 0:")
for number in countdown(n):
    print(number)
