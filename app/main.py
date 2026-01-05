from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Final Project V1 - Added Trivy and Ingress"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

