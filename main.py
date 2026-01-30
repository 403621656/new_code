from fastapi import FastAPI

router = FastAPI()

@router.get("/health_check")
async def health_check() -> bool:
    return True

