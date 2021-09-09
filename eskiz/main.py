fin  = open("/home/oybek/menshikov/eskiz/input.txt")
fout = open("/home/oybek/menshikov/eskiz/output.txt","a")

a, b = map(int, fin.readline().split())
fout.write(str(a+b))

fin.close()
fout.close()

# Done successfully, Alhamdulillah