from pandas import read_csv

def load_external_test_data():
    load = read_csv("./data/spam_database.csv")
    load_arr = []
    converted = []
    test_label = []

    for index, row in load.iterrows():
        load_arr.append(row['text'])
        if row['type'] == "spam":
            test_label.append(1)
        else:
            test_label.append(0)

    for i in range(len(load_arr)):
        converted.append(load_arr[i].split(" "))

    return (converted, test_label)