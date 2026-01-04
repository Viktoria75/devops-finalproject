from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Final Project V1 - Deployed via ArgoCD"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Simulating a developer leaving a hardcoded secret
password = "secret_password_123"