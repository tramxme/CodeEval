import math

def is_prime(num):
    n = 3
    while(n < math.sqrt(num) + 1):
        if num % 2 == 0 or num % n == 0:
            return False
        n+=2
    return True

def run():
    count = 1
    total = 2
    n = 3
    while(count < 1000):
        if(is_prime(n)):
            count += 1
            total += n
        n+=2

    print(total)
    return 0

run()
