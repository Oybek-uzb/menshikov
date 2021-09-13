fin  = open("/home/oybek/menshikov/dlinnoye_proizvedeniye/input.txt")
fout = open("/home/oybek/menshikov/dlinnoye_proizvedeniye/output.txt","a")

a = fin.readline().strip()
b = fin.readline().strip()

if len(a) < len(b):
    extra = a
    a = b
    b = extra

len_a = len(a)
len_b = len(b)

mul_array = []
final_result = ""

def mul_big_num(a, b, postfix):
    global mul_array, len_a
    res = ""
    memo = 0
    result = 0

    if b == 1:
        res = a + postfix
        mul_array.append(res)
        return

    for i in range(len_a - 1, -1, -1):
        result = int(a[i]) * b + memo

        memo = int(result / 10)
        res = str(result % 10) + res
    
    if memo != 0:
        res = str(memo) + res

    res = res + postfix
    mul_array.append(res)

def sum_big_num(a, b):
    len_a = len(a)
    len_b = len(b)

    index_a = len_a - 1
    index_b = len_b - 1

    res = ""
    memo = 0
    num_res = 0
    
    while True:
        num_a_i = int(a[index_a]) if index_a >= 0 else 0
        num_b_i = int(b[index_b]) if index_b >= 0 else 0

        if index_a == -1 and index_b == -1:
            return res
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

postfix = ""
for i in range(len_b - 1, -1, -1):
    if b[i] != "0":
        mul_big_num(a, int(b[i]), postfix)

    postfix += "0"

len_mul_array = len(mul_array)

if len_mul_array == 0:
    final_result = "0"
elif len_mul_array == 1:
    final_result = mul_array[0]
else:
    for i in range(1, len_mul_array):
        if i == 1:
            final_result = sum_big_num(mul_array[0], mul_array[1])
        else:
            final_result = sum_big_num(final_result, mul_array[i])

fout.write(final_result)

fin.close()
fout.close()

# Done successfully, Alhamdulillah