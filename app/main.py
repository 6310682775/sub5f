from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
import models, name

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:7000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(name.router)


@app.get("/check")
def root():
    return {"message": "Health check"}
