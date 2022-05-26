from fastapi import APIRouter, Depends, status, HTTPException, responses
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database, models, oauth2
from  .. import database
from .. repository import blog, user
get_db = database.get_db
router = APIRouter()
get_current_user = oauth2.get_current_user

@router.post('/blog', status_code=status.HTTP_201_CREATED,tags=['blog'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db)
    
@router.get('/blog',response_model=List[schemas.ShowBlog],tags=['blog'])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)
   
@router.get('/blog/{id}',response_model=schemas.ShowBlog,tags=['blog'])
def show(id:int,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details':f"Blog with the id {id} is not available"}
    return blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
def destroy(id:int, db : Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    # blog .delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.destroy(id,db)
 
@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    # blog.update(request)
    # db.commit()
    # return "updated"

    return blog.update(id,request,db)

