from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from flask_bcrypt import Bcrypt
import logging as LOGGER
from models import User

from werkzeug.security import generate_password_hash, check_password_hash

bcrypt = Bcrypt()

def create_user(session:Session, user:User):
    try:
        existing_user = session.query(User).filter(User.email == user.email).first()
        if existing_user is None:
            user.password = bcrypt.generate_password_hash(user.password)
            session.add(user)  # Add the user
            session.commit()  # Commit the change
            LOGGER.info(f"Created user: {user}")
        else:
            LOGGER.info(f"Users already exists in database: {existing_user}")
        return session.query(User).filter(User.email == user.email).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e 

def login_user(session:Session,user:dict):
    
    try:
        existing_user = session.query(User).filter(User.email==user['email']).first()
        
        # bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
        if bcrypt.check_password_hash(existing_user.password, user['password']) == False:
            LOGGER.info(f"Please check your login details and try again {user['email']}")
            return str(False) # if user doesn't exist or password is wrong, reload the page
        else:
            LOGGER.info(f"successfully login: {user['email']}")
        return existing_user
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when loging user: {e}")
        raise e 

