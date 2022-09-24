# with open('Task_1_initial.txt', 'w') as f:
   # f.write("writeabc a program that removes allabc words containing 'abc' from a text\n")

with open('Task_1_initial.txt', 'r') as a:
    lines = a.read()

d =  " ".join(filter(lambda x: "abc" not in x, lines.split()))

with open('Task_1_output.txt', 'w') as b:
    b.write(d)


