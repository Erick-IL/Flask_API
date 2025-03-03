from flask_openapi3 import APIBlueprint, Tag
from app.commons.dtos import Token, get_user

blueprint = APIBlueprint("user_api", __name__, url_prefix="/v1")
tag_users = Tag(name="Users Functions", description="Routes CRUD")

@blueprint.get(
    "/get-users",
    summary="Get All Users",
    description="Return all users in DataBase.",
    tags=[tag_users],
    security=[{"BearerAuth": []}],
    responses={
        403: {
            "description": "Forbidden - missing token.",
            "content": {
                "application/json": {
                    "example": {
                        "message": 'missing token'
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized - invalid token.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'invalid token',
                    }
                }
            }
        },
        406: {
            "description": "Unauthorized - expired token.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'expired token',
                    }
                }
            }
        },
        404: {
            "description": "Not Found",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'Users Not Found',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server error]',
                    }
                }
            }
        },
        200: {
            "description": "Ok",            
            "content": {
                "application/json": {
                    "example": {
                        "users": [  # Agora a lista tem uma chave associada
                            { "id": 1, "name": "roger", "email": "roger.teste@email.com", "password": "password123" },
                            { "id": 2, "name": "Rodrigo", "email": "rodrigo.teste@email.com", "password": "password123" }
                        ]
                    }

                }
            }
        },
        422: {
            "description": "Unprocessable Entity - Invalid token",            
            "content": {
                "application/json": {
                    "example": {
                        'message': 'Invalid token'
                    }
                }
            }
        }
    }
)
def get_all_users(body: Token):
    return

@blueprint.get(
    "/get-user/<user_info>",
    summary="Get User by ID or Email",
    description="Return desired user in DataBase.",
    tags=[tag_users],
    security=[{"BearerAuth": []}],
    responses={
        403: {
            "description": "Forbidden - missing token.",
            "content": {
                "application/json": {
                    "example": {
                        "message": 'missing token'
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized - invalid token.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'invalid token',
                    }
                }
            }
        },
        406: {
            "description": "Unauthorized - expired token.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'expired token',
                    }
                }
            }
        },
        404: {
            "description": "Not Found",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'User Not Found',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server error]',
                    }
                }
            }
        },
        200: {
            "description": "Ok",            
            "content": {
                "application/json": {
                    "example": {
                        "user": [
                            { "id": 1, "name": "roger", "email": "roger.teste@email.com", "password": "password123" }
                        ]
                    }

                }
            }
        },
        422: {
            "description": "Unprocessable Entity - Invalid token",            
            "content": {
                "application/json": {
                    "example": {
                        'message': '[Validation error]'
                    }
                }
            }
        }
    }
)
def get_user_by_id(body: get_user):
    return

@blueprint.delete(
    "/get-user/<user_info>",
    summary="Delete User by ID or Email",
    description="Delete desired user in DataBase.",
    tags=[tag_users],
    security=[{"BearerAuth": []}],
    responses={
        403: {
            "description": "Forbidden - missing token.",
            "content": {
                "application/json": {
                    "example": {
                        "message": 'missing token'
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized - invalid token.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'invalid token',
                    }
                }
            }
        },
        406: {
            "description": "Unauthorized - expired token.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'expired token',
                    }
                }
            }
        },
        404: {
            "description": "Not Found",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'user not found or already deleted',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server error]',
                    }
                }
            }
        },
        204: {
            "description": "No Content - Deleted User",            
            "content": {
                "application/json": {
                    "example": {
                        'message': 'User Deleted'
                    }

                }
            }
        },
        422: {
            "description": "Unprocessable Entity - Invalid token",            
            "content": {
                "application/json": {
                    "example": {
                        'message': '[Validation error]'
                    }
                }
            }
        }
    }
)
def delete_user(body: Token):
    return

@blueprint.patch(
    "/get-user/<user_info>",
    summary="Update user User by ID or Email",
    description="Return desired user in DataBase.",
    tags=[tag_users],
    security=[{"BearerAuth": []}],
    responses={
        403: {
            "description": "Forbidden - missing token.",
            "content": {
                "application/json": {
                    "example": {
                        "message": 'missing token'
                    }
                }
            }
        },
        401: {
            "description": "Unauthorized - invalid token.",           
            "content": {
                "application/json": {
                    "example": {
                        "message": 'invalid token',
                    }
                }
            }
        },
        406: {
            "description": "Unauthorized - expired token.",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'expired token',
                    }
                }
            }
        },
        404: {
            "description": "Not Found",            
            "content": {
                "application/json": {
                    "example": {
                        "message": 'User Not Found',
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",            
            "content": {
                "application/json": {
                    "example": {
                        "message": '[Server error]',
                    }
                }
            }
        },
        200: {
            "description": "Ok",            
            "content": {
                "application/json": {
                    "example": {
                            "name": "roger", "email": "roger.teste@email.com", "password": "password123"
                    }

                }
            }
        },
        422: {
            "description": "Unprocessable Entity - Invalid token",            
            "content": {
                "application/json": {
                    "example": {
                        'message': '[Validation error]'
                    }
                }
            }
        },
        400: {
            "description": "Bad Request - Insufficient data",            
            "content": {
                "application/json": {
                    "example": {
                        'message': 'insufficient data'
                    }
                }
            }
        }
    }
)
def update_user(body: Token):
    return