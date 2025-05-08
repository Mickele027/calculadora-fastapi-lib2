from fastapi import FastAPI, HTTPException
from app.calculadora import operacoes  # Usando a lib

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Calculadora com FastAPI"}

@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": operacoes.soma(a, b)}

@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": operacoes.subtracao(a, b)}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": operacoes.multiplicacao(a, b)}

@app.get("/divisao")
def divisao(a: float, b: float):
    try:
        return {"resultado": operacoes.divisao(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
