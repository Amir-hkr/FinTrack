from fastapi import FastAPI

app = FastAPI(
    title="FinTrack API",
    version="1.0.0",
    description="Portfolio Tracker API",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to FinTrack API"}