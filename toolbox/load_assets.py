import pandas as pd


def load_spam(file_name):
    spam_file = pd.read_csv(file_name, encoding='latin-1', engine='python')
    temp = []
    spam_array = []


    for index, row in spam_file.iterrows():
        if row['v1'] == 'spam':
            temp.append(row['v2'])

    for i in range(len(temp)):
        spam_array.append(temp[i].split(" "))


    return spam_array

#%%

#%%
