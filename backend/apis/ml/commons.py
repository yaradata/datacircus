import uvicorn, os, sys
from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException

from fastapi.responses import ORJSONResponse, HTMLResponse, JSONResponse, UJSONResponse

from models.regressor.sklearn.Regressor import RegressorModel

from pathlib import Path
import shutil # save upload file
import uuid

import pandas as pd
from pydantic import BaseModel

from core import memory_data
from core.chunksize_data import chunksize_data
from core.validate_url import validate_url
from core.convert_file_size import convert_file_size

# import logger 
from core.logger import *


common_router = APIRouter() # FastAPI()


ml_folder = os.path.dirname(os.path.abspath('../'))
sys.path.insert(0,ml_folder)
print(ml_folder)
base_file_path = f"{ml_folder}/apis/ml/static/"

class UploadWithUrlInputModel(BaseModel):
    data_url:str
    sep:str = ","

class InfoColumnsInputModel(BaseModel):
    filepath:str
    sep:str = ","



# ========================================

@common_router.get("/status")
def get_status():
    return {"status": "ok"}



@common_router.post("/upload_file", tags=["upload"])   
async def upload_file(file:UploadFile=File(...)):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """
    try:
        myuuid = uuid.uuid4()
        fname = "{}#{}".format(myuuid, file.filename)
        fname = fname.split(' ')
        fname = ''.join(fname)
        
        file_path = base_file_path + fname
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    except Exception as ex:
        logger.error(f'upload file {ex}')
        raise HTTPException(status_code=404, detail=str(ex))

    file_size = await convert_file_size(file_path)
    res = {"old_filename": file.filename, "filename": fname, "filepath": file_path, "filesize":file_size}
    logger.info(f'upload file {res}')
    return res


@common_router.post("/read_url", tags=["upload"])  
async def read_url(data:UploadWithUrlInputModel):
    """
    > **file:str**
    >> Variables à predire (ex: y)
    """
    # return str(dir(validate_url))

    try:
        data_url = data.data_url
        sep = data.sep

        if validate_url(url=data_url): # if data_url is link

            if data_url.endswith('.csv'): # csv management
                df = chunksize_data(data_url=data_url,sep=sep)
                
                myuuid = uuid.uuid4()
                fname = "{}#{}".format(myuuid, data_url.split('/')[-1])
                file_path = base_file_path + fname
                df.to_csv(file_path, sep=sep, index=False)

                file_size = convert_file_size(file_path)
                res = {"url": data_url, "filename": fname, "filepath":file_path, "filesize":file_size}
                # res = {"url": data_url, "filename": fname, "filepath":file_path}
                logger.info(f'read url {res}')
                print(f'read url {res}')
                return res

            elif data_url.endswith('.xls') or data_url.endswith('.xlsx'): # xls management
                logger.info(f'read url : le format xls ou xlsx n est pas prise en charge')
                return {'message':'le fichier est au format xls ou xlsx'}

            else:
                logger.info(f'read url : file is not csv')
                raise HTTPException(status_code=400, detail=f"read url : quelques chose ne va pas")

        else:
            logger.error(f'{data_url} is not link')
            raise HTTPException(status_code=400, detail=f"{data_url} is not link")
    except Exception as ex:
        logger.error(f'read url {ex}')
        raise HTTPException(status_code=500, detail="error de lecture "+str(ex))

    # raise HTTPException(status_code=404, detail=str('read url  error'))


@common_router.post("/dataframe/columns", tags=["info"])   
async def data_info_columns(data:InfoColumnsInputModel):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        filepath = data.filepath
        sep = data.sep

        print("info columns...")
        df = pd.read_csv(filepath, sep=sep)

        res = {'columns': list(df.columns)}
        logger.info(f'data info columns {res}')
        return res
    except Exception as ex:
        logger.error(f'data info columns {ex}')
        raise HTTPException(status_code=404, detail=str(ex))

@common_router.post("/dataframe/columns_type", tags=["info"])   
async def data_info_columns_type(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        df = pd.read_csv(filepath, sep=sep)
        df = pd.DataFrame(df.dtypes, columns=["type"])
        
        df['type'] = df['type'].apply(str)
        df = df.reset_index()

        df.rename({'index':'column'}, axis=1, inplace=True)
        res = df.to_dict('records')

        # static/f0369d5d-1c22-4599-84a1-79e0dfb63fae#credit_data.csv

        res = list(res)
        logger.info(f'data info columns {res}')
        return res

    except Exception as ex:
        logger.error(f'data info columns {res}')
        raise HTTPException(status_code=404, detail=str(ex))


@common_router.get("/dataframe/shape", tags=["info"])   
async def data_info_shape(filepath:str, sep:str=','):
    """
    > **features:str**
    >> Variables à predire (ex: y)
    """
    try:
        df = pd.read_csv(filepath, sep=sep)
        res = {'raw': int(df.shape[1]), 'columns': int(df.shape[0])}
        logger.info(f'data info columns {res}')
        return res
    except Exception as ex:
        logger.error(f'data info columns {res}')
        raise HTTPException(status_code=404, detail=str(ex))




