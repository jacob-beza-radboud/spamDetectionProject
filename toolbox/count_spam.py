

def count_spam(spam_array, text):
    spam_counter = 0
    for i in range(len(spam_array)):
        for j in spam_array[i]:
            if j in text and (j != "," or j != ','):
                spam_counter += 1
    return spam_counter

