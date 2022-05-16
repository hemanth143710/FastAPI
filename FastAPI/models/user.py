from pydantic import Basemodel
class User(Basemodel):
    name :str
    email:str
    password:str
    