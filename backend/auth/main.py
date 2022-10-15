# # from flask import Flask
from sqlalchemy.sql import func

from database import session
from models import User 
from orm import create_user, login_user

import uvicorn, os, logging
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

import pyfiglet

from logger import *


# from elasticapm.contrib.starlette import make_apm_client, ElasticAPM


"""
For PostgreSQL, use the following format:
postgresql://username:password@host:port/database_name

For MySQL:
mysql://username:password@host:port/database_name


User.query.filter_by(firstname='Sammy').all()
User.query.filter_by(id=3).first()

User.query.get(3)
User.query.get_or_404(User_id)

db.session.delete (model object)


## RelationShip
post1 = Post(title='Post The First', content='Content for the first post')
post2 = Post(title='Post The Second', content='Content for the Second post')
post3 = Post(title='Post The Third', content='Content for the third post')

comment1 = Comment(content='Comment for the first post', post=post1)
comment2 = Comment(content='Comment for the second post', post=post2)
comment3 = Comment(content='Another comment for the second post', post_id=2)
comment4 = Comment(content='Another comment for the first post', post_id=1)


db.session.add_all([post1, post2, post3])
db.session.add_all([comment1, comment2, comment3, comment4])

db.session.commit()
"""

"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""

# # os.chdir('/c/Users/user/Desktop/workspace/yara-datastorm/backend/apis/ml/')

app = FastAPI(
    title="AutoML",
    description="""**Auto Machine Learning App**""",
    version="0.0.1",
    contact={
        "name": "YaraData",
        "email": "yaradatateam@gmail.com",
    },
)


# db = SQLAlchemy() 


APP_PORT = os.environ.get("APP_PORT", default=8070)
APP_RELOAD = os.environ.get("APP_RELOAD", default=True)
APP_WORKERS = os.environ.get("APP_WORKERS", default=3)


# # elastic
# apm = make_apm_client(
# {
#     'SERVICE_NAME': '<SERVICE-NAME>',
#     'SECRET_TOKEN': '<SECRET-TOKEN>',
# })
# app = FastAPI()
# app.add_middleware(ElasticAPM, client=apm)
# # usage
# # apm.client.capture_exception()
# # apm.client.capture_message('hello, world!')



@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.get('/status')
def status():
    logger.info("{'status':'ok'}")
    return {'status':'ok'}


@app.get("/register")
def register():
    try:
        u = User(username='hey',firstname='hey',lastname='way',email='hway@gmail.com',password='00000000',bio='Sportif')
        admin_user = create_user(session, u)
        logger.info(f"register {admin_user}") 
        return {"msg": "user created"}
    except Exception as e:
        logger.error(f"{e}")
        raise "errorr"

@app.get("/login")
def login(email:str='hway@gmail.com', password:str='00000000'):
    try:
        # u = {'email':'hway@gmail.com','password':'00000000'}
        u = {'email':email,'password':password}
        user = login_user(session, dict(u))

        logger.info(f"login {user}") 
        return {'status': f'{user}'}
    except Exception as e:
        logger.error(f"{e}")
        return f"error {e}"


if __name__ == "__main__":

    result = pyfiglet.figlet_format("CIRCUS")
    print(result)

    uvicorn.run("main:app", host="0.0.0.0", port=int(APP_PORT), reload=APP_RELOAD, workers=int(APP_WORKERS)) 
    

