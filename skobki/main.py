fin  = open("/home/oybek/menshikov/skobki/input.txt")
fout = open("/home/oybek/menshikov/skobki/output.txt","w")

str = fin.readline()
len_str = len(str)
print(len_str)
open = ["(", "[", "{"]
close = [")", "]", "}"]

arr = []
char = ""
is_correct = True

if len_str%2 == 1:
    is_correct = False
else:
    for i in str:
        if i in open:
            arr.append(i)
            continue
        elif not arr:
            is_correct = False
            break
        else:
            char = arr.pop()
            if not ((i == ")" and char == "(") or (i == "]" and char == "[") or (i == "}" and char == "{")):
                is_correct = False
                break

fout.write("Yes" if is_correct else "No")


fin.close()
fout.close()

# Done successfully, Alhamdulillah