from sqlalchemy.orm import Session
from schemas.auth import UserCreate
from utils.passwordHash import get_password_hash, verify_password
from models.user import User
from utils.token import generate_access_token, generate_refresh_token
from fastapi import Response

# Cookie expiration constants
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30

def register_user(user:UserCreate, db:Session) -> bool:
    #hash the password
    hashed_password = get_password_hash(user.password)
    print(hashed_password)
    #create a new user object
    db_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password
    )
    # add and commit to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return True


def login_user(existing_user:User, userData:UserCreate, response: Response) -> dict:
    #verify the password is correct or not
    passwordIsCorrect = verify_password(userData.password, existing_user.password)
    if passwordIsCorrect:
        print("password is correct")
        #if true make access token and refresh token
        access_token = generate_access_token(existing_user.id)

        # set access token in the cookies
        response.set_cookie(key="access_token", value=access_token, httponly=True)

        refresh_token = generate_refresh_token(existing_user.id)

        #set refresh token in the cookies
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        # Return user data in the response
        return {"message": "Login successful", "username":existing_user.username ,"email":existing_user.email, "is_active":True}
    
    return {
        "message": "Invalid credentials"
    }


    


    