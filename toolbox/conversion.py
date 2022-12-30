

def conversion(spam_array, data_array):

    final_array = []

    for i in range(len(data_array)):
        temp = []
        for j in range(len(data_array[i])):
            if any(data_array[i][j] in sublist for sublist in spam_array):
                temp.append(1)
            else:
                temp.append(0)
        final_array.append(temp)

    return final_array

#%%
