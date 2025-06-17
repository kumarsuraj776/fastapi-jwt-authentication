from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.user import router as user_router
from routes.auth.auth_routes import router as auth_router

# Creating all tables in the database at starting
from core.database import engine, Base
# Import your models here
from models.user import User
# Create all tables
Base.metadata.create_all(bind=engine)


app=FastAPI(
    title="Welcome",
    description="JWT Authentication"
)
app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def health_check():
    return JSONResponse(content={
        "message":"API Working",
        "status":"Running..."
    })