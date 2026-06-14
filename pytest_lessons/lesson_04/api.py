from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

accounts = {
    1: {"name": "Ashish", "balance": 100.0},
    2: {"name": "Ravi", "balance": 50.0},
}


class AmountRequest(BaseModel):
    amount: float


@app.get("/accounts/{account_id}")
def get_account(account_id: int):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts[account_id]


@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, body: AmountRequest):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    if body.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    accounts[account_id]["balance"] += body.amount
    return accounts[account_id]


@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, body: AmountRequest):
    if account_id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    if body.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    if body.amount > accounts[account_id]["balance"]:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    accounts[account_id]["balance"] -= body.amount
    return accounts[account_id]