with open("traces/task2_p2.din", 'w') as f:
    for _ in range(50):
        for i in range(0,256,32):
            f.write("0 " + hex(i)[2:] + "\n")
        for i in range(8,256,32):
            f.write("0 " + hex(i)[2:] + "\n")

