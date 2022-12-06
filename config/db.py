from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine =  create_engine("mysql+pymysql://admin:Skills39@163.18.71.78:9906/insurance")
meta = MetaData()
conn = engine.connect() 





