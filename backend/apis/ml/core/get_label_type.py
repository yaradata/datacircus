def get_label_type(dataframe, label) -> list:
    """
    with label, detect model
    """
    try:
        label_type = ""
        if (dataframe[label].dtype=="object") :
            label_type = "qualitative"
        elif (dataframe[label].dtype == "float64" or dataframe[label].dtype == "int64"):
            label_type = "quantitative"
        else:
            raise('something wrong')
        return str(label_type)
    except Exception as ex:
        raise('something wrong')