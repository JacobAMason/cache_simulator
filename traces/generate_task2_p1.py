with open("traces/task2_p1.din", 'w') as f:
    for _ in range(50):
        for i in range(0,256,64):
            f.write("0 " + hex(i)[2:] + "\n")

