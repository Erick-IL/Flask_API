from flask_openapi3 import APIBlueprint, Tag
from app.commons.dtos import UserSignup, Userlogin

blueprint = APIBlueprint("api", __name__, url_prefix="/v1")

tag_auth = Tag(name="Auth Jwt", description="Rotas para funcionamento do Jwt authenticator")

@blueprint.get(    
    "/auth/login",
    summary="Login",
    description="Login a user account and get JWT token (1 hour to expire).",
    tags=[tag_auth],
    responses={
        201: {
            "description": "Created - User created successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "roger",
                        "email": "roger.teste@email.com",
                        "password": 'password123'
                    }
                }
            }
        },
        400: {
            "description": "Bad Request - Missing fields.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'insufficient data',
                    }
                }
            }
        },
        422: {
            "description": "Unprocessable Entity - invalid fields.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Validation Error]',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server Error]',
                    }
                }
            }
        }
    }
)
def login(body: Userlogin):
    return

@blueprint.post(
    "/auth/signup",
    summary="Signup",
    description="Create a user account.",
    tags=[tag_auth],
    responses={
        201: {
            "description": "Created - User created successfully.",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "roger",
                        "email": "roger.teste@email.com",
                        "password": 'password123'
                    }
                }
            }
        },
        400: {
            "description": "Bad Request - Missing fields.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'insufficient data',
                    }
                }
            }
        },
        422: {
            "description": "Unprocessable Entity - invalid fields.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Validation Error]',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server Error]',
                    }
                }
            }
        }
    }
)
def signup(body: UserSignup):
    return
