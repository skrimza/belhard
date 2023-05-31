# writing a function-generator, accepting integer
# count, and returning the specified number of 
# prime numbers, for example:
# count=5
# result=2, 3, 5, 7, 11

def prime_numbers(count):
    counter = 0
    num = 2
 
    while counter < count:
        if is_prime(num):
            yield num
            counter += 1
        num += 1
 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
primes = prime_numbers(15)
for prime in primes:
    print(prime)