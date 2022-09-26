def delete_row_where_label_is_empty(dataframe, label):
    try:
        return dataframe[dataframe[label].isnull()==False]
    except Exception as ex:
        raise 'something is wrong'