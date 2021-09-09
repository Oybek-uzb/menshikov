from os import EX_OSFILE


fin  = open("/home/oybek/menshikov/peresecheniye_otrezkov/input.txt")
fout = open("/home/oybek/menshikov/peresecheniye_otrezkov/output.txt","a")

line_1 = []
line_2 = []

a_x1, a_y1 = map(int, fin.readline().split())
a_x2, a_y2 = map(int, fin.readline().split())
b_x1, b_y1 = map(int, fin.readline().split())
b_x2, b_y2 = map(int, fin.readline().split())


# a, b = map(int, fin.readline().split())
# fout.write(str(a+b))

print(a_y2)

fin.close()
fout.close()

# Done successfully, Alhamdulillah