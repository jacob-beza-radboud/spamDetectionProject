import pandas as pd


def prepare(file_name, column_name, labels):
    file = pd.read_csv(file_name, encoding='latin-1', engine='python')
    temp = []
    msg_array = []
    label = []

    for index, row in file.iterrows():
        temp.append(row[column_name])
        label.append(row[labels])

    for i in range(len(temp)):
        msg_array.append(temp[i].split(" "))

    return (msg_array, label)

#%%
