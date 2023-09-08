from fastapi import FastAPI

from backend.app.routers import notes, users

app = FastAPI()


app.include_router(users.router)
app.include_router(notes.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}