from fastapi import FastAPI

app = FastAPI(title="NeuroClinic API")

@app.get("/")
def read_root():
    return {"message": "NeuroClinic API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}