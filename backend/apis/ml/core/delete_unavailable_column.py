def delete_unavailable_column(dataframe, seuil=0.25) -> list:
    """
    missing value > 25%
    """
    try:
        df_int = dataframe.isnull().sum()
        df_int = df_int.to_frame("missing").reset_index()

        columns_delete = df_int['index'][df_int["missing"] > dataframe.shape[0]*seuil].values

        dataframe.drop(columns_delete, axis=1, inplace=True) 

        return dataframe
    except Exception as ex:
        raise('something wrong')