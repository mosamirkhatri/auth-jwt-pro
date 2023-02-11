# Library Imports
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials


# Import from files
from ..core.utils.config import Config
from ..core.auth.auth_bearer import LoginRequired
from ..core.auth.auth_handler import sign_jwt
from ..core.database.users import USERS
from ..core.database.user_roles import UserRole

router = APIRouter(prefix="/auth")
security = HTTPBasic()


@router.get("/", name="Auth Router Health", tags=["Health"])
@router.get("/health", name="Auth Router Health", tags=["Health"])
def router_test():
    return "Auth Router Working"


user_login_required = LoginRequired([UserRole.USER])
admin_login_required = LoginRequired([UserRole.ADMIN])
mod_login_required = LoginRequired([UserRole.MODERATOR])

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# @router.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # validate the user's credentials here
#     # if valid, create and return a new access token
#     return {"access_token": "my_access_token", "token_type": "bearer"}

# @router.get("/protected")
# async def protected_route(token: str = Depends(oauth2_scheme)):
#     # verify the token here
#     # if valid, return the protected data
#     return {"data": "my_protected_data"}


@router.post("/login", tags=["Auth Route"], name="Login")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username.strip().lower()
    password = credentials.password
    verified_user = None
    for user in USERS:
        if user.get("username") == username:
            verified_user = user
            break
    if verified_user is None:
        return JSONResponse(
            content={"success": False, "message": "User Not Found"},
            status_code=404,
        )
    if verified_user.get("password") != password:
        return JSONResponse(
            content={"success": False, "message": "Credentials Mismatch"},
            status_code=403,
        )
    token = sign_jwt(verified_user.get("id"), verified_user.get("role"))
    *access_token, sign = token.split(".")
    access_token = ".".join(access_token)
    response = JSONResponse(
        content={"access_token": access_token, "token_type": "Bearer"}
    )
    response.set_cookie(
        "sign",
        sign,
        httponly=True,
        secure=True,
        samesite=Config.SAME_SITE_POLICY,
        expires=Config.ACCESS_TOKEN_EXPIRE_MINUTES * 60 + 300,
    )
    return response


@router.post(
    "/protected-user", tags=["Login Required Routes"], name="Post Login - User"
)
def protected_user(user=Depends(user_login_required)):
    print(user)
    return user


@router.post(
    "/protected-admin", tags=["Login Required Routes"], name="Post Login - Admin"
)
def protected_admin(user=Depends(admin_login_required)):
    print(user)
    return user


@router.post(
    "/protected-mod", tags=["Login Required Routes"], name="Post Login - Moderator"
)
def protected_mod(user=Depends(mod_login_required)):
    print(user)
    return user
