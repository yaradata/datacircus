"""
    
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def imputation_feature_column(dataframe, label):
    try:
        features = list(set(dataframe.columns) - set([label])) # columns without label
        
        for col in features:
            # int or float
            if dataframe[col].dtype=='int64' or dataframe[col].dtype=='float64':
                moy = dataframe[col].mean()
                # dataframe[col][dataframe[col].isnull()==True] = moy 
                dataframe[col].fillna(value=moy,inplace=True)
            # object
            elif dataframe[col].dtype=='object':
                mode = dataframe[col].mode()[0]
                # dataframe[col][dataframe[col].isnull()==True] = mode
                dataframe[col].fillna(value=mode,inplace=True)
            else:
                continue

        return dataframe
    except Exception as ex:
        raise ('b something is wrong')


