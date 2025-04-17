primes = []
for i in range(2, 10000):
    print(i)
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

f = open("primes.txt","w")
for p in primes:
    f.write(str(p) + "\n")
f.close()
