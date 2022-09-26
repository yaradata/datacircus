"""
    LabelEncoder  ---> attribut des valeurs numeriques au variables categorielles
    lbl_encoder = LabelEncoder()
    df['pays_new'] = lbl_encoder.fit_transform(df['pays'])
        > lagos = 37
        > cotonou = 88
        > kigali  = 3
    
    OnehotEncoder ---> creer de nouvel colonne portant le nom de la variable et define 1 si correct 0 sinon

    * float, round(x,4)
    * qualitative variable, nuniq<4, dummy
    * qualitative variable, nuniq>=4, labelencoder
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def transform_feature_column(dataframe, label):
    try:
        features = list(set(dataframe.columns) - set([label])) # columns without label

        for col in features:
            # int 
            if dataframe[col].dtype=='int64':
                pass
            # float
            elif dataframe[col].dtype=='float64':
                # round unit 4 --> 5.001
                dataframe[col] = dataframe[col].apply(lambda x: round(x, 4))
            # object
            elif dataframe[col].dtype=='object':
                # unique value of column
                nunique = dataframe[col].nunique()
                
                if nunique < 4:
                    # dummies
                    dummies_col = pd.get_dummies(dataframe[col])
                    dataframe = dataframe.join(dummies_col)
                    dataframe.drop([col], axis=1, inplace=True)
                else:
                    # label
                    lbl_encoder = LabelEncoder()
                    dataframe[col] = lbl_encoder.fit_transform(dataframe[col])
            else:
                continue

        return dataframe
    except Exception as ex:
        raise ('b something is wrong')


