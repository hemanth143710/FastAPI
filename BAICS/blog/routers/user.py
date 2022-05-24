from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import database, schemas, models
from .. hashing import Hash
from ..repository import user

get_db = database.get_db
router = APIRouter()



@router.post('/user',response_model=schemas.ShowUser,tags=['users'])
def create_user(request: schemas.User,db: Session = Depends(get_db)):

    # new_user = models.NewUser(name=request.name,email=request.email, password=Hash.bcrypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user

    return user.create(request,db)

@router.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
def get_user(id:int,db: Session = Depends(get_db)):
    # user = db.query(models.NewUser).filter(models.NewUser.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    # return user

    return user.show(id,db)
