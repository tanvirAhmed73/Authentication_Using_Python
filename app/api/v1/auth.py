from fastapi import APIRouter
from schemas.auth import Auth_Msg_Response, UserCreate, Auth_Data_Response, UserLogin
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends
from utils.auth import register_user, login_user
from crud.user import get_user_by_email
from utils.token import generateResetToken
from utils.email import send_reset_email

router = APIRouter()

@router.post("/register", response_model=Auth_Msg_Response, tags= ["auth"])
def register(user:UserCreate, db:Session = Depends(get_db)):
    try:
        existing_user = get_user_by_email(db, user.email)
        if existing_user:
            return {"message":"User already exists"}
        else:
            success= register_user(user, db)
            print(success)
        if success:
            return {"message":"User registered successfully"}
            

    except Exception as e:
        return {"message":str(e)}
    

@router.post("/login", response_model=Auth_Data_Response, tags= ["auth"])
def login(userData:UserLogin, db:Session = Depends(get_db)):
    try:
        existing_user = get_user_by_email(db, userData.email)
        if not existing_user:
            return {"message":"Invalid credentials"}
        else:
            print("user1",existing_user, userData)
            success = login_user(existing_user, userData, db)
            if success:
                print(success)
                return {"username":existing_user.username ,"email":existing_user.email, "is_active":True}
        
            
    except Exception as e:
        return {"message":str(e)}
    

@router.post("/forgetPassword", response_model= dict, tags = ["auth"])
def forget_password(userData:dict , db:Session = Depends(get_db)):
    try:
        existing_user = get_user_by_email(db, userData["email"])
        if not existing_user:
            return 2
        else:
            reset_token = generateResetToken(userData)
            if reset_token:
                #send the reset token to the user email
                send_reset_email(userData["email"], reset_token)
                return {"message": "Password reset link has been sent to your email."}
            
    except Exception as e:
        return 0
        
    