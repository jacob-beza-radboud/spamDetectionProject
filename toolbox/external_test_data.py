from pandas import read_csv

def load_external_test_data():
    load = read_csv("./data/test_spam_model.csv")
    load_arr = []
    converted = []
    test_label = []

    for index, row in load.iterrows():
        load_arr.append(row['Message'])
        if row['Category'] == "spam":
            test_label.append(1)
        else:
            test_label.append(0)

    for i in range(len(load_arr)):
        converted.append(load_arr[i].split(" "))

    return (converted, test_label)