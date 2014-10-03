def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num
    
def main():
    num = 0
    prime_pair = 0
    while prime_pair < 50:
        prime1 = prime_check(num)
        prime2 = prime_check(num + 2)
        num = num + 1
        if prime1 + 2 == prime2:         
            print '%d and %d are a pair!' % (prime1, prime2)
            prime_pair = prime_pair + 1

if __name__ == '__main__':
    main()
