fin  = open("/home/oybek/menshikov/drujestvenniye_chisla/input.txt")
fout = open("/home/oybek/menshikov/drujestvenniye_chisla/output.txt","w")

a, b = map(int, fin.readline().split())

sqrt_val = int(a**0.5)
val = sqrt_val ** 2

res_arr = []

def sum_val(a, max, b):
    sum = 1

    for i in range(2, b+1):
        if a%i == 0:
            sum += int(a/i) + i
        if sum > max:
            return 0

    return sum

for i in range(a, b+1):
    if val < i:
        sqrt_val += 1
        val = sqrt_val ** 2

    res_arr.append(sum_val(i, b, sqrt_val))

for i in range(0, len(res_arr)):
    if a <= res_arr[i] <= b and res_arr[res_arr[i]-a] == i + a:
        fout.write(str(res_arr[i]) + " " + str(i+a) + "\n")


fin.close()
fout.close()

# Done successfully, Alhamdulillah