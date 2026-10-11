from server import home,app,my_function
from fastapi.testclient import TestClient
from pytest import MonkeyPatch
import server
patch=MonkeyPatch()


import pytest
client=TestClient(app)

def test_home():
    reponse=client.get("/home")
    assert reponse.status_code==200
    assert reponse.json()=={"message":"welcome home"}
    
def test_exemple():
    reponse= client.get("/async")
    assert reponse.status_code==200
    assert reponse.json()=={"message":"function executed"}
    

def test_register():
    new_users=[]
    patch.setattr(server,"users",new_users)
    reponse= client.post(
        "/register",
        params={
            "email":"email",
            "password":"password",
            "name":"name",
            "phone":"phone"
        }
    )
    
    assert reponse.status_code==200
    assert reponse.json()=={"message":"user register successfully"}
    assert len(new_users)==1
    