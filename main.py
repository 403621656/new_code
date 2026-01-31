from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import secrets

app = FastAPI()

bearer = HTTPBearer(auto_error=False)
secret_key = secrets.token_urlsafe(32)

def require_fixed_token(
        cred: HTTPAuthorizationCredentials|None = Depends(bearer)
):
    if cred is None or cred.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Missing token")
    if cred.credentials != secret_key:
        raise HTTPException(status_code=403, detail="Invalid token")
    return cred


@app.get("/test-token")
async def test_token(
        cred: HTTPAuthorizationCredentials = Depends(require_fixed_token)
):
    return cred.credentials

@app.get("/token")
async def get_token():
    return {"token": secret_key}