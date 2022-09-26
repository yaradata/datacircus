from concurrent.futures import process
import uvicorn, os
from fastapi import FastAPI, APIRouter, File, Request 

import requests

from models.regressor.sklearn.Regressor import RegressorModel as SklearnRegressorModel
from models.main import process      

from commons import get_status

regressor_router = APIRouter() # FastAPI()

# {"data_url": "static/ff54b71e-9c41-4f13-be45-45d6395a4aa5#1987.csv","data_sep": ",","label": "ArrTime"}
@regressor_router.post("/processs", tags=["saml"])
def entrypoint(file_info:dict):
    # filepath:str, label:str, sep=str 
    # process = process(label_type="quantitative",file_info={"data_url":filepath,"data_sep": sep,"label":label})
    # process = process(label_type="quantitative",file_info={"data_url":filepath,"data_sep": sep,"label":label})

    
    # process = await process(label_type="quantitative",file_info={"data_url":filepath,"data_sep": sep,"label":label})

    # input_ = {
    #     "data_url":"/mnt/c/Users/user/Desktop/workspace/yara-datastorm/backend/apis/ml/static/36138f2e-eebe-46fb-babb-2a76393a0301#data.csv",
    #     "data_sep": ",",
    #     "label":"revenu"
    # }

    
    # process = process(label_type="quantitative",file_info=input_)

    # print('dans process...')
    # print(get_status())
    # url = "http://localhost:8070/common/status"
    # print(requests.get(url))

    res = process(label_type="quantitative",models=[SklearnRegressorModel(**file_info)])
    
    # return {"result":"res"}
    return {"result":res}



