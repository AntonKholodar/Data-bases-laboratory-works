from view import Menu
from controller import Base, engine
from sqlalchemy import *
metadata = MetaData()

Base.metadata.create_all(engine)

Menu.menu()