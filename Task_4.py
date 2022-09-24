# with open('Task_4_initial.txt', 'w') as f:
  # f.write("aaaaaaabbbbbbbbbllllll")


with open('Task_4_initial.txt', 'r') as a:
    data = a.read()


def f(data):
    final_line = '' 
    prev_item = ''
    count = 1 
    if not data:
         return '' 
    for item in data: 
        if item != prev_item:
            if prev_item:
                final_line += str(count) + prev_item
            count = 1
            prev_item = item
        else:
            count += 1
    else:
        final_line += str(count) + prev_item
    return final_line
print(f(data))


res = f(data)


with open('Task_4_output.txt', 'w') as n:
    n.write(f'{res}\n')


with open ('Task_4_output.txt', 'r') as s:
    my_line = s.read()


def unpack(my_line):
    new_str = ""
    count = ""
    for i in my_line:
        if i.isdigit():
            count += i
        else:
             new_str += i * int(count)
             count = ""
    return new_str
print(unpack(my_line))

