from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'sqlite:///db.sqlite',
    # 'mysql+pymysql://user:password@host:3600/database',
    echo=True,
    connect_args={'check_same_thread': False}
)
Session = sessionmaker(bind=engine)
session = Session() 
