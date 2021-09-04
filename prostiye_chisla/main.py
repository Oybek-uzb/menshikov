import math

fin  = open("/home/oybek/menshikov/prostiye_chisla/input.txt")
fout = open("/home/oybek/menshikov/prostiye_chisla/output.txt","a")

a, b = map(int, fin.readline().split())
primes = [2, 3]

root = math.ceil(b ** (1.0/2))

for i in range(2, root+1):
    isPrime = True
    for j in primes:
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(i)

# print(primes)
sqrt_init = math.ceil(a ** (1.0/2))

for i in range(a, b):
    isPrime = True

    if (sqrt_init + 1) ** 2 == i:
        sqrt_init = math.ceil(i ** (1.0/2))
    
    for j in primes:
        if j > sqrt_init:
            break
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime:
        fout.write("{}\n".format(i))

# fout.write(str(a+b))

fin.close()
fout.close()

# Done successfully, Alhamdulillah