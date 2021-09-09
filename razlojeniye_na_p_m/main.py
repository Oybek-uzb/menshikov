import math

fin  = open("/home/oybek/menshikov/razlojeniye_na_p_m/input.txt")
fout = open("/home/oybek/menshikov/razlojeniye_na_p_m/output.txt","w")

primes = [2, 3]
num = int(fin.readline())
num_sqrt = math.ceil(num ** 0.5)

for i in range(5, num_sqrt):
    is_prime = True

    for j in primes:
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

res = ""
is_started = False

while True:
    is_devided = False
    for i in primes:
        if num % i == 0:
            if not is_started:
                res = str(i)
                is_started = True
            else:
                res = res + "*" + str(i)
            
            num = int(num / i)
            is_devided = True
            break
    if not is_devided:
        if is_started and num != 1:
            res = res + "*" + str(num)
        break

if not is_started:
    res = str(num)

fout.write(res)

fin.close()
fout.close()

# Done successfully, Alhamdulillah