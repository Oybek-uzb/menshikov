fin  = open("/home/oybek/menshikov/perestanovki/input.txt")
fout = open("/home/oybek/menshikov/perestanovki/output.txt","a")

str = fin.readline()
str_len = len(str)
is_used = [False for i in str]

def p(m: int, prefix = []):
    if m == 0:
        fout.write("".join(prefix)+"\n")
        return
    
    for i in range(0, str_len):
        if is_used[i]:
            continue

        prefix.append(str[i])
        is_used[i] = True
        p(m-1, prefix)

        prefix.pop()
        is_used[i] = False

p(str_len)

fin.close()
fout.close()

# Done successfully, Alhamdulillah