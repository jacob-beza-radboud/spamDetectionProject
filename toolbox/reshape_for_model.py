
def reshape_for_model(array, nr_features):
    for x in array:
        for s in range(len(x)):
            if x[s] == 0:
                x.pop(s)

    for y in array:
        if len(y) < nr_features:
            for b in range(abs(len(y) - nr_features)):
                y.append(0)
        elif len(y) > nr_features:
            length = len(y) - 1
            while len(y) != nr_features:
                y.pop(length)
                length -= 1
        else:
            continue