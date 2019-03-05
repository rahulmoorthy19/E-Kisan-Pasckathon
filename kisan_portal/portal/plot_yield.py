import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns
#%matplotlib inline
def crop_yield(X, district):
    X = X.loc[X['District'] == district]
    X = X[['Crop','Yield']]
    X = X.groupby(['Crop']).mean()
    X = X.sort_values(by=['Yield'],ascending=False)
    X = X[:5]
    X['Crop']= X.index
    X = X.round({'Yield':2})
    plt.bar(X['Crop'],X['Yield'])
    for a,b in zip(X['Crop'], X['Yield']):
        plt.text(a, b, str(b))
  
    plt.xlabel('Crops')
    plt.ylabel('Yield (in metric tone)')
    plt.title('Crop vs Yield')
    plt.savefig('/home/sirzechlucifer/ML and ROS/e-Kisan/kisan_portal/portal/static/plant_predict/images/CvsY.png')