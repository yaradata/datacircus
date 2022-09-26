

def process(label_type:str,models:list):
    print('dans process ~~~~')
    outputs = [] # result of all model(sklearn, pytorch)
    
    if (label_type=="qualitative"):
        pass
    elif (label_type=="quantitative"):
        # loop models: regressor(sklearn, pytorch), classifier(sklearn, pytorch)
        for model in models: 
            res = model.get_best_model() 
            outputs.append(res) 
    else:
        pass 

    # get last best_model: loop output
    # save 
    return outputs 

