import pandas as pd


def prepare(file_name, data_column, label_column):
    file = pd.read_csv(file_name, encoding='latin-1', engine='python')
    temp = []
    msg_array = []
    label = []

    for index, row in file.iterrows():
        temp.append(row[data_column])
        label.append(row[label_column])

    for i in range(len(temp)):
        msg_array.append(temp[i].split(" "))

    return (msg_array, label)

#%%
