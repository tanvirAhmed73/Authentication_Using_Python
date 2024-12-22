from fastapi import FastAPI
from database import Base
from database import engine
from api.v1.auth import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

#Include the auth router
app.include_router(auth_router, prefix='/auth')

@app.get('/', tags=['root'])
def read_root():
    return {'Hello': 'World'}