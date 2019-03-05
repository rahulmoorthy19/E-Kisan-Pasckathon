import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import seaborn as sns
water = {'Castor seed':500, 
         'Potato':600, 
         'Other oilseeds':550,
         'Cotton':1000,
         'Groundnut':650, 
         'Sunflower':425, 
         'Onion':450,
         'Sugarcane':2000,
         'Sannhamp':550,
         'Dry chillies':500, 
         'Maize':650,
         'Coriander':600,
         'Jowar':1000,
         'Wheat':550,
         'Other kharif pulses':800,
         'Barley':410,
         'Arhar/tur':900,
         'Gram':600,
         'Safflower':300,
         'Bajra':650,
         'Urad':370,
         'Rice':1700, 
         'Garlic':425,
         'Sesamum':700,
         'Moong':470,
         'Mustard':250,
         'Rapeseed & mustard':425,
         'Horse-gram':800,
         'Linseed':475,
         'Moth':230,
         'Tapioca':400,
         'Small millets':550,
         'Tobacco':500,
         'Peas':425,
         'Ragi':425, 
         'Masoor':450,
         'Soyabean':575, 
         'Other rabi pulses':800,
         'Guar seed':500, 
         'Sweet potato':600,
         'Niger seed':800,
         'Turmeric':600,
         'Ginger':1000,
         'Sanhump':550,
         'Banana':1700,
         'Khesari':800,
         'Peas & beans (pulses)':400, 
         'Black pepper':2025,
         'Mesta':500,
         'Arecanut':900,
         'Cashewnut':1750,
         'Jute':500,
         'Cardamom':2250,
         'Cowpea':460
        }
def crop_water(X, district):
    X['Water'] = X['Crop'].map(water)
    X = X.loc[X['District'] == district]
    X = X[['Crop','Yield','Water']]
    X = X.groupby(['Crop']).mean()
    X = X.sort_values(by=['Yield'],ascending=False)
    X = X[:5]
    X['Crop']= X.index
    X = X.round({'Yield':2})
    plt.bar(X['Crop'],X['Water'])
    for a,b in zip(X['Crop'], X['Water']):
        plt.text(a, b, str(b))
        
    plt.xlabel('Crops')
    plt.ylabel('Water (in mm)')
    plt.title('Crop vs Water require')
    plt.savefig('/home/sirzechlucifer/ML and ROS/e-Kisan/kisan_portal/portal/static/water_predict/images/CvsW.png')