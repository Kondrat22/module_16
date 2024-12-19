from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example=22)) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def read_name(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')], age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
