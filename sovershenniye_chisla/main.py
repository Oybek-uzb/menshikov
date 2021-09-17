fin  = open("/home/oybek/menshikov/sovershenniye_chisla/input.txt")
fout = open("/home/oybek/menshikov/sovershenniye_chisla/output.txt","a")

a, b = map(int, fin.readline().split())

def is_perfect(num):
    sqrt_num: int = int(num ** 0.5)
    sum: int = 1
    for i in range(2, sqrt_num+1):
        if num % i == 0:
            sum = sum + i + num / i

        if sum > num:
            return False
    
    if sum == num:
        return True
for i in range(a, b+1):
    if is_perfect(i):
        fout.write(str(i) + "\n")

fin.close()
fout.close()

# Done successfully, Alhamdulillah