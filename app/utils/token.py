from datetime import timedelta, datetime, timezone
import jwt
import secrets
from environs import Env
env = Env()
env.read_env()

access_secret = env.str("AccessTokenSecret")
refresh_secret = env.str("RefreshTokenSecret")
generate_secret_Token = env.str("GenerateResetToken")

algorithm = "HS256"


def generate_access_token(data: int, expires_delta:timedelta = timedelta(minutes=15))->str:
    to_encode ={"id": data}
    print("data",to_encode)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, access_secret, algorithm)

def generate_refresh_token(data: dict, expires_delta:timedelta = timedelta(days=15))->str:
    to_encode ={"id": data}
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, refresh_secret, algorithm)


def generateResetToken(data:dict, expires_delta:timedelta = timedelta(minutes=5))->str:
    to_encode ={"email": data["email"]}
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, generate_secret_Token, algorithm)