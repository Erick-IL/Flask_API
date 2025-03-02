from flask_openapi3 import APIBlueprint, Tag

blueprint = APIBlueprint("user_api", __name__, url_prefix="/v1")
tag_users = Tag(name="Users Functions", description="Routes CRUD")

@blueprint.get(
    "/get-users",
    summary="Get All Users",
    description="Return all users in DataBase.",
    tags=[tag_users],
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
        }
    }
)
def get_all_users():
    return