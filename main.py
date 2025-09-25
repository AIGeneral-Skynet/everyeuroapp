from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Vitali, your Python app is running!"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Vitali, your Python app is running!"}

@app.get("/budget")
def get_budget():
    return {
        "income": 5000,
        "expenses": {
            "housing": 1780,
            "transportation": 750,
            "food": 700,
            "personal": 150,
            "savings_and_debt": 1100
        },
        "remaining": 520
    }

