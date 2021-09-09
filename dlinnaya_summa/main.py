fin  = open("/home/oybek/menshikov/dlinnaya_summa/input.txt")
fout = open("/home/oybek/menshikov/dlinnaya_summa/output.txt","a")

a, b = map(int, fin.readline().split())
fout.write(str(a+b))

fin.close()
fout.close()

# Done successfully, Alhamdulillah