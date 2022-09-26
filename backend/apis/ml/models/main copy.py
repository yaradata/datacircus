import sys, os, time 

# importing grand-parent folder
ml_folder = os.path.dirname(os.path.abspath('./'))
sys.path.insert(0,ml_folder)

print(ml_folder)
from ml.models.regressor.sklearn.Regressor import RegressorModel as SkLearnRegressorModel

# best_model:dict = {
#     "pipeline" : "",
#     "accuracy" : 0,
#     "classifier" : 0
# }

# model_requirement = {"data_url": f"{ml_folder}/static/ff54b71e-9c41-4f13-be45-45d6395a4aa5#1987.csv","data_sep": ",","label": "ArrTime"}

print('gjuuuuuuuuuuuuuuuu')
start = time.time()

async def process(label_type,file_info={"data_url": f"/mnt/c/Users/user/Desktop/workspace/yara-datastorm/backend/apis/ml/static/ff54b71e-9c41-4f13-be45-45d6395a4aa5#1987.csv","data_sep": ",","label": "ArrTime"}):
    outputs = [] # result of all model(sklearn, pytorch)

    
    if (label_type=="qualitative"):
        pass
    elif (label_type=="quantitative"):
        # loop models: regressor(sklearn, pytorch), classifier(sklearn, pytorch)
        for model in [SkLearnRegressorModel(**file_info)]: 
            res = model.get_best_model() 
            outputs.append(res) 
    else:
        pass 

    print(outputs) 

    # get last best_model: loop output
    # save model

    return outputs 

end = time.time()

# process(label_type="quantitative") 

print('temps total: ', float(end - start)/60) 



