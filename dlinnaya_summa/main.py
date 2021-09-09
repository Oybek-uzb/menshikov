fin  = open("/home/oybek/menshikov/dlinnaya_summa/input.txt")
fout = open("/home/oybek/menshikov/dlinnaya_summa/output.txt","w")

a = fin.readline().strip()
b = fin.readline().strip()
res = ""

len_a = len(a)
len_b = len(b)
print("len_a", len_a)

index_a = len_a - 1
index_b = len_b - 1

memo = 0

while True:
    num_a_i = int(a[index_a]) if index_a >= 0 else 0
    num_b_i = int(b[index_b]) if index_b >= 0 else 0


    if index_b == -1 and index_a == -1:
        fout.write(res)
        break
    else:
        if index_b == -1:
            num_res = num_a_i + memo
            index_a -= 1
        elif index_a == -1:
            num_res = num_b_i + memo
            index_b -= 1
        else:
            num_res = num_a_i + num_b_i + memo
            index_a -= 1
            index_b -= 1
        
        memo = int(num_res / 10)
        res = str(num_res % 10) + res

fin.close()
fout.close()

# Done successfully, Alhamdulillah