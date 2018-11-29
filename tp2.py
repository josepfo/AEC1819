# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:55:54 2018

@author: zeped

"""

import pandas as pd 
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt 

df = pd.read_csv('Dataset_DecisionPSS.csv', sep=';', 
                 header=0, encoding='ascii', engine='python')



#Data Visualization ---------------------------------------------------------

#Estamos a usar um scatter_matrix para verificar a variação dos vários atributo
#em relação ao PSS_Stress TODO-> Arranjar gráficos que demonstrem melhor as 
#relações


pd.plotting.scatter_matrix(df.loc[:,["PSS_Stress",
                                     "avg_durationperquestion",
                                     "decision_time_efficiency",
                                     "avg_tbd",
                                     ]],
                           figsize=(12,10),s=150,marker='D')

"""

pd.plotting.scatter_matrix(df.loc[:,["PSS_Stress",
                                     "good_decision_time_efficiency",
                                     "maxduration",
                                     "median_tbd",
                                     ]],
                           figsize=(20,18),marker='o')

pd.plotting.scatter_matrix(df.loc[:,["PSS_Stress",
                                     "minduration",
                                     "num_decisions_made",
                                     "question_enter_count",
                                     ]],
                           figsize=(20,18),marker='o')


pd.plotting.scatter_matrix(df.loc[:,["PSS_Stress",
                                     "ratio_decisions",
                                     "ratio_good_decisions",
                                     "totalduration",
                                     "variance_tbd",
                                     ]],
                           figsize=(20,18),marker='o')


"""



#Data PRE-PROCESSING --------------------------------------------------------


#Only some median_tdb values are NaN
#Eliminate NaN values with dropna()

FilteredDF = df.dropna()

print(df['median_tbd'])
print(FilteredDF['median_tbd'])


#




