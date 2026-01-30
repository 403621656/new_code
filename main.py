from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
async def health_check() -> bool:
    return True

