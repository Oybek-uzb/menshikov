fin  = open("/home/oybek/menshikov/perestanovki_v2/input.txt")
fout = open("/home/oybek/menshikov/perestanovki_v2/output.txt","a")

chars = [char for char in fin.readline()]
chars_len = len(chars)

used_chars = []

def permutations(m, prefix = []):
    global used_chars
    if m == 0:
        print(prefix)
        return
    
    for i in chars:
        if i in used_chars:
            continue
        
        prefix.append(i)
        permutations(m-1, prefix)
        prefix.pop()

permutations(chars_len)
fin.close()
fout.close()

# Done successfully, Alhamdulillah