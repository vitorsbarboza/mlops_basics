
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def welcome():
    """
    Rota de boas-vindas com instruções de uso da API de juros compostos.
    """
    return {
        "mensagem": "Bem-vindo à API de Juros Compostos!",
        "como_usar": "Envie um POST para /calculate com um JSON contendo: principal (valor inicial), rate (taxa anual em %), time (anos), n (capitalizações por ano, opcional).",
        "exemplo_json": {
            "principal": 1000,
            "rate": 10,
            "time": 2,
            "n": 1
        },
        "exemplo_curl": "curl -X POST http://localhost:8000/calculate -H 'Content-Type: application/json' -d '{\"principal\": 1000, \"rate\": 10, \"time\": 2, \"n\": 1}'"
    }

class CompoundInterestRequest(BaseModel):
    principal: float
    rate: float  # annual interest rate in percent
    time: float  # time in years
    n: int = 1   # number of times interest applied per year

class CompoundInterestResponse(BaseModel):
    final_amount: float
    interest_earned: float

@app.post("/calculate", response_model=CompoundInterestResponse)
def calculate_compound_interest(data: CompoundInterestRequest):
    p = data.principal
    r = data.rate / 100
    t = data.time
    n = data.n
    amount = p * (1 + r/n) ** (n*t)
    interest = amount - p
    return CompoundInterestResponse(final_amount=round(amount, 2), interest_earned=round(interest, 2))
