fin  = open("/home/oybek/menshikov/razlojeniye_na_slagayemiye/input.txt")
fout = open("/home/oybek/menshikov/razlojeniye_na_slagayemiye/output.txt","a")

num: int = int(fin.readline())
sqrt_num: int = int(num ** 0.5)

numbers: list = [i for i in range(1, num)]

def generate(sum: int = 0, prefix: list = []):
    if sum > num:
        return
    if sum == num:
        fout.write("+".join(prefix) + "\n")
        return
    for i in numbers:
        prefix.append(str(i))
        sum += i

        generate(sum, prefix)

        prefix.pop()
        sum -= i

        

generate()

fin.close()
fout.close()

# Done successfully, Alhamdulillah