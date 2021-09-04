fin  = open("/home/oybek/menshikov/prostiye_chisla/input.txt")
fout = open("/home/oybek/menshikov/prostiye_chisla/output.txt","a")

a, b = map(int, fin.readline().split())
fout.write(str(a+b))

fin.close()
fout.close()

# Done successfully, Alhamdulillah