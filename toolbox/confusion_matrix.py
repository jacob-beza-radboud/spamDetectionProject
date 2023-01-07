import numpy as np
import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt


def plot_confusion_matrix(cm, y):
    df_cm = pd.DataFrame(cm, index=[i + 1 for i in np.unique(y)],
                         columns=[i + 1 for i in np.unique(y)])
    plt.figure()
    sn.heatmap(df_cm, annot=True)
    plt.title('Confusion matrix')
    plt.xlabel('Predicted class')
    plt.ylabel('Actual class')
    plt.show()
