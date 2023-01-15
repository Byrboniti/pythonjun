from fastapi import FastAPI
from validate import valid
from database.database import search
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Alexandr Lebedchenko"}



@app.post("/get_form")
async def get_form(request):
    if type(search(valid(request))) == str:
        return {"name": search(valid(request))}
    else:
        return valid(request)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000,host='127.0.0.1',reload=True)
