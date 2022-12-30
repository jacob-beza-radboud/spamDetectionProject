
def reshape(a):
    temp = []
    for i in a:
        temp.append(len(i))
    curr_max = max(temp)

    for r in a:
        for m in range(abs(len(r) - curr_max)):
            r.append(0)