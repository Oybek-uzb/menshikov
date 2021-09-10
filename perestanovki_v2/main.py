fin  = open("/home/oybek/menshikov/perestanovki_v2/input.txt")
fout = open("/home/oybek/menshikov/perestanovki_v2/output.txt","a")

chars = [char for char in fin.readline()]
chars_len = len(chars)
is_used = [False for i in range(0, chars_len)]

def permutations(m, prefix = []):
    if m == 0:
        print(prefix)
        return
    
    for i in chars:
        prefix.append(i)
        permutations(m-1, prefix)
        prefix.pop()

permutations(chars_len)
fin.close()
fout.close()

# Done successfully, Alhamdulillah