print("Printing current and previous number and their sum in a range(10)")
previous_num = 0
for i in range(0,10):
    sum = previous_num + i
    print("Current number", i, "previous number", previous_num, "sum", previous_num + i)
    previous_num = i

