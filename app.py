from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt

app = FastAPI()

EMAIL = "23f2004946@ds.study.iitm.ac.in"

ISSUER = "https://idp.exam.local"
AUDIENCE = "tds-3il8kp0d.apps.exam.local"

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuYcxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMIDEkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXcWyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfWed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfISI6iyrYbKR0NEBSqq4XkadEjsCs4LlgniT7GlkL9Mce3b0wGLs9/7ZIXdQIDAQAB
-----END PUBLIC KEY-----"""

class TokenRequest(BaseModel):
    token: str


from fastapi.responses import JSONResponse

@app.post("/verify")
def verify(req: TokenRequest):

    try:

        payload = jwt.decode(
            req.token,
            PUBLIC_KEY,
            algorithms=["RS256"],
            issuer=ISSUER,
            audience=AUDIENCE,
        )

        return {
    "valid": True,
    "email": payload.get("email"),
    "sub": payload.get("sub"),
    "aud": payload.get("aud"),
}

    except InvalidTokenError:
    return JSONResponse(
        status_code=401,
        content={"valid": False}
    )
