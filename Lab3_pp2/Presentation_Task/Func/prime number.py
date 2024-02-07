def filter_prime(list1):
    primes = []

    for i in list1:
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                primes.append(i)

    return primes


given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
prime_numbers = filter_prime(given_list)
print(prime_numbers)
