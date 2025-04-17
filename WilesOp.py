f = open("coeffs.txt","r")
line_strings = f.readlines()
f.close()
coeffs = []
for ls in line_strings:
    coeffs.append(int(ls))
f2 = open("primes.txt","r")
prime_strings = f2.readlines()
f2.close()
primes = []
for ps in prime_strings:
    primes.append(int(ps))
f3 = open("wiles_op.txt","w")
for p in primes:
    a = 1 + p - coeffs[p-1]
    f3.write(str(p) + " " + str(a)+"\n")
f3.close()
